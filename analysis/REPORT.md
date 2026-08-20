# Native `.so` / ELF Binary Analysis Report

**Target**: Android APK contents in `/root/dari/` — a Flutter application ("Daricomma")
**Date of analysis**: 2026-08-13
**Analysis performed entirely from scratch** (no prior documentation or findings assumed)

---

## 0. Executive Summary

The analyzed artifact is an **extracted, repackaged Android APK** of a Flutter educational
app called **Daricomma** (`com.education.daricomma`). It contains four native libraries:

| Library | Purpose | Custom? |
|---|---|---|
| `lib/app.so` | Flutter **AOT-compiled Dart application code** | app code |
| `libflutter.so` | Flutter engine (v3.7.2, 2025-03-11 build) | no |
| `libSignatureKiller.so` | **MT Manager "Signature Killer" hooking library (libxhook 1.2.0)** | **yes — injected** |
| `libdatastore_shared_counter.so` | AndroidX DataStore native shared counter | no |

The APK is a **modified/repackaged build** of the original Daricomma app:

* The manifest's `application android:name` was replaced with
  `bin.mt.signature.KillerApplication` (injected by the **MT Manager** / **ApkSignatureKiller**
  tooling by L-JINBIN, `github.com/L-JINBIN/ApkSignatureKillerEx`).
* A native library `libSignatureKiller.so` (all 4 ABIs) hooks `openat64/openat/open64/open`
  in libc to **redirect APK file reads from the modified APK to the original, correctly
  signed APK** (`assets/SignatureKiller/origin.apk`).
* A `PackageInfo.CREATOR` replacement **spoofs the signature reported by the PackageManager**
  to the original signing certificate, which is embedded (base64 DER) in the injected dex
  class. The embedded certificate was verified byte-for-byte equal to the certificate in
  `origin.apk`'s `META-INF/BNDLTOOL.RSA`.

**Confirmed purpose of the modding**: defeat Daricomma's signature/anti-tamper verification so
that the repackaged (modified) APK runs while the app believes it is the original signed build.

The Flutter side (`libapp.so`) is a **product-mode AOT snapshot** (Dart SDK build id
`d91c0e6f35f0eb2e44124e8f42aa44a7`). It is stripped of all debug metadata, but the Dart
**string pool and the full source-file tree are still present** and were extracted (341
`package:daricomma/...` file paths, UI strings, API endpoints, and the app's backend domain
`daricomma.com` / `api.daricomma.com` / `daricomma.appspot.com`).

---

## 1. File Inventory & Identification

### 1.1 Native libraries found

All four ABIs were checked; only `arm64-v8a` carries all four libraries (other ABIs carry
only the injected `libSignatureKiller.so`):

```
lib/arm64-v8a/libapp.so                   9,634,720 bytes  SHA-256 5aa03c5b…b0c3b
lib/arm64-v8a/libflutter.so              11,057,504 bytes  SHA-256 6e2b75fa…63b
lib/arm64-v8a/libSignatureKiller.so         21,184 bytes  SHA-256 482f0088…b1076
lib/arm64-v8a/libdatastore_shared_counter.so 7,112 bytes  SHA-256 d3e48717…e1
lib/armeabi-v7a/libSignatureKiller.so      19,904 bytes  SHA-256 e3fd62c7…40
lib/x86/libSignatureKiller.so              18,004 bytes  SHA-256 a71bb4ba…d07
lib/x86_64/libSignatureKiller.so           23,056 bytes  SHA-256 c216091d…9ca
```

Full hashes:

```
5aa03c5b746082c7f24b0fd894ee6189f52ba22fe74d5d0f79d528ca950b0c3b  libapp.so
6e2b75facf01ae02a2d9367db197d5a61fb88df8af6233deefb9c90f059e163b  libflutter.so
482f0088d1c7cbb01f649c87c5be157a81803718febf39450698eeb668bf1076  libSignatureKiller.so (arm64)
d3e48717c9aa147e0ab21063ba0e8e0211cabf8bf40b222640829519edbf58e1  libdatastore_shared_counter.so
e3fd62c783c09408f70727ef248278174fb12f09850cd2ad60f97706f2b91740  libSignatureKiller.so (armv7)
a71bb4bae732a5904f16839e8807e89d1de6dc89e9a75dc0d568a2d893f5d07d  libSignatureKiller.so (x86)
c216091d6dd468785d33fb68a55fd3d71cce6f3ddde5b45eda999cc298707ca9  libSignatureKiller.so (x86_64)
a0e22dba564c0d8b70523d30d3be3a9775d793114704d832ad732d22db06e7a1  assets/SignatureKiller/origin.apk (original, signed APK)
```

