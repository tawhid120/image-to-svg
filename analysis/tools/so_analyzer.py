#!/usr/bin/env python3
"""
so_analyzer.py - Reusable ELF shared-object (.so) analyzer for Android APKs.

Analyzes a native .so / ELF binary and extracts:

  * ELF header info (class, arch, endianness, type, machine, entry point)
  * Program headers (segments) and section headers
  * Dynamic linking info (DT_NEEDED dependencies, SONAME, tags)
  * Exported (defined) and imported (undefined) dynamic symbols
  * Relocations summary
  * All printable strings (ASCII / UTF-8), plus categorized finds:
      - URLs / domains
      - File paths (/proc, /data, /system, assets/, lib/, etc.)
      - Potential secrets (api keys, tokens, AIza..., passwords)
      - JNI / Java class names (L...;) and JNI exports (Java_*)
      - Flutter/Dart snapshot indicators (magic 0xf5f5dcdc, _kDart* symbols,
        build id + feature string)
  * Optional disassembly of exported functions or an address range
    (requires the `capstone` package; falls back to a plain hexdump)

Outputs both human-readable text and machine-readable JSON.

Usage:
    python3 so_analyzer.py <input.so> [-o out.json] [--disasm]
    python3 so_analyzer.py <input.so> --func <address> --length <bytes> [--arch auto]
    python3 so_analyzer.py --help

Requirements:
    Python >= 3.8
    pyelftools  (pip install pyelftools)   - ELF parsing
    capstone    (pip install capstone)     - optional, disassembly only

The tool is generic: it works on any ELF file, not just this project's .so files.
"""

import argparse
import hashlib
import json
import os
import re
import struct
import sys

try:
    from elftools.elf.elffile import ELFFile
    from elftools.elf.dynamic import DynamicSection
    from elftools.elf.sections import SymbolTableSection
    from elftools.elf.relocation import RelocationSection
    HAVE_ELFTOOLS = True
except ImportError:
    HAVE_ELFTOOLS = False

try:
    from capstone import Cs, CS_ARCH_ARM64, CS_ARCH_ARM, CS_ARCH_X86, CS_MODE_ARM, \
        CS_MODE_LITTLE_ENDIAN, CS_MODE_BIG_ENDIAN, CS_MODE_64, CS_MODE_32
    HAVE_CAPSTONE = True
except ImportError:
    HAVE_CAPSTONE = False

# --------------------------------------------------------------------------
# String / pattern extraction
# --------------------------------------------------------------------------

MIN_STR_LEN = 4

URL_RE = re.compile(rb'https?://[A-Za-z0-9._~:/?#\[\]@!$&()*+,;=%-]+')
DOMAIN_RE = re.compile(rb'(?<![\w.])(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(?:/[A-Za-z0-9._~:/?#\[\]@!$&()*+,;=%-]*)?')
PATH_RE = re.compile(rb'(?:/proc|/data|/system|/sdcard|/storage|/mnt|/cache|assets/|lib/|res/|META-INF/)[A-Za-z0-9_./-]*')
SECRET_RE = re.compile(rb'(?i)(api[_-]?key|apikey|secret|token|passwd|password|authorization|bearer|private[_-]?key|BEGIN [A-Z ]*PRIVATE KEY)\s*[=:]\s*[A-Za-z0-9._/+=:-]{8,}')
GOOGLE_KEY_RE = re.compile(rb'AIza[0-9A-Za-z_-]{30,}')
JAVA_CLASS_RE = re.compile(rb'L[a-zA-Z][a-zA-Z0-9_/$.]*;')
JNI_EXPORT_RE = re.compile(rb'^Java_[A-Za-z0-9_]+$')
BASE64_CERT_RE = re.compile(rb'MII[A-Za-z0-9+/]{100,}={0,2}')

MAGIC_DART_SNAPSHOT = b'\xf5\xf5\xdc\xdc'


def extract_strings(data, min_len=MIN_STR_LEN):
    """Yield (offset, ascii_string) for printable ASCII runs."""
    pat = re.compile(rb'[\x20-\x7e]{%d,}' % min_len)
    for m in pat.finditer(data):
        yield m.start(), m.group().decode('ascii', 'replace')


def extract_utf16_strings(data, min_len=MIN_STR_LEN):
    """Yield (offset, string) for little-endian UTF-16 printable runs."""
    pat = re.compile(rb'(?:[\x20-\x7e]\x00){%d,}' % min_len)
    for m in pat.finditer(data):
        raw = m.group().decode('utf-16-le', 'replace')
        yield m.start(), raw


