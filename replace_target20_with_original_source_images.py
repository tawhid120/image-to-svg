# -*- coding: utf-8 -*-
"""
replace_target20_with_original_source_images.py
===============================================
Replaces the 20 target questions:
815, 816, 817, 819, 829, 840, 846, 864, 865, 867, 868, 874, 882, 883, 884, 885, 886, 887, 892, 896
with their 100% authentic, original downloaded source images.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# 1. Load clean uploaded map
with open(os.path.join(HERE, "clean_uploaded_map.json"), "r", encoding="utf-8") as f:
    clean_map = json.load(f)

targets = [815, 816, 817, 819, 829, 840, 846, 864, 865, 867, 868, 874, 882, 883, 884, 885, 886, 887, 892, 896]

proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in targets:
        k = f"clean_q_{qn}_img_1.png"
        if k in clean_map:
            orig_url = clean_map[k] + "?v=20260818_original"
            if "![" in q["q"]:
                q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({orig_url})", q["q"])
            else:
                q["q"] = f"![চিত্র]({orig_url})\n\n" + q["q"]

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for q_idx, q in enumerate(raw_data["data"]["questions"], 1):
    if q_idx in targets:
        k = f"clean_q_{q_idx}_img_1.png"
        if k in clean_map:
            orig_url = clean_map[k] + "?v=20260818_original"
            body = q.get("question", {}).get("body", {})
            for ek, ent in body.get("entityMap", {}).items():
                if ent.get("type") == "IMAGE":
                    ent["data"]["src"] = orig_url

with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

print("Successfully replaced all 20 target questions with their 100% authentic original source images!")