### 1.2 Which library is "relevant" and why

* **`libapp.so`** — the Flutter application code. This is the primary subject of a
  Flutter-app binary analysis (AOT Dart code, app strings, business logic indicators).
* **`libSignatureKiller.so`** — the only *custom* native library; the most interesting
  from a reverse-engineering / tamper standpoint and the reason this APK is a repackaged build.
* `libflutter.so` / `libdatastore_shared_counter.so` — stock third-party/engine libraries;
  analyzed briefly to rule them out.

### 1.3 The embedded `origin.apk`

`assets/SignatureKiller/origin.apk` is the **original, unmodified Daricomma APK**:
* Signed with `META-INF/BNDLTOOL.RSA` (Play App Signing / bundletool), certificate DN
  `C=US, ST=California, L=Mountain View, O=Google Inc., OU=Android, CN=Android`,
  serial `B1DA745087E4335B6733F56BFF78ACB1D1CEA1E7`, SHA-256
  `80:15:B9:71:55:F4:34:39:71:3C:85:67:31:D3:04:7E:4A:DC:84:17:22:B7:3B:5D:78:12:B3:58:00:10:A9:49`
* Its manifest has `application android:name="android.app.Application"` (default), package
  `com.education.daricomma`, launcher `com.education.daricomma.MainActivity`, and carries
  Play stamp meta-data (`com.android.stamp.type=STAMP_TYPE_DISTRIBUTION_APK`,
  `com.android.vending.splits`, `requiredSplitTypes`, `base__abi,base__density`) — i.e. it was
  distributed through Google Play (fused APK / dynamic delivery).

---

## 2. ELF Analysis — `libapp.so` (Flutter AOT)

### 2.1 ELF header

```
Magic     7f 45 4c 46 | class ELF64 | little endian | SYSV ABI
Type      ET_DYN (shared object)
Machine   EM_AARCH64 (ARM AArch64)
Entry     0x0
7 program headers, 11 section headers
```

### 2.2 Program headers / segments

| Type | Offset | VirtAddr | FileSz | MemSz | Flags |
|---|---|---|---|---|---|
| PHDR | 0x40 | 0x40 | 0x188 | 0x188 | R |
| LOAD | 0x0 | 0x0 | 0x3a1e32 | 0x3a1e32 | R  (rodata/snapshot data) |
| LOAD | 0x3b0000 | 0x3b0000 | 0x5776c0 | 0x5776c0 | R E (.text — Dart AOT code) |
| LOAD | 0x930000 | 0x930000 | 0x80 | 0x80 | RW (.dynamic/.bss) |
| NOTE, DYNAMIC, GNU_STACK | | | | | |

### 2.3 Sections

```
.note.gnu.build-id  @0x1c8   Build ID: cde83d0695e94f9f8f5eb4deea2cafe8
.dynstr             @0x1e8   (133 bytes — only the 5 exported symbol names)
.dynsym             @0x270   6 entries (see below)
.hash               @0x300
.rodata             @0x340   0x3a1ab0 bytes — **Dart snapshot DATA** (heap objects + string pool)
.eh_frame           @0x3a1df0
.text               @0x3b0000 0x5776c0 bytes — **AOT-compiled Dart machine code**
.dynamic            @0x930000
.bss                @0x930060
```

**No `.symtab`, no `.debug_*`, no `.comment`, no `.init_array`, no `.data.rel.ro`.**
The library is **fully stripped**; only the five Flutter snapshot symbols are exported.

### 2.4 Dynamic linking

* **No `DT_NEEDED` dependencies at all** — libapp.so imports nothing directly. All runtime
  symbol resolution (e.g. `dart::...` calls into the engine) is performed by the Flutter
  engine (`libflutter.so`) at load time via the `_kDart*` symbols.
* No relocations (`readelf -r` → none). The snapshot is position-independent by design
  (Dart AOT snapshots are loaded with `dlopen` and self-relocate at runtime from the header).

### 2.5 Exported symbols (the complete dynamic symbol table)