def categorize_strings(all_strings):
    """Given a list of (offset, string), return categorized finds."""
    cats = {'urls': [], 'domains': [], 'paths': [], 'secrets': [],
            'google_keys': [], 'java_classes': [], 'jni_exports': [],
            'embedded_certs': [], 'flutter_indicators': []}

    for off, s in all_strings:
        b = s.encode('ascii', 'ignore')
        if URL_RE.search(b):
            cats['urls'].append((off, s))
        if DOMAIN_RE.search(b) and not URL_RE.search(b):
            cats['domains'].append((off, s))
        if PATH_RE.search(b):
            cats['paths'].append((off, s))
        if SECRET_RE.search(b):
            cats['secrets'].append((off, s))
        if GOOGLE_KEY_RE.search(b):
            cats['google_keys'].append((off, GOOGLE_KEY_RE.search(b).group().decode()))
        if JAVA_CLASS_RE.search(b) and 'L' in s[:2]:
            cats['java_classes'].append((off, JAVA_CLASS_RE.search(b).group().decode()))
        if JNI_EXPORT_RE.match(b):
            cats['jni_exports'].append((off, s))
        if BASE64_CERT_RE.match(b):
            cats['embedded_certs'].append((off, 'base64 DER certificate (%d chars)' % len(s)))
        if 'dart' in s.lower() or 'flutter' in s.lower() or s.startswith('_kDart'):
            cats['flutter_indicators'].append((off, s))
    return cats


def dedupe(items):
    seen = set()
    out = []
    for off, s in items:
        key = s
        if key not in seen:
            seen.add(key)
            out.append((off, s))
    return out


# --------------------------------------------------------------------------
# Flutter / Dart snapshot detection
# --------------------------------------------------------------------------

DART_MAGIC = b'\xf5\xf5\xdc\xdc'


def detect_flutter_snapshot(data, symbols):
    """Look for Dart AOT snapshot indicators in the binary."""
    result = {'is_flutter': False, 'snapshots': [], 'build_id': None,
              'feature_string': None, 'notes': []}

    dart_symbols = [s for s in symbols if s.get('name', '').startswith('_kDart')]
    if dart_symbols:
        result['is_flutter'] = True
        result['snapshots'] = dart_symbols

    pos = 0
    while True:
        idx = data.find(DART_MAGIC, pos)
        if idx < 0:
            break
        # Header: magic (4) + version-ish bytes; build id string follows shortly
        tail = data[idx:idx + 0x200]
        m = re.search(rb'([0-9a-f]{32})([a-z][a-z0-9 -]*)', tail)
        entry = {'offset': idx}
        if m:
            entry['build_id'] = m.group(1).decode()
            feat = m.group(2).decode().strip()
            if feat:
                entry['feature_string'] = feat
                result['build_id'] = entry['build_id']
                result['feature_string'] = feat
        result['snapshots'].append(entry)
        pos = idx + 4
    if result['snapshots']:
        result['is_flutter'] = True
    return result


# --------------------------------------------------------------------------
# ELF analysis
# --------------------------------------------------------------------------

def map_machine(machine):
    m = {
        'EM_386': 'Intel 80386 (x86, 32-bit)',
        'EM_X86_64': 'AMD x86-64',
        'EM_ARM': 'ARM (32-bit)',
        'EM_AARCH64': 'ARM AArch64',
        'EM_MIPS': 'MIPS',
        'EM_RISCV': 'RISC-V',
    }
    return m.get(machine, machine)


