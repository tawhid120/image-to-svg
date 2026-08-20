# -*- coding: utf-8 -*-
"""
convert_8_targets_to_svg.py
===========================
Converts ONLY the 8 requested questions (786, 794, 796, 802, 806, 840, 846, 873)
to handcrafted, high-precision SVG vectors with standard counter-clockwise orientation.
Uploads to ImageKit and updates question bank files.
"""

import json
import os
import re
import requests

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
svg_out_dir = os.path.join(HERE, "svg_diagrams")
os.makedirs(svg_out_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# 8 HANDCRAFTED TARGET SVGs
# ─────────────────────────────────────────────────────────────────────────────
TARGET_SVGS = {
    # ── Q786: Right triangle for sec^-1(x/y) -> hyp x, base y, perp sqrt(x^2-y^2) ──
    "svg_target_786.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="145" y="105" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">x</text>
  <text x="155" y="214" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#0f172a">y</text>
  <text x="290" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">√(x² - y²)</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">α</text>
</svg>""",

    # ── Q794: Right triangle 5, 12, 13 with angle phi ──
    "svg_target_794.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 260" width="100%" height="260">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,220 250,220 250,30" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="228,220 228,198 250,198" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,220 A 60,60 0 0,0 95,178" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="270" y="130" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">12</text>
  <text x="135" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">13</text>
  <text x="125" y="208" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">ϕ</text>
</svg>""",

    # ── Q796: Right triangle AB=2, BC=y=sqrt(5), AC=x ──
    "svg_target_796.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="290" y="125" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">2</text>
  <text x="160" y="214" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">y = √5</text>
  <text x="145" y="105" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#2563eb">x</text>
</svg>""",

    # ── Q802: Double right triangles (r, x) and (r, y) ──
    "svg_target_802.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="30,175 160,175 160,45" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="144,175 144,159 160,159" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 75,175 A 45,45 0 0,0 65,145" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="165" y="38" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="170" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="15" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="85" y="98" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">r</text>
  <text x="95" y="196" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">x</text>
  <polygon points="220,175 350,175 350,45" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="334,175 334,159 350,159" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 265,175 A 45,45 0 0,0 255,145" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="355" y="38" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">P</text>
  <text x="360" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">R</text>
  <text x="205" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">Q</text>
  <text x="275" y="98" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">r</text>
  <text x="365" y="115" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">y</text>
</svg>""",

    # ── Q806: Right triangle ABC with angle theta ──
    "svg_target_806.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q840: Right triangle ABC with angle theta ──
    "svg_target_840.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q846: Triangle 1 (theta) and Triangle 2 (DEF) ──
    "svg_target_846.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- Triangle 1: ABC -->
  <polygon points="30,175 160,175 160,45" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="144,175 144,159 160,159" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 75,175 A 45,45 0 0,0 65,145" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="165" y="38" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="170" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="15" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="82" y="165" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">θ</text>
  <text x="85" y="210" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">১ম চিত্র</text>
  <!-- Triangle 2: DEF -->
  <polygon points="220,175 350,175 295,45" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="295" y="35" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">F</text>
  <text x="205" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="358" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">E</text>
  <text x="285" y="210" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">২য় চিত্র</text>
</svg>""",

    # ── Q873: Right triangle ABC with angle theta ──
    "svg_target_873.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>"""
}

# 1. Save locally and Upload to ImageKit
target_uploaded_urls = {}
for fname, content in TARGET_SVGS.items():
    p = os.path.join(svg_out_dir, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

    files = {"file": (fname, content.encode("utf-8"), "image/svg+xml")}
    data = {
        "fileName": fname,
        "folder": "/math_2nd_ch7/svg/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    if res.ok:
        ik_url = res.json().get("url")
        target_uploaded_urls[fname] = ik_url
        print(f"  [TARGET SVG UPLOADED] {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] {fname}: {res.text}")

# 2. Map the 8 Target Questions to their SVG URLs
TARGET_MAP = {
    786: target_uploaded_urls["svg_target_786.svg"],
    794: target_uploaded_urls["svg_target_794.svg"],
    796: target_uploaded_urls["svg_target_796.svg"],
    802: target_uploaded_urls["svg_target_802.svg"],
    806: target_uploaded_urls["svg_target_806.svg"],
    840: target_uploaded_urls["svg_target_840.svg"],
    846: target_uploaded_urls["svg_target_846.svg"],
    873: target_uploaded_urls["svg_target_873.svg"],
}

# 3. Update Raw JSON
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for q_idx, q in enumerate(raw_data["data"]["questions"], 1):
    if q_idx in TARGET_MAP:
        svg_url = TARGET_MAP[q_idx]
        body = q.get("question", {}).get("body", {})
        for ek, ent in body.get("entityMap", {}).items():
            if ent.get("type") == "IMAGE":
                ent["data"]["src"] = svg_url

with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

# 4. Update processed_questions.json
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in TARGET_MAP:
        svg_url = TARGET_MAP[qn]
        if "![" in q["q"]:
            q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({svg_url})", q["q"])
        else:
            # If Q786 doesn't have an image tag in question, insert it after the stem
            q["q"] = f"![চিত্র]({svg_url})\n" + q["q"]

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("Successfully converted ONLY the 8 requested questions (786, 794, 796, 802, 806, 840, 846, 873) to SVG format!")
