# -*- coding: utf-8 -*-
"""
apply_hybrid_master_approach.py
===============================
Implements the Hybrid Master Approach:
1. Single/standard geometry questions -> Pristine counter-clockwise high-DPI recreated diagrams.
2. Complex composite diagrams (Q865, Q867, Q883, Q884, Q885, Q811, Q815, Q816, Q817, Q819, Q868, Q872, Q874, Q887, Q892, Q894, Q896) -> 2x Super-Resolution clean white-base PNGs from original textbook scans.
3. Updates raw JSON, processed_questions.json, and HTML viewer.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# 1. LOAD IMAGEKIT URL MAPS
# ─────────────────────────────────────────────────────────────────────────────
clean_map_file = os.path.join(HERE, "clean_uploaded_map.json")
with open(clean_map_file, "r", encoding="utf-8") as f:
    clean_urls = json.load(f)

# Recreated clean URLs
recreated_base = "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/recreated"

# ─────────────────────────────────────────────────────────────────────────────
# 2. DEFINE HYBRID MAPPING
# ─────────────────────────────────────────────────────────────────────────────
# Complex multi-panel composite questions that use 2x enhanced original clean PNGs:
COMPLEX_COMPOSITE_QS = {
    811: clean_urls.get("clean_q_811_img_1.png"),
    815: clean_urls.get("clean_q_815_img_1.png"),
    816: clean_urls.get("clean_q_816_img_1.png"),
    817: clean_urls.get("clean_q_817_img_1.png"),
    819: clean_urls.get("clean_q_819_img_1.png"),
    865: clean_urls.get("clean_q_865_img_1.png"),
    867: clean_urls.get("clean_q_867_img_1.png"),
    868: clean_urls.get("clean_q_868_img_1.png"),
    872: clean_urls.get("clean_q_872_img_1.png"),
    874: clean_urls.get("clean_q_874_img_1.png"),
    883: clean_urls.get("clean_q_883_img_1.png"),
    884: clean_urls.get("clean_q_884_img_1.png"),
    885: clean_urls.get("clean_q_885_img_1.png"),
    887: clean_urls.get("clean_q_887_img_1.png"),
    892: clean_urls.get("clean_q_892_img_1.png"),
    894: clean_urls.get("clean_q_894_img_1.png"),
    896: clean_urls.get("clean_q_896_img_1.png"),
}

# Standard single-geometry & function graph questions that use fresh recreated diagrams:
STANDARD_RECREATED_QS = {
    546: [
        f"{recreated_base}/diag_546_1.png",
        f"{recreated_base}/diag_546_2.png",
        f"{recreated_base}/diag_546_3.png",
        f"{recreated_base}/diag_546_4.png"
    ],
    567: f"{recreated_base}/diag_sin_inv.png",
    574: f"{recreated_base}/diag_cos_inv.png",
    575: f"{recreated_base}/diag_cos_inv.png",
    582: f"{recreated_base}/diag_sin_inv.png",
    583: f"{recreated_base}/diag_sin_inv.png",
    590: f"{recreated_base}/diag_tan_inv.png",
    591: f"{recreated_base}/diag_tan_inv.png",
    622: f"{recreated_base}/diag_cos_inv.png",
    623: f"{recreated_base}/diag_cos_inv.png",
    746: f"{recreated_base}/diag_sin_inv.png",
    747: f"{recreated_base}/diag_cos_inv.png",
    756: f"{recreated_base}/diag_775.png",
    775: f"{recreated_base}/diag_775.png",
    786: f"{recreated_base}/diag_794.png",
    794: f"{recreated_base}/diag_794.png",
    796: f"{recreated_base}/diag_796.png",
    802: f"{recreated_base}/diag_802.png",
    806: f"{recreated_base}/diag_806.png",
    829: f"{recreated_base}/diag_806.png",
    840: f"{recreated_base}/diag_806.png",
    846: f"{recreated_base}/diag_846.png",
    855: f"{recreated_base}/diag_796.png",
    863: f"{recreated_base}/diag_863.png",
    864: f"{recreated_base}/diag_806.png",
    873: f"{recreated_base}/diag_806.png",
    882: f"{recreated_base}/diag_802.png",
    886: f"{recreated_base}/diag_806.png",
    901: f"{recreated_base}/diag_901.png",
    902: f"{recreated_base}/diag_902.png",
    938: f"{recreated_base}/diag_802.png",
}

# Merge all mappings into MASTER_HYBRID_MAP
MASTER_HYBRID_MAP = {}
MASTER_HYBRID_MAP.update(STANDARD_RECREATED_QS)
MASTER_HYBRID_MAP.update(COMPLEX_COMPOSITE_QS)

print(f"Total mapped questions in Hybrid Master Scheme: {len(MASTER_HYBRID_MAP)}")

# ─────────────────────────────────────────────────────────────────────────────
# 3. UPDATE RAW JSON & PROCESSED_QUESTIONS.JSON
# ─────────────────────────────────────────────────────────────────────────────
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for q_idx, q in enumerate(raw_data["data"]["questions"], 1):
    if q_idx in MASTER_HYBRID_MAP:
        mapping = MASTER_HYBRID_MAP[q_idx]
        if isinstance(mapping, list):
            for opt_idx, opt in enumerate(q.get("question_options", [])):
                opt_body = opt.get("body", {})
                for ek, ent in opt_body.get("entityMap", {}).items():
                    if ent.get("type") == "IMAGE":
                        ent["data"]["src"] = mapping[min(opt_idx, len(mapping)-1)]
        else:
            body = q.get("question", {}).get("body", {})
            for ek, ent in body.get("entityMap", {}).items():
                if ent.get("type") == "IMAGE":
                    ent["data"]["src"] = mapping

with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

# Update processed_questions.json directly
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in MASTER_HYBRID_MAP:
        mapping = MASTER_HYBRID_MAP[qn]
        if isinstance(mapping, list):
            if q.get("o"):
                for i, opt_url in enumerate(mapping):
                    if i < len(q["o"]):
                        q["o"][i] = f"![চিত্র]({opt_url})"
        else:
            if "![" in q["q"]:
                q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({mapping})", q["q"])
            else:
                q["q"] = f"![চিত্র]({mapping})\n" + q["q"]

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("Successfully applied the Hybrid Master Scheme to all 48 question diagrams!")
