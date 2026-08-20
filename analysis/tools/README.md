# so_analyzer.py — Reusable `.so` / ELF Analysis Tool

A generic Python tool that analyzes any ELF shared object (`.so`) — typically extracted
from Android APKs — and produces:

1. A **human-readable report** (stdout / `.txt`)
2. A **machine-readable JSON report**

## Features

| Category | What it extracts |
|---|---|
| ELF identity | class (32/64-bit), endianness, OS ABI, type, machine, entry point, file size, SHA-256 |
| Segments | program headers (LOAD/DYNAMIC/RELRO/NOTE/...) with offsets, vaddrs, sizes, flags |
| Sections | names, types, addresses, offsets, sizes, flags |
| Dynamic | `DT_NEEDED` dependencies, `SONAME`, runpath, all tags |
| Symbols | exported (defined) and imported (undefined) dynamic symbols with type/bind/address/size |
| Relocations | per-section lists (RELA/REL), types, symbols, addends |
| Notes | build-id, Android ident, etc. |
| Strings | all printable ASCII strings, plus categorized finds: URLs, domains, file paths, potential secrets (api keys, tokens), Google API keys (`AIza…`), Java class names, JNI exports, embedded base64 certs |
| Flutter/Dart | AOT snapshot detection (magic `f5f5dcdc`), `_kDart*` symbols, Dart SDK build id, build feature string |
| Disassembly | any address range via `capstone` (arm64/arm/x86/x86-64, endian-aware) |

## Requirements

```bash
pip install pyelftools        # required
pip install capstone          # optional — only needed for --func/--disasm
```

Python ≥ 3.8. No binutils/readelf/objdump needed.

## Usage

```bash
# Full analysis: writes <file>.analysis.json + prints human report
python3 so_analyzer.py lib/arm64-v8a/libapp.so --text

# Custom output path
python3 so_analyzer.py libSignatureKiller.so -o out/sk.json --text

# Disassemble a specific address range (hex), e.g. a JNI function
python3 so_analyzer.py libSignatureKiller.so --func 0x1a38 --length 0x200 --text

# Help
python3 so_analyzer.py --help
```

## Output

* **JSON**: `out.json` — nested dict with keys `elf`, `sections`, `segments`, `dynamic`,
  `symbols`, `relocations`, `notes`, `strings`, `flutter`, `disassembly`.
* **Human text**: sections/symbols/dependencies/strings tables, Flutter summary,
  disassembly listing.

## Reproducing this project's analysis

```bash
# 1. Extract the APK (this analysis used an already-extracted directory)
unzip -o app.apk -d extracted/

# 2. Run the tool on every native library
find extracted/lib -name '*.so' | while read f; do
  python3 so_analyzer.py "$f" -o "out/$(basename $f).analysis.json" --text
done

# 3. Cross-check with binutils (optional)
file <so> && readelf -h -l -S -d -sW -rW <so> && strings -a <so> | grep -iE 'https?://'

# 4. Flutter-specific
strings -a libapp.so | grep -E '_kDart|product'     # snapshot markers
xxd -l 8 <so>                                        # magic f5 f5 dc dc in data blobs

# 5. Deeper (manual) analysis of a custom library
#    - identify exported JNI symbols (readelf -sW | grep Java_)
#    - disassemble them with the tool's --func, resolve ADRP targets,
#      map rodata strings to function parameters
```

## Notes / limitations

* Stripped binaries (no `.symtab`) yield only dynamic symbols; function discovery is
  then limited to exports, PLT imports, and manual disassembly.
* For Flutter `libapp.so`, the Dart string pool is still recoverable (strings); the
  AOT function names are not (no DWARF in product builds).
* `libflutter.so` JSON reports are large (506 exported symbols) — use the text report
  for a quick look.