```
_kDartVmSnapshotInstructions        @ 0x3b0000  size 92,688  (0x16A50)  OBJECT
_kDartIsolateSnapshotInstructions   @ 0x3c6a40  size 0x560C80 (5,639,296) OBJECT
_kDartVmSnapshotData                @ 0x340     size 16,176          OBJECT
_kDartIsolateSnapshotData           @ 0x4280    size 0x39DB70 (3,787,120) OBJECT
_kDartSnapshotBuildId               @ 0x1c8     size 32             OBJECT
```

### 2.6 Flutter snapshot structure (confirmed)

Both data blobs start with the **Dart AOT snapshot magic `f5 f5 dc dc`**, followed by a
version word, then the **Dart SDK build id** and the build feature string:

```
build id : d91c0e6f35f0eb2e44124e8f42aa44a7
features : product no-code_comments no-dwarf_stack_traces_mode dedup_instructions
           no-tsan no-msan arm64 android compressed-pointers
```

Interpretation:
* **product** — release-mode AOT snapshot, assertions off.
* **no-dwarf_stack_traces_mode** — DWARF stack traces disabled → *no* inlined debugging
  info; stack traces will be symbol-less.
* **dedup_instructions** — code deduplication applied.
* **compressed-pointers** — 64-bit compressed heap pointers (the code uses `x28` as heap
  base and compresses pointers as `(addr >> 32) | 1` tags — observed in disassembly,
  e.g. `add x2, x2, x28, lsl #32`).
* The `.text` instructions blob begins with its own length (0x16A10 = 92688, matching the
  `_kDartVmSnapshotInstructions` symbol size).

---

## 3. ELF Analysis — `libSignatureKiller.so` (the injected library)

### 3.1 ELF header

```
ELF64 little-endian, ET_DYN, EM_AARCH64, entry 0x19e4 (constructor), stripped
25 sections; 9 program headers; .note.android.ident (API level r24 → minSdk 24)
Build ID (sha1): 58bb34c20393a78f2a23ee298230047980d9b2ad
Compiler      : Android NDK r24 — "Android (8075178, based on r437112b) clang 14.0.1"
Linker        : LLD 14.0.1
```

### 3.2 Dynamic & dependencies

```
SONAME : libSignatureKiller.so
NEEDED : liblog.so, libm.so, libdl.so, libc.so
FLAGS  : BIND_NOW (full RELRO)
```

### 3.3 Exported symbols

```
Java_bin_mt_signature_KillerApplication_hookApkPath   @ 0x1a38  (232 bytes)  FUNC
xhook_register         @ 0x1c98  xhook_refresh @ 0x1ca0  xhook_ignore @ 0x1c9c
xhook_clear            @ 0x1ca4  xhook_enable_debug @ 0x1ca8
xhook_enable_sigsegv_protection @ 0x1cac
```

The `xhook_*` exports are the public API of the well-known open-source library
**libxhook** (`github.com/iqiyi/xHook`) — a PLT/GOT hooking engine. Its version string
`libxhook 1.2.0 (aarch64)` is embedded in `.rodata`, together with its internal debug
strings (`hooking %s in %s`, `XH_HK_OK %p: %p -> %p`, `/proc/self/maps` parsing format
`%lx-%lx %4s ...`, `.*\.so$`, `openat`/`open64` handling, SIGSEGV catcher strings).

### 3.4 Imported functions (what the hook engine needs)

```
strcmp, __android_log_print, regcomp/regexec/regfree (regex for .so matching),
malloc/free/strdup/strcpy/strlen/strstr/sscanf, fopen/fgets/fclose,
pthread_mutex_lock/unlock, pthread_create/join/self/setname_np, pthread_cond_*,
sigemptyset/sigaction/sigsetjmp/siglongjmp (SIGSEGV protection), mprotect, __errno
```

### 3.5 Relocations

* `.rela.dyn`: 6 `R_AARCH64_RELATIVE` (fini_array → 0x19fc/0x19e4, data pointers).
* `.rela.plt`: 33 `R_AARCH64_JUMP_SLOT` (all libc/liblog imports + 2 to local `xhook_*`).

---

## 4. Disassembly / Function Analysis

### 4.1 `Java_bin_mt_signature_KillerApplication_hookApkPath` @ 0x1a38

Signature (from the dex side): `private static native void hookApkPath(String oldApkPath,
String newApkPath)`.