def analyze_elf(path, want_disasm=False, disasm_func=None, disasm_len=0):
    if not HAVE_ELFTOOLS:
        sys.exit('ERROR: pyelftools not installed. Run: pip install pyelftools')

    with open(path, 'rb') as f:
        data = f.read()
        elffile = ELFFile(f)

        header = elffile.header
        elf_info = {
            'file': os.path.basename(path),
            'path': path,
            'size_bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'elf_class': 'ELF64' if str(header['e_ident']['EI_CLASS']) == 'ELFCLASS64' else 'ELF32',
            'endianness': 'little' if str(header['e_ident']['EI_DATA']) == 'ELFDATA2LSB' else 'big',
            'os_abi': header['e_ident'].get('EI_OSABI', ''),
            'type': header['e_type'],
            'machine': map_machine(header['e_machine']),
            'machine_raw': header['e_machine'],
            'entry_point': hex(header['e_entry']),
            'phoff': header['e_phoff'],
            'shoff': header['e_shoff'],
            'flags': hex(header['e_flags']),
        }

        # --- Sections ---
        sections = []
        for sec in elffile.iter_sections():
            sections.append({
                'name': sec.name,
                'type': sec['sh_type'],
                'addr': hex(sec['sh_addr']),
                'offset': sec['sh_offset'],
                'size': sec['sh_size'],
                'flags': sec['sh_flags'],
                'link': sec['sh_link'],
                'info': sec['sh_info'],
                'align': sec['sh_addralign'],
            })

        # --- Segments ---
        segments = []
        for seg in elffile.iter_segments():
            segments.append({
                'type': seg['p_type'],
                'offset': seg['p_offset'],
                'vaddr': hex(seg['p_vaddr']),
                'paddr': hex(seg['p_paddr']),
                'filesz': seg['p_filesz'],
                'memsz': seg['p_memsz'],
                'flags': seg['p_flags'],
                'align': seg['p_align'],
            })

        # --- Dynamic ---
        dynamic = {'needed': [], 'soname': None, 'tags': [], 'runpath': None}
        for sec in elffile.iter_sections():
            if isinstance(sec, DynamicSection):
                for tag in sec.iter_tags():
                    t = tag.entry
                    dynamic['tags'].append({'tag': tag['d_tag'], 'value': t.get('d_val', t.get('d_ptr', ''))})
                    if tag['d_tag'] == 'DT_NEEDED':
                        dynamic['needed'].append(tag.needed)
                    elif tag['d_tag'] == 'DT_SONAME':
                        dynamic['soname'] = tag.soname
                    elif tag['d_tag'] == 'DT_RPATH':
                        dynamic['runpath'] = tag.rpath
                    elif tag['d_tag'] == 'DT_RUNPATH':
                        dynamic['runpath'] = tag.runpath

        # --- Symbols ---
        exported, imported = [], []
        for sec in elffile.iter_sections():
            if isinstance(sec, SymbolTableSection):
                for sym in sec.iter_symbols():
                    name = sym.name
                    if not name:
                        continue
                    e = {
                        'name': name,
                        'value': hex(sym['st_value']),
                        'size': sym['st_size'],
                        'type': sym['st_info']['type'],
                        'bind': sym['st_info']['bind'],
                        'vis': sym['st_other']['visibility'],
                        'ndx': sym['st_shndx'],
                    }
                    if sym['st_shndx'] == 'SHN_UNDEF':
                        imported.append(e)
                    else:
                        exported.append(e)

        # --- Relocations ---
        relocs = []
        for sec in elffile.iter_sections():
            if isinstance(sec, RelocationSection):
                for rel in sec.iter_relocations():
                    try:
                        symtab = elffile.get_section(sec['sh_link'])
                        sym = symtab.get_symbol(rel['r_info_sym'])
                        name = sym.name
                    except Exception:
                        pass
                    try:
                        addend = rel['r_addend']
                    except (KeyError, TypeError):
                        addend = None
                    relocs.append({
                        'section': sec.name,
                        'offset': hex(rel['r_offset']),
                        'type': rel['r_info_type'],
                        'symbol': name,
                        'addend': addend,
                    })

        # --- Notes (build-id, android ident) ---
        notes = []
        for sec in elffile.iter_sections():
            if sec['sh_type'] == 'SHT_NOTE':
                try:
                    for note in sec.iter_notes():
                        notes.append({'owner': note['n_name'],
                                      'type': note['n_type'],
                                      'desc': note['n_desc'].decode('latin-1', 'replace') if isinstance(note['n_desc'], bytes) else note['n_desc']})
                except Exception:
                    pass

        # --- Strings ---
        all_strings = list(extract_strings(data))
        cats = categorize_strings(all_strings)
        for k in cats:
            cats[k] = dedupe(cats[k])

        # --- Flutter ---
        flutter = detect_flutter_snapshot(data, exported)

        # --- Disassembly ---
        disasm_out = None
        if want_disasm:
            disasm_out = disassemble_range(path, data, elffile, None, None, None)

        result = {
            'elf': elf_info,
            'sections': sections,
            'segments': segments,
            'dynamic': dynamic,
            'symbols': {'exported': exported, 'imported': imported,
                        'exported_count': len(exported), 'imported_count': len(imported)},
            'relocations': {'count': len(relocs), 'entries': relocs},
            'notes': notes,
            'strings': {
                'total': len(all_strings),
                'urls': cats['urls'],
                'domains': cats['domains'],
                'paths': cats['paths'],
                'secrets': cats['secrets'],
                'google_keys': cats['google_keys'],
                'java_classes': cats['java_classes'],
                'jni_exports': cats['jni_exports'],
                'embedded_certs': cats['embedded_certs'],
                'flutter_indicators': cats['flutter_indicators'],
            },
            'flutter': flutter,
            'disassembly': disasm_out,
        }
        return result


