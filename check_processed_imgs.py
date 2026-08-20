import json
import re

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if "img" in json.dumps(q, ensure_ascii=False) or "![" in json.dumps(q, ensure_ascii=False):
        print(f"=== Q{q['n']} ===")
        print("Question text:", q["q"])
        print("Options:", q["o"])
        print()