```
0x1a38  stp  x29,x30,[sp,#-0x20]!      ; prologue
0x1a44  ldr  x8,[x0]                   ; JNIEnv* -> function table
0x1a54  ldr  x8,[x8,#0x548]            ; slot 169 = GetStringUTFChars
0x1a5c  blr  x8                        ; env->GetStringUTFChars(env, arg1(x2), NULL)
0x1a64  str  x0,[0x6ae8]               ; -> global g_old_path (in .bss)
        ; (repeat for arg2(x3))        ; -> global g_new_path @ 0x6af0
0x1a88  mov  x0, ".*\.so$" (rodata)
        ; then 4 x xhook_register calls:
        ;   xhook_register(".*\.so$", "openat64", hook_openat64, &0x6af8)
        ;   xhook_register(".*\.so$", "openat",   hook_openat,   &0x6b00)
        ;   xhook_register(".*\.so$", "open64",   hook_open64,   &0x6b08)
        ;   xhook_register(".*\.so$", "open",     hook_open,     &0x6b10)
0x1b14  mov  w0,#0                     ; return 0
0x1b1c  b    xhook_refresh             ; apply the hooks
```

### 4.2 The four open-hooks (e.g. `openat64` hook @ 0x1b20)

```
0x1b30  ldr  x1, [0x6ae8]        ; g_old_path
0x1b40  mov  x0, x21             ; path argument
0x1b4c  bl   strstr              ; strstr(path, g_old_path)
0x1b60  ldr  x4, [0x6af8]        ; saved original openat64
0x1b64  csel x1, x9, x21, eq     ; if match -> path := g_new_path
0x1b80  br   x4                  ; call real openat64(dirfd, path', flags, mode)
```

**Behavior**: any `open*` call whose path *contains* the first JNI argument is transparently
redirected to the second argument. Called from Java as
`hookApkPath(modifiedApkPath, dataDir/origin.apk)` — so when the app opens its own APK
(the modified `base.apk`) to verify its signature, it is redirected to the **original,
correctly signed** APK. **Confirmed by reading both the native code and the caller.**

### 4.3 Constructor / entry @ 0x19e4

Calls `xhook_refresh`-related initialization with `__cxa_atexit`-registered destructor
(0x19fc → 0x19f4); `fini_array` contains 0x19fc and 0x19e4. Also a small helper at 0x1a18
that invokes the refresh thread.

### 4.4 `libapp.so` `.text` — Dart AOT machine code

The 5.7 MB `.text` is AOT-compiled Dart. Characteristics observed in disassembly:
object field copying/initialization sequences, compressed-pointer arithmetic via `x28`,
no symbol table, no function names. Individual Dart functions cannot be named, but the
code is functional and analyzable at the instruction level (sample dump in
`disassembly/libapp.text.sample.disasm.txt`). **Limitation**: mapping instructions back to
named Dart functions requires the DWARF data that was stripped (`no-dwarf_stack_traces_mode`).

---

## 5. String / Constant Analysis (libapp.so)

23,911 printable strings extracted (`analysis/strings/libapp.all_strings.txt`).

### 5.1 The app's own endpoints (confirmed, in binary)

| String | Meaning |
|---|---|
| `https://daricomma.com/api` @0x7474f | **API base URL** |
| `https://api.daricomma.com` (in `Enter full url. Ex: https://api.daricomma.com`) | alternative/current API host (debug URL-input screen) |
| `https://www.daricomma.com` @0xe2f94 | public website |
| `daricomma.appspot.com` | legacy Google App Engine backend host |
| `aamarpay` | **Aamarpay** Bangladeshi payment gateway |
| `/v1/self-test/...`, `/v1/users-subscription/...`, `/v2/question`, `/v2/payment`, `/v2/package`, `/v2/bookshelf`, `/v2/referral`, `/v2/question/admission`, `/v2/payment/wallet`, `/v1/self-test/{start-exam,submit-exam,result,answer,all-self-test-exam}` | REST API paths |
| `/payment/:payment_url/:payment_source` | in-app route for payment URLs |

### 5.2 Developer/build-machine leak (confirmed)

```
file:///Users/yeamin/Documents/Daricomma/daricomma-app/.dart_tool/flutter_build/dart_plugin_registrant.dart
```
Reveals: developer username **`yeamin`**, project directory **`Daricomma/daricomma-app`**,
macOS build host, plus the full source tree (below).

