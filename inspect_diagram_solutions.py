import json
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "downloaded_diagrams")

with open(os.path.join(HERE, "processed_questions.json"), encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}

# Find all downloaded images
imgs = glob.glob(os.path.join(IMG_DIR, "q_*_img_*.png"))
print(f"Total downloaded image files so far: {len(imgs)}")

# Group by question number
q_to_imgs = {}
for ip in imgs:
    base = os.path.basename(ip)
    # q_546_img_1.png
    parts = base.split("_")
    q_num = int(parts[1])
    q_to_imgs.setdefault(q_num, []).append(ip)

print(f"Total questions with downloaded images: {len(q_to_imgs)}")
for qn in sorted(q_to_imgs.keys()):
    q = q_map.get(qn, {})
    q_type = "MCQ" if q.get("t") == 0 else "CQ"
    print(f"--- Q{qn} ({q_type}) ---")
    print(f"Images: {len(q_to_imgs[qn])}")
    print(f"Statement: {q.get('q')}")
    if q_type == "MCQ":
        print(f"Options: {q.get('o')}")
    print(f"Answer: {q.get('a')}")
    print(f"Explanation: {q.get('e')}")
    print()