# --------------------------------------------------------------------------
# Disassembly helpers
# --------------------------------------------------------------------------

def arch_from_elf(elffile):
    machine = elffile.header['e_machine']
    data = elffile.header['e_ident']['EI_DATA']
    endian = CS_MODE_BIG_ENDIAN if data == 2 else CS_MODE_LITTLE_ENDIAN
    if machine == 'EM_AARCH64':
        return CS_ARCH_ARM64, CS_MODE_ARM
    if machine == 'EM_ARM':
        return CS_ARCH_ARM, CS_MODE_ARM + (CS_MODE_BIG_ENDIAN if data == 2 else 0)
    if machine == 'EM_X86_64':
        return CS_ARCH_X86, CS_MODE_64 + endian
    if machine == 'EM_386':
        return CS_ARCH_X86, CS_MODE_32 + endian
    return None, None


def disassemble_range(path, data, elffile, start, length, exports):
    if not HAVE_CAPSTONE:
        return {'error': 'capstone not installed (pip install capstone)'}
    arch, mode = arch_from_elf(elffile)
    if arch is None:
        return {'error': 'unsupported architecture for disassembly'}

    out = []
    if start is not None:
        code = data[start:start + length]
        md = Cs(arch, mode)
        md.skipdata = True
        try:
            for ins in md.disasm(code, start):
                out.append('0x%x: %s\t%s' % (ins.address, ins.mnemonic, ins.op_str))
        except Exception as e:
            out.append('disasm error: %s' % e)
    return {'arch': str(elffile.header['e_machine']), 'start': hex(start) if start else None,
            'length': length, 'lines': out}


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

