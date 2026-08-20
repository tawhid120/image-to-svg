# -*- coding: utf-8 -*-
"""
cleanup_and_deploy_v2_svgs.py
=============================
1. Deletes all old cached files from ImageKit.
2. Generates geometrically pristine V2 SVGs with:
   - Angle vertex on the BOTTOM-LEFT.
   - Base on the horizontal line.
   - Right angle at BOTTOM-RIGHT.
   - Perpendicular rising vertically on the RIGHT.
   - Hypotenuse rising from bottom-left to top-right.
   - Angle arc rotating strictly COUNTER-CLOCKWISE (ঘড়ির কাঁটার বিপরীত দিকে) from base up to hypotenuse.
3. Uploads V2 SVGs to ImageKit with cache-busting URLs.
4. Updates question bank and viewer HTML.
"""

import json
import os
import re
import requests

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# 1. DELETE OLD FILES FROM IMAGEKIT
# ─────────────────────────────────────────────────────────────────────────────
print("Cleaning up old ImageKit files...")
list_url = "https://api.imagekit.io/v1/files?path=%2Fmath_2nd_ch7%2F&limit=100"
res = requests.get(list_url, auth=auth, timeout=30)
if res.ok:
    for f in res.json():
        fid = f.get("fileId")
        requests.delete(f"https://api.imagekit.io/v1/files/{fid}", auth=auth, timeout=20)
        print(f"  Deleted old file: {f.get('name')}")

# ─────────────────────────────────────────────────────────────────────────────
# 2. DEFINE TRUE COUNTER-CLOCKWISE (ANTI-CLOCKWISE) V2 SVGs
# ─────────────────────────────────────────────────────────────────────────────

