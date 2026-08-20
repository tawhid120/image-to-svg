import json
import os

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

img_qs = []
for q in data["questions"]:
    s = json.dumps(q, ensure_ascii=False)
    if "clean_png" in s or "ik.imagekit.io" in s or "![" in s:
        img_qs.append(q)

print(f"Total questions with diagrams: {len(img_qs)}")
for q in img_qs:
    print(f"=== Q{q['n']} ===")
    print("Q:", q['q'][:140].replace("\n", " "))
    print("A:", q['a'][:140].replace("\n", " "))
    print()
