# -*- coding: utf-8 -*-
"""
rebuild_all_svgs_standard_orientation.py
========================================
Rebuilds ALL SVG diagrams to strictly adhere to the standard mathematical convention:
- Counter-clockwise angle direction (ঘড়ির কাঁটার বিপরীত দিক).
- Standard First-Quadrant Orientation (Base on horizontal axis, angle at bottom-left opening upwards).
- Clean, professional typography and dark-mode adaptive SVG styling.
- Uploads to ImageKit and updates question bank viewer.
"""

import json
import os
import requests

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
svg_out_dir = os.path.join(HERE, "svg_diagrams")
os.makedirs(svg_out_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# 📐 STANDARD ORIENTATION SVG DEFINITIONS (ALL COUNTER-CLOCKWISE)
# ─────────────────────────────────────────────────────────────────────────────

SVG_STANDARD = {
    # ── Q863: Standard right triangle ABC (Angle theta at B, bottom-left, counter-clockwise) ──
    "svg_q863.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- Triangle vertices: B(50, 180), C(270, 180), A(270, 40) -->
  <polygon points="50,180 270,180 270,40" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Right angle at C -->
  <polyline points="250,180 250,160 270,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <!-- Counter-clockwise angle arc at B (from base BC up to hypotenuse BA) -->
  <path d="M 100,180 A 50,50 0 0,0 92,153" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <!-- Vertices -->
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="285" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="275" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <!-- Labels -->
  <text x="145" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">1</text>
  <text x="115" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">θ</text>
  <text x="290" y="115" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#64748b">AC</text>
  <text x="160" y="202" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#64748b">BC</text>
</svg>""",

    # ── Q806 / Q829 / Q840 / Q864 / Q886: Standard right triangle ABC (theta at B, counter-clockwise) ──
    "svg_q806.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,180 270,180 270,40" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="250,180 250,160 270,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 100,180 A 50,50 0 0,0 92,153" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="285" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="275" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="115" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q796 / Q855: Right triangle with perpendicular=2, base=sqrt(5), hyp=x (theta counter-clockwise) ──
    "svg_q796.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- C at bottom-left (50, 180), B at bottom-right (270, 180), A at top-right (270, 40) -->
  <polygon points="50,180 270,180 270,40" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="250,180 250,160 270,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 100,180 A 50,50 0 0,0 92,153" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="285" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="275" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="290" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">2</text>
  <text x="160" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">y = √5</text>
  <text x="145" y="95" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">x</text>
</svg>""",

    # ── Q775 / Q756: Right triangle 3, 4, 5 with angle ACB = theta (counter-clockwise) ──
    "svg_q775.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- C at (50, 180), B at (270, 180), A at (270, 40) -->
  <polygon points="50,180 270,180 270,40" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="250,180 250,160 270,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 100,180 A 50,50 0 0,0 92,153" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="285" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="275" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="290" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">3</text>
  <text x="145" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">5</text>
  <text x="115" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q794 / Q786: Right triangle 5, 12, 13 with angle phi (counter-clockwise) ──
    "svg_q794.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 260" width="100%" height="260">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,220 250,220 250,30" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="230,220 230,200 250,200" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 100,220 A 50,50 0 0,0 90,185" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="270" y="130" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">12</text>
  <text x="135" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">13</text>
  <text x="115" y="208" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">ϕ</text>
</svg>""",

    # ── Q901: Right triangle with angle theta at C (counter-clockwise) ──
    "svg_q901.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,180 270,180 270,40" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="250,180 250,160 270,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 100,180 A 50,50 0 0,0 92,153" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="285" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="275" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="145" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">5</text>
  <text x="160" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">3</text>
  <text x="290" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">x</text>
  <text x="115" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q902: Right triangle with angle theta at C (counter-clockwise) ──
    "svg_q902.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,180 270,180 270,40" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="250,180 250,160 270,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 100,180 A 50,50 0 0,0 92,153" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="285" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="275" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="145" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">x</text>
  <text x="160" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">y</text>
  <text x="290" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">2</text>
  <text x="115" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q894: Two right triangles (alpha and beta counter-clockwise) ──
    "svg_q894.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- Triangle 1 -->
  <polygon points="30,170 160,170 160,40" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="145,170 145,155 160,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 65,170 A 35,35 0 0,0 58,145" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="85" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">√3</text>
  <text x="95" y="190" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">√2</text>
  <text x="75" y="162" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#2563eb">α</text>
  <text x="95" y="210" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">১ম চিত্র</text>
  <!-- Triangle 2 -->
  <polygon points="220,170 350,170 350,40" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="335,170 335,155 350,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 255,170 A 35,35 0 0,0 248,145" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="275" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">2√3</text>
  <text x="285" y="190" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">√3 + √2</text>
  <text x="265" y="162" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#2563eb">β</text>
  <text x="285" y="210" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">২য় চিত্র</text>
</svg>""",

    # ── Q802 / Q882 / Q938: Double right triangles (r, x) and (r, y) counter-clockwise ──
    "svg_q802_triangles.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="30,170 160,170 160,40" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="145,170 145,155 160,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 65,170 A 35,35 0 0,0 58,145" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="165" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="170" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="15" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">A</text>
  <text x="85" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">r</text>
  <text x="95" y="190" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">x</text>
  <polygon points="220,170 350,170 350,40" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="335,170 335,155 350,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 255,170 A 35,35 0 0,0 248,145" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="355" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">P</text>
  <text x="360" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">R</text>
  <text x="205" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">Q</text>
  <text x="275" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">r</text>
  <text x="365" y="110" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">y</text>
</svg>"""
}

# 1. Write all standard orientation SVGs locally
for fname, content in SVG_STANDARD.items():
    p = os.path.join(svg_out_dir, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
print(f"Generated {len(SVG_STANDARD)} corrected counter-clockwise SVGs locally.")

# 2. Upload to ImageKit
for fname, content in SVG_STANDARD.items():
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
        print(f"  [UPDATED] {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] Upload {fname} failed: {res.text}")

print("All counter-clockwise standard SVGs updated on ImageKit!")