### 5.3 Recovered Dart source tree (confirmed)

341 `package:daricomma/...` file paths were recovered, including:

```
core/networking/dio_client.dart            core/networking/interceptor/auth_interceptor.dart
core/networking/session_manager.dart       core/storage/secure_storage.dart
core/remote_config/remote_config_service.dart  core/routes/router.dart
feature/auth/...  (bloc, otp, password, register, sign_in/sign_up)
feature/exam/...  (self-test exams, results, answer sheets)
feature/show_question/...  (question bank, filters: chapter/topic/year/level/rating/source)
feature/show_subject/...   (class/group/version/curriculum)
feature/package, feature/payment, feature/checkout (coupon, stepper)
feature/my_subscription/... (student/teacher/free/online-exam/create-question subscriptions,
                             transaction history, wallet)
feature/bookshelf, feature/draft, feature/faq, feature/teachers_corner,
feature/webview, feature/onboarding, feature/splash, feature/profile, feature/my_dashboard
```

Third-party packages (from `package:` prefixes): `flutter_math_fork` (KaTeX math),
`youtube_player_iframe`, `go_router`, `dio`, `http`, `bloc`, `rxdart`, `sqflite`,
`webview_flutter`, `firebase_*`, `flutter_secure_storage`, `in_app_update` (channel
`de.ffuf.in_app_update` — a package by ffuf GmbH, not a network domain), `recaptcha_enterprise_flutter`,
`flutter_cache_manager`, `uuid`, `crypto`, `logger`, etc.

### 5.4 Interesting app strings

```
access_token / readTokenFromStorage / writeAccessToken / setToken  (auth token handling)
"Your new password set successfully."   /auth/forget-password   /auth/reset-password
"HTTP connection timed out after ..."   (dio error messages)
Enter full url. Ex: https://daricomma.com   (debug screen)
```

### 5.5 Secrets check

No valid-looking API keys found: **no `AIza...` Google API keys, no private keys, no
tokens** in libapp.so. The only embedded credential-like value is the **original app
signing certificate** in `classes3.dex` (see §6). The certificate is embedded application
data; treat as such — it is the *original* app's certificate and is used for spoofing.

---

## 6. The Signature-Killer Mechanism (behavioral analysis)

All confirmed from `classes3.dex` bytecode (`bin.mt.signature.KillerApplication` and inner
class `KillerApplication$1`) plus the native hooks:

**Startup (`<clinit>`, runs because the manifest points `android:name` to it):**

1. `killPM("com.education.daricomma", "<base64 original cert>")`:
   * builds a `Signature` from the embedded base64 **original signing certificate**
   * replaces `PackageInfo.CREATOR` with a custom `Parcelable.Creator` whose
     `createFromParcel` overwrites `PackageInfo.signatures[0]` — and on API ≥ 28
     `SigningInfo.getApkContentsSigners()[0]` — with the original signature whenever the
     parceled `packageName` equals `com.education.daricomma`
   * API ≥ 28: uses **LSPosed `HiddenApiBypass.addHiddenApiExemptions`** for hidden APIs
   * clears `PackageManager.sPackageInfoCache`, `Parcel.mCreators`, `Parcel.sPairedCreators`
2. `killOpen("com.education.daricomma")`:
   * `System.loadLibrary("SignatureKiller")`
   * finds the *modified* APK path by scanning `/proc/self/maps` and validating it with
     `isApkPath` (recognizes `/data/app/.../base.apk`, `/mnt/expand/...`, `/mnt/asec/.../pkg.apk`)
   * extracts `assets/SignatureKiller/origin.apk` (if not already present) to
     `/data/data/com.education.daricomma/origin.apk` (or `/data/user/0/...`)
   * calls native `hookApkPath(modifiedApkPath, originApkPath)` → the xhook `open*` hooks
     redirect any open of the *modified* APK to the *original* APK

**Net effect** (confirmed by the code paths):
* `PackageManager.getPackageInfo(...).signatures` reports the **original** certificate.
* Any file-based signature verification that opens the app's APK reads the **original**
  APK contents.
* Therefore the modified APK passes signature checks that would otherwise reject it.

**Obfuscation/protection of the mod**: the killer itself is *not* obfuscated; it relies on
being an established tool (MT Manager / ApkSignatureKiller). `libapp.so` is stripped but
not packed/encrypted (Dart AOT needs raw code). No packing detected in any library.

