import re, json, sys

p = r"C:\Users\WALTON\Downloads\dari-backup\dari\physics_work\results\batch48.json"
raw = open(p, encoding="utf-8-sig").read()
lines = raw.splitlines()

# A valid JSON string escape is one of: \" \\ \/ \b \f \n \r \t \uXXXX
bad_re = re.compile(r"\\(?![\\\"bfnrtu/])")
badlines = [i + 1 for i, l in enumerate(lines) if bad_re.search(l)]
print("lines with bad escapes:", badlines)

def fix_escapes(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            if i + 1 < len(s) and s[i + 1] in "\\\"bfnrtu/":
                out.append(s[i:i + 2])
                i += 2
                continue
            out.append("\\\\")
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)

fixed = []
for i, l in enumerate(lines):
    if bad_re.search(l):
        # only repair inside the string literal part; keys are untouched
        fixed.append(fix_escapes(l))
    else:
        fixed.append(l)
new = "\n".join(fixed)
try:
    j = json.loads(new)
    json.dump(j, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("repaired OK, entries:", len(j))
except Exception as e:
    print("STILL INVALID:", str(e)[:100])
    sys.exit(1)
