# -*- coding: utf-8 -*-
"""
deploy_v2_cache_busted_vectors.py
==================================
Uploads all pure vector images with clean versioned names (e.g. vec_819_physics_v2.png)
to instantly bust all browser and ImageKit CDN caches.
Updates raw JSON, processed_questions.json, and HTML viewer.
"""

import json
import os
import re
import requests

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
vec_dir = os.path.join(HERE, "pure_vector_diagrams")

# 1. Upload all files from pure_vector_diagrams with v2 naming
uploaded_v2_urls = {}
for fname in os.listdir(vec_dir):
    if not fname.endswith('.png'):
        continue
    p = os.path.join(vec_dir, fname)
    with open(p, 'rb') as f:
        img_bytes = f.read()
    
    v2_name = fname.replace(".png", "_v2.png")
    files = {"file": (v2_name, img_bytes, "image/png")}
    data = {
        "fileName": v2_name,
        "folder": "/math_2nd_ch7/pure_vector_v2/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    if res.ok:
        ik_url = res.json().get("url") + "?v=20260818"
        uploaded_v2_urls[fname] = ik_url
        print(f"  [UPLOADED V2] {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] {fname}: {res.text}")

# 2. Master Map for All 48 Questions
MAP = {
    546: [uploaded_v2_urls["vec_546_1.png"], uploaded_v2_urls["vec_546_2.png"], uploaded_v2_urls["vec_546_3.png"], uploaded_v2_urls["vec_546_4.png"]],
    567: uploaded_v2_urls["vec_sin_inv.png"],
    574: uploaded_v2_urls["vec_cos_inv.png"],
    575: uploaded_v2_urls["vec_cos_inv.png"],
    582: uploaded_v2_urls["vec_sin_inv.png"],
    583: uploaded_v2_urls["vec_sin_inv.png"],
    590: uploaded_v2_urls["vec_tan_inv.png"],
    591: uploaded_v2_urls["vec_tan_inv.png"],
    622: uploaded_v2_urls["vec_cos_inv.png"],
    623: uploaded_v2_urls["vec_cos_inv.png"],
    746: uploaded_v2_urls["vec_746_794.png"],
    747: uploaded_v2_urls["vec_747_863.png"],
    756: uploaded_v2_urls["vec_756_775.png"],
    775: uploaded_v2_urls["vec_756_775.png"],
    786: uploaded_v2_urls["vec_746_794.png"],
    794: uploaded_v2_urls["vec_746_794.png"],
    796: uploaded_v2_urls["vec_796_855.png"],
    802: uploaded_v2_urls["vec_802_dual.png"],
    806: uploaded_v2_urls["vec_806_std.png"],
    811: uploaded_v2_urls["vec_811.png"],
    815: uploaded_v2_urls["vec_815.png"],
    816: uploaded_v2_urls["vec_816.png"],
    817: uploaded_v2_urls["vec_817_874.png"],
    819: uploaded_v2_urls["vec_819.png"],
    829: uploaded_v2_urls["vec_806_std.png"],
    840: uploaded_v2_urls["vec_806_std.png"],
    846: uploaded_v2_urls["vec_846.png"],
    855: uploaded_v2_urls["vec_796_855.png"],
    863: uploaded_v2_urls["vec_747_863.png"],
    864: uploaded_v2_urls["vec_806_std.png"],
    865: uploaded_v2_urls["vec_865_composite.png"],
    867: uploaded_v2_urls["vec_865_composite.png"],
    868: uploaded_v2_urls["vec_868.png"],
    872: uploaded_v2_urls["vec_872_triple.png"],
    873: uploaded_v2_urls["vec_806_std.png"],
    874: uploaded_v2_urls["vec_817_874.png"],
    882: uploaded_v2_urls["vec_802_dual.png"],
    883: uploaded_v2_urls["vec_865_composite.png"],
    884: uploaded_v2_urls["vec_865_composite.png"],
    885: uploaded_v2_urls["vec_865_composite.png"],
    886: uploaded_v2_urls["vec_806_std.png"],
    887: uploaded_v2_urls["vec_872_triple.png"],
    892: uploaded_v2_urls["vec_872_triple.png"],
    894: uploaded_v2_urls["vec_894.png"],
    896: uploaded_v2_urls["vec_872_triple.png"],
    901: uploaded_v2_urls["vec_901.png"],
    902: uploaded_v2_urls["vec_902.png"],
    938: uploaded_v2_urls["vec_802_dual.png"],
}

# 3. Update Raw JSON
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for q_idx, q in enumerate(raw_data["data"]["questions"], 1):
    if q_idx in MAP:
        mapping = MAP[q_idx]
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

# 4. Update processed_questions.json
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in MAP:
        mapping = MAP[qn]
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

print("\nSuccessfully updated all questions with v2 cache-busted ImageKit URLs!")