---

## 7. Flutter-Specific Findings & Limitations (libapp.so)

* **What it is**: a product-mode, `compressed-pointers`, AArch64 AOT snapshot; Dart VM
  runtime lives in `libflutter.so` (engine **3.7.2 (stable)**, built 2025-03-11), which
  loads the `_kDart*` blobs.
* **What can be extracted**: the complete string pool (UI texts, URLs, API paths), the
  source file tree, library/package usage, object model hints (class names like
  `_HttpClient@16463476`, library suffixes), and raw machine code.
* **What cannot be recovered**: original Dart source text, function names/parameters for
  individual AOT functions (no DWARF, `no-dwarf_stack_traces_mode`), and high-level
  control-flow structure. Reconstructing semantics is only possible through manual
  disassembly of the (large) `.text` section.
* **No obfuscation** (`--obfuscate` not detected: no `_OBFUSCATED` markers; symbol names
  like `_HttpClient@16463476` show the normal non-obfuscated private-name mangling).

---

## 8. Confirmed vs. Hypothesized

**Confirmed (binary-level evidence):**
1. APK is repackaged: manifest `android:name="bin.mt.signature.KillerApplication"`,
   injected dex class, injected native lib, embedded origin.apk.
2. `libSignatureKiller.so` = libxhook 1.2.0 + one JNI entry that hooks `openat64/openat/
   open64/open` and redirects the modified APK path to `origin.apk`.
3. The embedded base64 certificate is byte-identical to `origin.apk`'s BNDLTOOL.RSA cert.
4. `libapp.so` is a product-mode Flutter AOT snapshot (magic, symbols, build id, features),
   engine 3.7.2, containing 341 `package:daricomma` files, `https://daricomma.com/api` etc.
5. `libdatastore_shared_counter.so` is stock AndroidX DataStore (`NativeSharedCounter`).

**Strong indications:**
* The modder used MT Manager / L-JINBIN ApkSignatureKillerEx tooling (code matches the
  public project; the GitHub URL is embedded in the dex).
* The app's backend is hosted on `daricomma.com` with a legacy `appspot.com` host.

**Speculative / not determined:**
* *Why* the app was modified (e.g. free-subscription unlocking, content extraction,
  ad-removal) — no evidence in the binary about the actual modification payload; the
  Flutter code is unmodified (same AOT snapshot, single `package:` set).
* Whether the embedded certificate corresponds to the currently shipped Play Store key.

---

## 9. Deliverables (files produced)

```
/root/dari/analysis/
├── REPORT.md                          (this report)
├── tools/
│   ├── so_analyzer.py                 (reusable analyzer: ELF+symbols+strings+JSON)
│   └── README.md                      (tool usage & reproduction guide)
├── outputs/                           (JSON + human-readable reports per .so)
│   ├── libapp.analysis.json/.txt
│   ├── libSignatureKiller.arm64-v8a.json / .armeabi-v7a / .x86 / .x86_64
│   ├── libflutter.analysis.json/.txt
│   ├── libdatastore_shared_counter.analysis.json/.txt
│   └── libSignatureKiller.*.txt (human-readable reports)
├── strings/
│   ├── libapp.all_strings.txt         (23,911 strings)
│   ├── libapp.dart_source_tree.txt    (341 recovered dart file paths)
│   ├── libapp.domains.txt
│   └── dex_classes.txt                (6,143 dex classes from the APK)
└── disassembly/
    ├── libSignatureKiller.text.disasm.txt   (full 2,805-line .text disasm, aarch64)
    └── libapp.text.sample.disasm.txt        (1,026-line sample of Dart AOT code)
```

## 10. Conclusion

* The subject `.so` files belong to **`com.education.daricomma`**, a Flutter education app
  for the Bangladeshi market (exams, question banks, subscriptions, Aamarpay payments).
* `libapp.so` is the app's AOT-compiled Dart code; its structure, SDK, endpoints, and
  entire Dart file tree were successfully extracted.
* `libSignatureKiller.so` is a tamper tool: it is the MT Manager signature-killer that
  makes the **repackaged APK pass the original app's signature verification** by hooking
  libc `open*` and spoofing `PackageInfo` signatures with the original certificate and APK.
* What could not be determined: the actual gameplay/content modification performed by the
  repackager, and the names of individual AOT functions (stripped, no DWARF).