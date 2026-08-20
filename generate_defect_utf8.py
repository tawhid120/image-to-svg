import json
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "processed_questions.json"), encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}
defect_qs = [796, 806, 811, 815, 816, 817, 819, 840, 846, 855, 863, 864, 865, 867, 868, 872, 883, 884, 887, 894, 901, 905]

out_lines = []
for qn in defect_qs:
    q = q_map.get(qn)
    img_files = glob.glob(os.path.join(HERE, "downloaded_diagrams", f"q_{qn}_img_*.png"))
    out_lines.append(f"==================== QUESTION {qn} ====================")
    out_lines.append(f"Type: {q.get('t')}")
    out_lines.append(f"Images ({len(img_files)}): {img_files}")
    out_lines.append(f"Statement:\n{q.get('q')}")
    if q.get('o'):
        out_lines.append(f"Options: {q.get('o')}")
    out_lines.append(f"Current Answer:\n{q.get('a')}")
    out_lines.append(f"Current Explanation:\n{q.get('e')}")
    out_lines.append("\n")

with open(os.path.join(HERE, "defect_details_utf8.txt"), "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(out_lines))

print("Wrote defect_details_utf8.txt")