def human_report(result):
    L = []
    e = result['elf']
    L.append('=' * 70)
    L.append('ELF ANALYSIS REPORT')
    L.append('=' * 70)
    L.append('File     : %s' % e['path'])
    L.append('Size     : %d bytes (%.2f KB)' % (e['size_bytes'], e['size_bytes'] / 1024))
    L.append('SHA-256  : %s' % e['sha256'])
    L.append('Class    : %s, %s endian' % (e['elf_class'], e['endianness']))
    L.append('Type     : %s' % e['type'])
    L.append('Machine  : %s' % e['machine'])
    L.append('Entry    : %s' % e['entry_point'])

    L.append('')
    L.append('--- Dynamic ---')
    dyn = result['dynamic']
    L.append('SONAME  : %s' % dyn['soname'])
    L.append('NEEDED  : %s' % (', '.join(dyn['needed']) if dyn['needed'] else '(none)'))

    L.append('')
    L.append('--- Symbols ---')
    syms = result['symbols']
    L.append('Exported (defined) : %d' % syms['exported_count'])
    for s in syms['exported']:
        L.append('  %-6s %-8s %s @ %s (size %s)' % (s['type'], s['bind'], s['name'], s['value'], s['size']))
    L.append('Imported (undefined): %d' % syms['imported_count'])
    for s in syms['imported']:
        L.append('  %s' % s['name'])

    L.append('')
    L.append('--- Sections ---')
    for s in result['sections']:
        if s['name']:
            L.append('  %-22s addr=%s off=%s size=%s' % (s['name'], s['addr'], hex(s['offset']), hex(s['size'])))

    L.append('')
    L.append('--- Segments ---')
    for s in result['segments']:
        L.append('  %-14s off=%s vaddr=%s filesz=%s memsz=%s flags=%s' % (
            s['type'], hex(s['offset']), s['vaddr'], hex(s['filesz']), hex(s['memsz']), s['flags']))

    L.append('')
    L.append('--- Relocations: %d ---' % result['relocations']['count'])
    for r in result['relocations']['entries'][:30]:
        L.append('  %s %s %s %s' % (r['section'], r['offset'], r['type'], r['symbol'] or ''))

    L.append('')
    L.append('--- Notes ---')
    for n in result['notes']:
        d = n['desc'] if len(n['desc']) < 120 else n['desc'][:120] + '...'
        L.append('  %s: %s' % (n['owner'], d))

    st = result['strings']
    L.append('')
    L.append('--- Strings: %d printable strings ---' % st['total'])
    L.append('  URLs (%d):' % len(st['urls']))
    for off, s in st['urls'][:40]:
        L.append('    [0x%x] %s' % (off, s))
    L.append('  Domains (%d):' % len(st['domains']))
    for off, s in st['domains'][:40]:
        L.append('    [0x%x] %s' % (off, s))
    L.append('  Paths (%d):' % len(st['paths']))
    for off, s in st['paths'][:30]:
        L.append('    [0x%x] %s' % (off, s))
    if st['secrets']:
        L.append('  Potential secrets (%d):' % len(st['secrets']))
        for off, s in st['secrets'][:20]:
            L.append('    [0x%x] %s' % (off, s))
    if st['google_keys']:
        L.append('  Google API keys (%d):' % len(st['google_keys']))
        for off, s in st['google_keys'][:20]:
            L.append('    [0x%x] %s' % (off, s))
    if st['jni_exports']:
        L.append('  JNI exports (%d):' % len(st['jni_exports']))
        for off, s in st['jni_exports'][:20]:
            L.append('    [0x%x] %s' % (off, s))
    if st['java_classes']:
        L.append('  Java classes (%d):' % len(st['java_classes']))
        for off, s in st['java_classes'][:20]:
            L.append('    [0x%x] %s' % (off, s))
    if st['embedded_certs']:
        L.append('  Embedded certs (%d):' % len(st['embedded_certs']))
        for off, s in st['embedded_certs']:
            L.append('    [0x%x] %s' % (off, s))

    fl = result['flutter']
    L.append('')
    L.append('--- Flutter/Dart snapshot ---')
    L.append('  Is Flutter AOT: %s' % fl['is_flutter'])
    if fl['build_id']:
        L.append('  Dart build id : %s' % fl['build_id'])
    if fl['feature_string']:
        L.append('  Features      : %s' % fl['feature_string'])
    for snap in fl['snapshots']:
        if 'name' in snap:
            L.append('  %s @ %s size %s' % (snap['name'], snap['value'], snap['size']))
        else:
            L.append('  snapshot blob @ 0x%x build=%s' % (snap['offset'], snap.get('build_id')))

    if result['disassembly']:
        L.append('')
        L.append('--- Disassembly ---')
        L.append('  arch=%s start=%s len=%s' % (result['disassembly']['arch'],
                                                result['disassembly']['start'],
                                                result['disassembly']['length']))
        for line in result['disassembly']['lines'][:100]:
            L.append('  ' + line)
        if len(result['disassembly']['lines']) > 100:
            L.append('  ... (%d more lines)' % (len(result['disassembly']['lines']) - 100))

    L.append('')
    return '\n'.join(L)


def json_default(o):
    if isinstance(o, bytes):
        return o.decode('latin-1', 'replace')
    return str(o)


def main():
    ap = argparse.ArgumentParser(description='Reusable ELF/.so analyzer')
    ap.add_argument('input', help='Path to the .so / ELF file')
    ap.add_argument('-o', '--output', help='Write JSON report to this file (default: <input>.analysis.json)')
    ap.add_argument('--text', action='store_true', help='Also print the human-readable report')
    ap.add_argument('--disasm', action='store_true', help='Disassemble exported functions (needs capstone)')
    ap.add_argument('--func', help='Disassemble address range starting at this hex address')
    ap.add_argument('--length', type=lambda x: int(x, 0), default=0x200,
                    help='Length of --func range (default 0x200)')
    args = ap.parse_args()

    if not os.path.exists(args.input):
        sys.exit('ERROR: file not found: %s' % args.input)
    if not HAVE_ELFTOOLS:
        sys.exit('ERROR: pyelftools not installed. Run: pip install pyelftools')

    with open(args.input, 'rb') as f:
        if f.read(4) != b'\x7fELF':
            sys.exit('ERROR: %s is not an ELF file (only .so / ELF binaries are supported)' % args.input)

    result = analyze_elf(args.input, want_disasm=False)
    if args.disasm or args.func:
        if args.func:
            start = int(args.func, 16)
            with open(args.input, 'rb') as f:
                data = f.read()
                elffile = ELFFile(f)
                result['disassembly'] = disassemble_range(args.input, data, elffile, start, args.length, None)
        else:
            result['disassembly'] = 'use --func <addr> to disassemble a specific range'

    out = args.output or (args.input + '.analysis.json')
    with open(out, 'w') as f:
        json.dump(result, f, indent=2, default=json_default)
    print('JSON report written to: %s' % out)
    if args.text or not args.output:
        print()
        print(human_report(result))


if __name__ == '__main__':
    main()