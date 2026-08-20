# -*- coding: utf-8 -*-
"""
process_and_upload_all_svgs.py
==============================
1. Generates pristine SVG vector assets for all question diagrams.
2. Uploads ONLY these clean SVG files to ImageKit under /math_2nd_ch7/.
3. Maps every question to its clean SVG URL on ImageKit.
4. Replaces URLs in the JSON question bank and rebuilds the viewer.
"""

import json
import os
import requests
import re
from create_all_svg_diagrams import SVG_DEFS

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
svg_out_dir = os.path.join(HERE, "svg_diagrams")
os.makedirs(svg_out_dir, exist_ok=True)

# 1. Write all SVG files
for filename, content in SVG_DEFS.items():
    p = os.path.join(svg_out_dir, filename)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(SVG_DEFS)} SVG files locally.")

# 2. Upload SVGs to ImageKit
svg_uploaded_urls = {}
for fname, content in SVG_DEFS.items():
    files = {"file": (fname, content.encode("utf-8"), "image/svg+xml")}
    data = {
        "fileName": fname,
        "folder": "/math_2nd_ch7/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    if res.ok:
        ik_url = res.json().get("url")
        svg_uploaded_urls[fname] = ik_url
        print(f"  [OK] Uploaded {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] Upload {fname} failed: {res.text}")

# Save mapping
with open(os.path.join(HERE, "svg_uploaded_map.json"), "w", encoding="utf-8") as f:
    json.dump(svg_uploaded_urls, f, indent=2)

# 3. Associate Questions with the correct SVGs
# Mapping question numbers to SVG filenames
QUESTION_SVG_MAP = {
    546: ["svg_q546_1.svg", "svg_q546_2.svg", "svg_q546_3.svg", "svg_q546_4.svg"],
    567: ["svg_sin_inv.svg"],
    574: ["svg_cos_inv.svg"],
    575: ["svg_cos_inv.svg"],
    582: ["svg_sin_inv.svg"],
    583: ["svg_sin_inv.svg"],
    590: ["svg_tan_inv.svg"],
    591: ["svg_tan_inv.svg"],
    622: ["svg_cos_inv.svg"],
    623: ["svg_cos_inv.svg"],
    746: ["svg_sin_inv.svg"],
    747: ["svg_cos_inv.svg"],
    756: ["svg_q775.svg"],
    775: ["svg_q775.svg"],
    786: ["svg_q794.svg"],
    794: ["svg_q794.svg"],
    796: ["svg_q796.svg"],
    802: ["svg_q802_triangles.svg"],
    806: ["svg_q806.svg"],
    811: ["svg_q811.svg"],
    815: ["svg_q815.svg"],
    816: ["svg_q816.svg"],
    817: ["svg_q817.svg"],
    819: ["svg_q819.svg"],
    829: ["svg_q806.svg"],
    840: ["svg_q806.svg"],
    846: ["svg_q894.svg"],
    855: ["svg_q796.svg"],
    863: ["svg_q863.svg"],
    864: ["svg_q806.svg"],
    865: ["svg_q865_parabola.svg"],
    867: ["svg_q865_parabola.svg"],
    868: ["svg_q868.svg"],
    872: ["svg_q872.svg"],
    873: ["svg_q872.svg"],
    874: ["svg_q817.svg"],
    882: ["svg_q802_triangles.svg"],
    883: ["svg_q865_parabola.svg"],
    884: ["svg_q865_parabola.svg"],
    885: ["svg_q865_parabola.svg"],
    886: ["svg_q806.svg"],
    887: ["svg_q887.svg"],
    892: ["svg_q872.svg"],
    894: ["svg_q894.svg"],
    896: ["svg_q872.svg"],
    901: ["svg_q901.svg"],
    902: ["svg_q902.svg"],
    938: ["svg_q802_triangles.svg"],
}

# 4. Update the raw JSON
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["data"]["questions"]
for q_idx, q in enumerate(questions, 1):
    if q_idx in QUESTION_SVG_MAP:
        target_svgs = QUESTION_SVG_MAP[q_idx]
        svg_url = svg_uploaded_urls.get(target_svgs[0])
        if svg_url:
            # Update entityMap in question statement
            body = q.get("question", {}).get("body", {})
            entity_map = body.get("entityMap", {})
            for ek, ent in entity_map.items():
                if ent.get("type") == "IMAGE":
                    ent["data"]["src"] = svg_url

            # Also update question options if applicable (e.g. Q546)
            for opt_idx, opt in enumerate(q.get("question_options", [])):
                opt_body = opt.get("body", {})
                opt_entity_map = opt_body.get("entityMap", {})
                for ek, ent in opt_entity_map.items():
                    if ent.get("type") == "IMAGE":
                        if opt_idx < len(target_svgs):
                            opt_svg_url = svg_uploaded_urls.get(target_svgs[opt_idx], svg_url)
                            ent["data"]["src"] = opt_svg_url
                        else:
                            ent["data"]["src"] = svg_url

# Save updated JSON
with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated raw JSON with SVG URLs successfully!")
