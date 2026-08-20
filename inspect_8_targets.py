import json

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

targets = [786, 794, 796, 802, 806, 840, 846, 873]
for q in data["questions"]:
    if q["n"] in targets:
        print(f"=== Q{q['n']} ===")
        print("Question:", q["q"])
        print("---")
