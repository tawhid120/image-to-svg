import json
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "processed_questions.json"), encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}
defect_qs = [796, 806, 811, 815, 816, 817, 819, 840, 846, 855, 863, 864, 865, 867, 868, 872, 883, 884, 887, 894, 901, 905]

for qn in defect_qs:
    q = q_map.get(qn)
    img_files = glob.glob(os.path.join(HERE, "downloaded_diagrams", f"q_{qn}_img_*.png"))
    print(f"==================== QUESTION {qn} ====================")
    print(f"Type: {q.get('t')}")
    print(f"Images ({len(img_files)}): {img_files}")
    print(f"Statement:\n{q.get('q')}")
    if q.get('o'):
        print(f"Options: {q.get('o')}")
    print(f"Current Answer:\n{q.get('a')}")
    print(f"Current Explanation:\n{q.get('e')}")
    print()