V2_SVGS = {
    # ── Q546: Inverse trig function graphs ──
    "svg_v2_q546_1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="170" x2="270" y2="170" stroke="#334155" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#334155" stroke-width="2"/>
  <line x1="30" y1="40" x2="270" y2="40" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <path d="M 50,45 Q 120,55 150,105 T 250,165" fill="none" stroke="#2563eb" stroke-width="3"/>
  <text x="275" y="174" font-family="sans-serif" font-size="14" fill="#334155">x</text>
  <text x="155" y="30" font-family="sans-serif" font-size="14" fill="#334155">y</text>
  <text x="135" y="45" font-family="sans-serif" font-size="13" fill="#64748b">π</text>
  <text x="130" y="108" font-family="sans-serif" font-size="13" fill="#64748b">π/2</text>
  <text x="138" y="185" font-family="sans-serif" font-size="13" fill="#64748b">O</text>
</svg>""",

    "svg_v2_q546_2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="100" x2="270" y2="100" stroke="#334155" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#334155" stroke-width="2"/>
  <line x1="30" y1="40" x2="270" y2="40" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="30" y1="160" x2="270" y2="160" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <path d="M 50,155 Q 110,145 150,100 T 250,45" fill="none" stroke="#2563eb" stroke-width="3"/>
  <text x="275" y="104" font-family="sans-serif" font-size="14" fill="#334155">x</text>
  <text x="155" y="30" font-family="sans-serif" font-size="14" fill="#334155">y</text>
  <text x="125" y="45" font-family="sans-serif" font-size="13" fill="#64748b">π/2</text>
  <text x="120" y="165" font-family="sans-serif" font-size="13" fill="#64748b">-π/2</text>
</svg>""",

    "svg_v2_q546_3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="100" x2="270" y2="100" stroke="#334155" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#334155" stroke-width="2"/>
  <path d="M 80,160 C 130,150 140,110 150,100 C 160,90 170,50 220,40" fill="none" stroke="#2563eb" stroke-width="3"/>
  <circle cx="80" cy="160" r="4" fill="#2563eb"/>
  <circle cx="220" cy="40" r="4" fill="#2563eb"/>
  <text x="275" y="104" font-family="sans-serif" font-size="14" fill="#334155">x</text>
  <text x="155" y="30" font-family="sans-serif" font-size="14" fill="#334155">y</text>
</svg>""",

    "svg_v2_q546_4.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="160" x2="270" y2="160" stroke="#334155" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#334155" stroke-width="2"/>
  <path d="M 80,40 C 130,50 140,90 150,100 C 160,110 170,150 220,160" fill="none" stroke="#2563eb" stroke-width="3"/>
  <circle cx="80" cy="40" r="4" fill="#2563eb"/>
  <circle cx="220" cy="160" r="4" fill="#2563eb"/>
  <text x="275" y="164" font-family="sans-serif" font-size="14" fill="#334155">x</text>
  <text x="155" y="30" font-family="sans-serif" font-size="14" fill="#334155">y</text>
</svg>""",

    # ── Graph of y = sin^-1 x ──
    "svg_v2_sin_inv.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="110" x2="290" y2="110" stroke="#334155" stroke-width="2"/>
  <line x1="160" y1="20" x2="160" y2="200" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="40" x2="240" y2="40" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="180" x2="240" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="40" x2="80" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="240" y1="40" x2="240" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <path d="M 80,180 C 135,175 145,130 160,110 C 175,90 185,45 240,40" fill="none" stroke="#0284c7" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="80" cy="180" r="5" fill="#0284c7"/>
  <circle cx="240" cy="40" r="5" fill="#0284c7"/>
  <text x="295" y="115" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">X</text>
  <text x="165" y="30" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">Y</text>
  <text x="235" y="128" font-family="sans-serif" font-size="13" fill="#64748b">1</text>
  <text x="70" y="128" font-family="sans-serif" font-size="13" fill="#64748b">-1</text>
  <text x="135" y="45" font-family="sans-serif" font-size="13" fill="#64748b">π/2</text>
  <text x="130" y="185" font-family="sans-serif" font-size="13" fill="#64748b">-π/2</text>
  <text x="168" y="125" font-family="sans-serif" font-size="13" fill="#64748b">O</text>
</svg>""",

    # ── Graph of y = cos^-1 x ──
    "svg_v2_cos_inv.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="180" x2="290" y2="180" stroke="#334155" stroke-width="2"/>
  <line x1="160" y1="20" x2="160" y2="200" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="40" x2="240" y2="40" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="40" x2="80" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="240" y1="40" x2="240" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <path d="M 80,40 C 135,45 145,90 160,110 C 175,130 185,175 240,180" fill="none" stroke="#0284c7" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="80" cy="40" r="5" fill="#0284c7"/>
  <circle cx="240" cy="180" r="5" fill="#0284c7"/>
  <text x="295" y="185" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">X</text>
  <text x="165" y="30" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">Y</text>
  <text x="235" y="198" font-family="sans-serif" font-size="13" fill="#64748b">1</text>
  <text x="70" y="198" font-family="sans-serif" font-size="13" fill="#64748b">-1</text>
  <text x="140" y="45" font-family="sans-serif" font-size="13" fill="#64748b">π</text>
  <text x="135" y="115" font-family="sans-serif" font-size="13" fill="#64748b">π/2</text>
</svg>""",

    # ── Graph of y = tan^-1 x ──
    "svg_v2_tan_inv.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="100" x2="290" y2="100" stroke="#334155" stroke-width="2"/>
  <line x1="160" y1="20" x2="160" y2="180" stroke="#334155" stroke-width="2"/>
  <line x1="30" y1="40" x2="290" y2="40" stroke="#cbd5e1" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="30" y1="160" x2="290" y2="160" stroke="#cbd5e1" stroke-dasharray="4,4" stroke-width="1.5"/>
  <path d="M 40,155 Q 120,150 160,100 T 280,45" fill="none" stroke="#0284c7" stroke-width="3.5" stroke-linecap="round"/>
  <text x="295" y="105" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">X</text>
  <text x="165" y="30" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">Y</text>
  <text x="130" y="45" font-family="sans-serif" font-size="13" fill="#64748b">π/2</text>
  <text x="125" y="165" font-family="sans-serif" font-size="13" fill="#64748b">-π/2</text>
</svg>""",

    # ── Q863: Hypotenuse=1, angle theta at B (bottom-left, counter-clockwise to BA) ──
    "svg_v2_q863.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- Base BC horizontal from (50, 190) to (270, 190) -->
  <!-- Perpendicular AC vertical from (270, 190) to (270, 50) -->
  <!-- Hypotenuse BA from (50, 190) to (270, 50) -->
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Right-angle symbol at C (270, 190) -->
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <!-- Counter-clockwise angle arc at B (from base BC rotating upwards CCW to hypotenuse BA) -->
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <!-- Vertex Labels -->
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <!-- Dimension & Angle Labels -->
  <text x="145" y="105" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#2563eb">1</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
  <text x="160" y="212" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#64748b">BC</text>
  <text x="295" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#64748b">AC</text>
</svg>""",

    # ── Q806 / Q829 / Q840 / Q864 / Q886: Right triangle with angle theta at B ──
    "svg_v2_q806.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q796 / Q855: Right triangle AB=2, BC=y=sqrt(5), AC=x ──
    "svg_v2_q796.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
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

    # ── Q775 / Q756: Right triangle 3, 4, 5 with angle ACB = theta ──
    "svg_v2_q775.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="290" y="125" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">3</text>
  <text x="145" y="105" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">5</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q794 / Q786: Right triangle 5, 12, 13 with angle phi ──
    "svg_v2_q794.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 260" width="100%" height="260">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,220 250,220 250,30" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="228,220 228,198 250,198" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,220 A 60,60 0 0,0 95,178" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="270" y="130" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">12</text>
  <text x="135" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">13</text>
  <text x="125" y="208" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">ϕ</text>
</svg>""",

    # ── Q901: Right triangle with angle theta at C ──
    "svg_v2_q901.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="145" y="105" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">5</text>
  <text x="160" y="214" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">3</text>
  <text x="290" y="125" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#2563eb">x</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q902: Right triangle with angle theta at C ──
    "svg_v2_q902.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="50,190 270,190 270,50" fill="none" stroke="#0f172a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="248,190 248,168 270,168" fill="none" stroke="#0f172a" stroke-width="2.0"/>
  <path d="M 110,190 A 60,60 0 0,0 98,159" fill="none" stroke="#2563eb" stroke-width="2.4"/>
  <text x="32" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">C</text>
  <text x="288" y="198" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">B</text>
  <text x="288" y="48" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#0f172a">A</text>
  <text x="145" y="105" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700" fill="#2563eb">x</text>
  <text x="160" y="214" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">y</text>
  <text x="290" y="125" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">2</text>
  <text x="125" y="175" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q894: Two right triangles (alpha and beta CCW) ──
    "svg_v2_q894.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <!-- Triangle 1 -->
  <polygon points="30,175 160,175 160,45" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="144,175 144,159 160,159" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 75,175 A 45,45 0 0,0 65,145" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="85" y="98" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">√3</text>
  <text x="95" y="196" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">√2</text>
  <text x="82" y="165" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">α</text>
  <text x="95" y="218" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">১ম চিত্র</text>
  <!-- Triangle 2 -->
  <polygon points="220,175 350,175 350,45" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="334,175 334,159 350,159" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 265,175 A 45,45 0 0,0 255,145" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="275" y="98" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">2√3</text>
  <text x="285" y="196" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">√3 + √2</text>
  <text x="272" y="165" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">β</text>
  <text x="285" y="218" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">২য় চিত্র</text>
</svg>""",

    # ── Q802 / Q882 / Q938: Double right triangles CCW ──
    "svg_v2_q802_triangles.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
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

    # ── Q811: River width CD=1 ──
    "svg_v2_q811.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="30" y1="60" x2="370" y2="60" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="30" y1="180" x2="370" y2="180" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="200" y1="60" x2="200" y2="180" stroke="#0f172a" stroke-width="2.8"/>
  <polyline points="200,80 215,80 215,60" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="70" y1="60" x2="200" y2="180" stroke="#0f172a" stroke-width="2.4"/>
  <line x1="340" y1="60" x2="200" y2="180" stroke="#0f172a" stroke-width="2.4"/>
  <path d="M 175,155 A 35,35 0 0,1 200,145" fill="none" stroke="#2563eb" stroke-width="2"/>
  <path d="M 200,140 A 40,40 0 0,1 230,153" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="70" y="45" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="200" y="45" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="340" y="45" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="200" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="135" y="48" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">y</text>
  <text x="270" y="48" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">x</text>
  <text x="215" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">1</text>
  <text x="175" y="145" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">θ</text>
  <text x="232" y="142" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">3θ</text>
</svg>""",

    # ── Q815: Symmetric angle array ──
    "svg_v2_q815.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" height="250">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="180" y1="210" x2="40" y2="70" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="180" y1="210" x2="110" y2="45" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="180" y1="210" x2="250" y2="45" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="180" y1="210" x2="320" y2="70" stroke="#0f172a" stroke-width="2.5"/>
  <text x="180" y="235" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="30" y="65" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">E</text>
  <text x="105" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">D</text>
  <text x="250" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="330" y="65" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="135" y="145" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">θ</text>
  <text x="180" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">θ</text>
  <text x="225" y="145" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">θ</text>
</svg>""",

    # ── Q816: Joint right triangles ──
    "svg_v2_q816.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="30" y1="180" x2="350" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <polygon points="190,180 80,180 80,60" fill="none" stroke="#0f172a" stroke-width="2.4"/>
  <polyline points="80,165 95,165 95,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <polygon points="190,180 300,180 300,80" fill="none" stroke="#0f172a" stroke-width="2.4"/>
  <polyline points="300,165 285,165 285,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="190" y1="180" x2="190" y2="50" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="190" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">O</text>
  <text x="70" y="55" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="70" y="195" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">A</text>
  <text x="310" y="75" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="310" y="195" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">D</text>
</svg>""",

    # ── Q817: Altitude and angle bisector ──
    "svg_v2_q817.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" height="250">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="140,40 40,200 300,200" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="140" y1="40" x2="140" y2="200" stroke="#0f172a" stroke-width="2.6"/>
  <polyline points="140,185 155,185 155,200" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="220" y1="200" x2="140" y2="100" stroke="#0f172a" stroke-dasharray="4,3" stroke-width="2"/>
  <line x1="40" y1="200" x2="140" y2="135" stroke="#0f172a" stroke-dasharray="4,3" stroke-width="2"/>
  <text x="140" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="25" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="315" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="140" y="222" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="80" y="110" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">5</text>
  <text x="155" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">3</text>
  <text x="220" y="222" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">1</text>
  <text x="245" y="150" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">EC=√5</text>
  <text x="65" y="185" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">β</text>
  <text x="260" y="190" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#2563eb">α</text>
</svg>""",

    # ── Q819: Springs and rod ──
    "svg_v2_q819.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="30" y1="210" x2="350" y2="210" stroke="#334155" stroke-width="2.5"/>
  <line x1="80" y1="80" x2="300" y2="210" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
  <line x1="80" y1="80" x2="80" y2="210" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="220" y1="120" x2="220" y2="210" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="75" y="70" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="315" y="215" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="220" y="110" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="50" y="150" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#0284c7">y₁ = 5 + sin t</text>
  <text x="235" y="165" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#0284c7">y₂ = 7 + cos 2t</text>
  <text x="180" y="140" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">13 m</text>
</svg>""",

    # ── Q865 / Q867 / Q883: Parabola and geometry ──
    "svg_v2_q865_parabola.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="180" y1="40" x2="180" y2="200" stroke="#0f172a" stroke-width="2.2"/>
  <path d="M 60,40 Q 180,210 300,40" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
  <line x1="180" y1="80" x2="260" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="180" y1="130" x2="110" y2="130" stroke="#0f172a" stroke-width="2"/>
  <polyline points="180,95 195,95 195,80" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <polyline points="180,115 165,115 165,130" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="220" y="70" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#0f172a">m</text>
  <text x="135" y="120" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#0f172a">b</text>
  <text x="195" y="110" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#0f172a">a</text>
  <text x="165" y="165" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" fill="#0f172a">n</text>
  <text x="250" y="30" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0284c7">f(x) = ax² + bx + c</text>
</svg>""",

    # ── Q868: Double triangles ──
    "svg_v2_q868.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <polygon points="120,40 40,190 200,190" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="120,60 100,60 100,40" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <polygon points="120,40 200,190 320,190" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="200,170 200,190 220,190" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="120" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="25" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="200" y="210" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="330" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="245" y="110" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">5</text>
  <text x="75" y="110" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">13</text>
  <text x="155" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">3</text>
</svg>""",

    # ── Q872 / Q887: Double triangles on straight line ──
    "svg_v2_q872.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="40" y1="180" x2="340" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="40" y1="40" x2="40" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="40" y1="40" x2="190" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <polyline points="40,160 60,160 60,180" fill="none" stroke="#0f172a" stroke-width="2"/>
  <line x1="340" y1="80" x2="340" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="340" y1="80" x2="190" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <polyline points="320,180 320,160 340,160" fill="none" stroke="#0f172a" stroke-width="2"/>
  <path d="M 160,180 A 30,30 0 0,0 170,160" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <path d="M 175,150 A 35,35 0 0,1 205,150" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <path d="M 210,160 A 30,30 0 0,0 220,180" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="25" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">4</text>
  <text x="115" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">1</text>
  <text x="355" y="135" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">1</text>
  <text x="265" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">√3</text>
  <text x="150" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">x</text>
  <text x="190" y="135" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">z</text>
  <text x="230" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">y</text>
</svg>""",

    "svg_v2_q887.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="12"/>
  <line x1="40" y1="180" x2="340" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="40" y1="40" x2="40" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="40" y1="40" x2="190" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <polyline points="40,160 60,160 60,180" fill="none" stroke="#0f172a" stroke-width="2"/>
  <line x1="340" y1="70" x2="340" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="340" y1="70" x2="190" y2="180" stroke="#0f172a" stroke-width="2.6"/>
  <polyline points="320,180 320,160 340,160" fill="none" stroke="#0f172a" stroke-width="2"/>
  <path d="M 160,180 A 30,30 0 0,0 170,160" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <path d="M 175,150 A 35,35 0 0,1 205,150" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <path d="M 210,160 A 30,30 0 0,0 220,180" fill="none" stroke="#2563eb" stroke-width="2.2"/>
  <text x="25" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">3</text>
  <text x="115" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">1</text>
  <text x="355" y="130" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">2</text>
  <text x="265" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">1</text>
  <text x="150" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">x</text>
  <text x="190" y="135" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">z</text>
  <text x="230" y="170" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">y</text>
</svg>"""
}

# ─────────────────────────────────────────────────────────────────────────────
# 3. UPLOAD V2 SVGs TO IMAGEKIT
# ─────────────────────────────────────────────────────────────────────────────
svg_out_dir = os.path.join(HERE, "svg_diagrams")
os.makedirs(svg_out_dir, exist_ok=True)

v2_uploaded_urls = {}
for fname, content in V2_SVGS.items():
    # Save locally
    p = os.path.join(svg_out_dir, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

    # Upload to ImageKit
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
        v2_uploaded_urls[fname] = ik_url
        print(f"  [UPLOADED V2] {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] {fname}: {res.text}")

# ─────────────────────────────────────────────────────────────────────────────
# 4. QUESTION MAPPING (V2 URLs)
# ─────────────────────────────────────────────────────────────────────────────
QUESTION_V2_MAP = {
    863: v2_uploaded_urls["svg_v2_q863.svg"],
    806: v2_uploaded_urls["svg_v2_q806.svg"],
    796: v2_uploaded_urls["svg_v2_q796.svg"],
    775: v2_uploaded_urls["svg_v2_q775.svg"],
    756: v2_uploaded_urls["svg_v2_q775.svg"],
    794: v2_uploaded_urls["svg_v2_q794.svg"],
    786: v2_uploaded_urls["svg_v2_q794.svg"],
    901: v2_uploaded_urls["svg_v2_q901.svg"],
    902: v2_uploaded_urls["svg_v2_q902.svg"],
    894: v2_uploaded_urls["svg_v2_q894.svg"],
    802: v2_uploaded_urls["svg_v2_q802_triangles.svg"],
    882: v2_uploaded_urls["svg_v2_q802_triangles.svg"],
    938: v2_uploaded_urls["svg_v2_q802_triangles.svg"],
    811: v2_uploaded_urls["svg_v2_q811.svg"],
    815: v2_uploaded_urls["svg_v2_q815.svg"],
    816: v2_uploaded_urls["svg_v2_q816.svg"],
    817: v2_uploaded_urls["svg_v2_q817.svg"],
    819: v2_uploaded_urls["svg_v2_q819.svg"],
    829: v2_uploaded_urls["svg_v2_q806.svg"],
    840: v2_uploaded_urls["svg_v2_q806.svg"],
    846: v2_uploaded_urls["svg_v2_q894.svg"],
    855: v2_uploaded_urls["svg_v2_q796.svg"],
    864: v2_uploaded_urls["svg_v2_q806.svg"],
    865: v2_uploaded_urls["svg_v2_q865_parabola.svg"],
    867: v2_uploaded_urls["svg_v2_q865_parabola.svg"],
    868: v2_uploaded_urls["svg_v2_q868.svg"],
    872: v2_uploaded_urls["svg_v2_q872.svg"],
    873: v2_uploaded_urls["svg_v2_q872.svg"],
    874: v2_uploaded_urls["svg_v2_q817.svg"],
    883: v2_uploaded_urls["svg_v2_q865_parabola.svg"],
    884: v2_uploaded_urls["svg_v2_q865_parabola.svg"],
    885: v2_uploaded_urls["svg_v2_q865_parabola.svg"],
    886: v2_uploaded_urls["svg_v2_q806.svg"],
    887: v2_uploaded_urls["svg_v2_q887.svg"],
    892: v2_uploaded_urls["svg_v2_q872.svg"],
    896: v2_uploaded_urls["svg_v2_q872.svg"],
    546: [v2_uploaded_urls["svg_v2_q546_1.svg"], v2_uploaded_urls["svg_v2_q546_2.svg"], v2_uploaded_urls["svg_v2_q546_3.svg"], v2_uploaded_urls["svg_v2_q546_4.svg"]],
    567: v2_uploaded_urls["svg_v2_sin_inv.svg"],
    574: v2_uploaded_urls["svg_v2_cos_inv.svg"],
    575: v2_uploaded_urls["svg_v2_cos_inv.svg"],
    582: v2_uploaded_urls["svg_v2_sin_inv.svg"],
    583: v2_uploaded_urls["svg_v2_sin_inv.svg"],
    590: v2_uploaded_urls["svg_v2_tan_inv.svg"],
    591: v2_uploaded_urls["svg_v2_tan_inv.svg"],
    622: v2_uploaded_urls["svg_v2_cos_inv.svg"],
    623: v2_uploaded_urls["svg_v2_cos_inv.svg"],
    746: v2_uploaded_urls["svg_v2_sin_inv.svg"],
    747: v2_uploaded_urls["svg_v2_cos_inv.svg"],
}

# ─────────────────────────────────────────────────────────────────────────────
# 5. UPDATE RAW JSON AND PROCESSED_QUESTIONS.JSON
# ─────────────────────────────────────────────────────────────────────────────
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for q_idx, q in enumerate(raw_data["data"]["questions"], 1):
    if q_idx in QUESTION_V2_MAP:
        mapping = QUESTION_V2_MAP[q_idx]
        if isinstance(mapping, list):
            svg_url = mapping[0]
            for opt_idx, opt in enumerate(q.get("question_options", [])):
                opt_body = opt.get("body", {})
                for ek, ent in opt_body.get("entityMap", {}).items():
                    if ent.get("type") == "IMAGE":
                        ent["data"]["src"] = mapping[min(opt_idx, len(mapping)-1)]
        else:
            svg_url = mapping
        
        body = q.get("question", {}).get("body", {})
        for ek, ent in body.get("entityMap", {}).items():
            if ent.get("type") == "IMAGE":
                ent["data"]["src"] = svg_url

with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

# Update processed_questions.json directly
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in QUESTION_V2_MAP:
        mapping = QUESTION_V2_MAP[qn]
        if isinstance(mapping, list):
            if q.get("o"):
                for i, opt_url in enumerate(mapping):
                    if i < len(q["o"]):
                        q["o"][i] = f"![চিত্র]({opt_url})"
        else:
            svg_url = mapping
            if "![" in q["q"]:
                q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({svg_url})", q["q"])
            else:
                q["q"] = f"![চিত্র]({svg_url})\n" + q["q"]

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("Successfully deployed V2 counter-clockwise standard SVGs to all question files!")
