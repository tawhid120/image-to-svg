# -*- coding: utf-8 -*-
"""
inspect_target_20_questions.py
"""
import json
import os
from PIL import Image

targets = [815, 816, 817, 819, 829, 840, 846, 864, 865, 867, 868, 874, 882, 883, 884, 885, 886, 887, 892, 896]

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}

for qn in targets:
    q = q_map.get(qn)
    raw_img_path = os.path.join("downloaded_diagrams", f"q_{qn}_img_1.png")
    exists = os.path.exists(raw_img_path)
    img_size = Image.open(raw_img_path).size if exists else "NOT FOUND"
    print(f"==================== QUESTION {qn} ====================")
    print(f"Original Image: {raw_img_path} (exists={exists}, size={img_size})")
    print("STEM & SUB-QUESTIONS:")
    if q:
        print(q["q"])
        print("\nANSWER / PROOF SUMMARY:")
        print(q["a"][:300].replace("\n", " "))
    else:
        print("Question not found in processed_questions.json!")
    print("\n")
