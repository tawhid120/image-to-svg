import json

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

img_map = {}
for q in data["questions"]:
    s = json.dumps(q, ensure_ascii=False)
    if "clean_png" in s or "ik.imagekit.io" in s or "![" in s:
        img_map[q["n"]] = q

print(f"Total questions with images: {len(img_map)}")
for qn in sorted(img_map.keys()):
    q = img_map[qn]
    short_q = q.get("q", "")[:100].replace("\n", " ")
    print(f"Q{qn}: {short_q}")
