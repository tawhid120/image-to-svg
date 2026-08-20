import json, os, re, sys, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "question_bank_HSC_Admission_HSC_-_পদার্থ_বিজ্ঞান_২য়_পত্র_অধ্যায়-০২ঃ_স্থির_তড়িৎ.json")
OUTDIR = os.path.join(BASE, "downloaded_diagrams_physics")
WORKDIR = os.path.join(BASE, "physics_work")
os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(WORKDIR, exist_ok=True)

with open(SRC, encoding="utf-8") as f:
    data = json.load(f)

questions = data["data"]["questions"]
image_map = {}
req = urllib.request.Request(
    "https://firebasestorage.googleapis.com",
    headers={"User-Agent": "Mozilla/5.0"},
)

def safe_name(s):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", s)

fail = []
for q in questions:
    qid = q["id"]
    ents = []
    if "entityMap" in q.get("question_text", {}):
        for k, v in q["question_text"]["entityMap"].items():
            if v.get("type") == "IMAGE" and "src" in v.get("data", {}):
                ents.append(v["data"]["src"])
    if not ents:
        continue
    paths = []
    for i, url in enumerate(ents):
        ext = ".webp"
        m = re.search(r"\.(png|jpg|jpeg|webp|gif)(?=\?)", url)
        if m:
            ext = "." + m.group(1)
        fname = f"{safe_name(qid)}_{i}{ext}"
        fpath = os.path.join(OUTDIR, fname)
        if not os.path.exists(fpath) or os.path.getsize(fpath) == 0:
            try:
                r = urllib.request.urlopen(url, timeout=60)
                with open(fpath, "wb") as fh:
                    fh.write(r.read())
                print(f"ok {qid} -> {fname} ({os.path.getsize(fpath)} bytes)")
            except Exception as e:
                fail.append((qid, url, str(e)))
                print(f"FAIL {qid}: {e}")
        else:
            print(f"exists {fname}")
        paths.append(fname)
    image_map[qid] = paths

with open(os.path.join(WORKDIR, "image_map.json"), "w", encoding="utf-8") as f:
    json.dump(image_map, f, ensure_ascii=False, indent=2)

print(f"\nquestions with images: {len(image_map)}")
print(f"failed downloads: {len(fail)}")
for it in fail[:20]:
    print(" ", it[0], it[2][:80])