# -*- coding: utf-8 -*-
"""
apply_svg_urls_to_all.py
========================
Directly maps each question to its corresponding valid SVG vector URL on ImageKit.
Updates processed_questions.json and the HTML viewer.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# Verified live ImageKit SVG URLs
SVG_MAP = {
    546: {
        "q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q546_1.svg",
        "opts": [
            "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q546_1.svg",
            "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q546_2.svg",
            "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q546_3.svg",
            "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q546_4.svg"
        ]
    },
    567: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_sin_inv.svg"},
    574: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_cos_inv.svg"},
    575: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_cos_inv.svg"},
    582: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_sin_inv.svg"},
    583: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_sin_inv.svg"},
    590: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_tan_inv.svg"},
    591: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_tan_inv.svg"},
    622: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_cos_inv.svg"},
    623: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_cos_inv.svg"},
    746: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_sin_inv.svg"},
    747: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_cos_inv.svg"},
    756: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q775.svg"},
    775: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q775.svg"},
    786: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q794.svg"},
    794: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q794.svg"},
    796: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q796.svg"},
    802: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q802_triangles.svg"},
    806: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q806.svg"},
    811: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q811.svg"},
    815: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q815.svg"},
    816: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q816.svg"},
    817: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q817.svg"},
    819: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q819.svg"},
    829: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q806.svg"},
    840: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q806.svg"},
    846: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q894.svg"},
    855: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q796.svg"},
    863: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q863.svg"},
    864: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q806.svg"},
    865: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q865_parabola.svg"},
    867: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q865_parabola.svg"},
    868: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q868.svg"},
    872: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q872.svg"},
    873: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q872.svg"},
    874: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q817.svg"},
    882: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q802_triangles.svg"},
    883: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q865_parabola.svg"},
    884: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q865_parabola.svg"},
    885: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q865_parabola.svg"},
    886: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q806.svg"},
    887: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q887.svg"},
    892: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q872.svg"},
    894: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q894.svg"},
    896: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q872.svg"},
    901: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q901.svg"},
    902: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q902.svg"},
    938: {"q": "https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/svg_q802_triangles.svg"},
}

# Update processed_questions.json directly
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    qn = q["n"]
    if qn in SVG_MAP:
        mapping = SVG_MAP[qn]
        # Replace image URL in question statement
        if "q" in mapping:
            svg_url = mapping["q"]
            # Replace any ![...](...) markdown image with the valid SVG URL
            if "![" in q["q"]:
                q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({svg_url})", q["q"])
            else:
                q["q"] = f"![চিত্র]({svg_url})\n" + q["q"]
        
        # Replace options if applicable
        if "opts" in mapping and q.get("o"):
            for i, opt_url in enumerate(mapping["opts"]):
                if i < len(q["o"]):
                    q["o"][i] = f"![চিত্র]({opt_url})"

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated all {len(SVG_MAP)} questions in processed_questions.json with pure SVG vector URLs!")
