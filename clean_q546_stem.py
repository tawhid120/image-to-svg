import json

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["n"] == 546:
        q["q"] = "$y=\\cot ^{-1} x$ এর লেখচিত্র নিচের কোনটি?"
        break

with open("processed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Q546 question stem!")
