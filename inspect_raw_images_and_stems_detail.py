# -*- coding: utf-8 -*-
"""
inspect_raw_images_and_stems_detail.py
"""
import json
import os
from PIL import Image

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}

targets = [815, 816, 817, 819, 829, 840, 846, 864, 865, 867, 868, 874, 882, 883, 884, 885, 886, 887, 892, 896]

for qn in targets:
    q = q_map.get(qn, {})
    print(f"==================================================")
    print(f"QUESTION {qn}")
    print(f"STEM: {q.get('q')}")
    print(f"ANS: {q.get('a')[:400] if q.get('a') else ''}")
    print(f"==================================================\n")
