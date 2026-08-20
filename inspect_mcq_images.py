import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "processed_questions.json"), encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}
mcq_img_qs = [546, 567, 574, 575, 582, 583, 590, 591, 622, 623, 746, 747, 756, 775, 786, 794]

for qn in mcq_img_qs:
    q = q_map.get(qn)
    print(f"==================== MCQ Q{qn} ====================")
    print(f"Statement: {q.get('q')}")
    print(f"Options: {q.get('o')}")
    print(f"Answer: {q.get('a')}")
    print(f"Explanation: {q.get('e')[:200]}")
    print()
