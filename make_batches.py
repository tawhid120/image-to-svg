import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.join(BASE, "physics_work")
BATCHDIR = os.path.join(WORKDIR, "batches")
os.makedirs(BATCHDIR, exist_ok=True)

recs = json.load(open(os.path.join(WORKDIR, "questions_info.json"), encoding="utf-8"))

BATCH = 29
batches = [recs[i:i + BATCH] for i in range(0, len(recs), BATCH)]
for idx, b in enumerate(batches, 1):
    with open(os.path.join(BATCHDIR, f"batch{idx:02d}.json"), "w", encoding="utf-8") as f:
        json.dump({"batch": idx, "questions": b}, f, ensure_ascii=False, indent=1)

print("batches:", len(batches))
for i, b in enumerate(batches, 1):
    imgs = sum(1 for r in b if r["images"])
    print(f"  batch{i:02d}: {len(b)} questions, {imgs} with images")