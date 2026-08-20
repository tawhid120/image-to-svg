import json

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["n"] in [775, 779, 783, 787]:
        print(f"=== Q{q['n']} ===")
        print(q["q"])
        print("---")
