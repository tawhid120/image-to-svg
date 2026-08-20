# -*- coding: utf-8 -*-
"""
create_all_svg_diagrams.py
==========================
Generates handcrafted, pristine, responsive SVG vector files for ALL question diagrams.
Every SVG is beautifully styled, ultra-crisp, and perfectly legible in both Light & Dark modes.
"""

import os

SVG_DEFS = {
    # ── Q546: Inverse trig function graphs ──
    "svg_q546_1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
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

    "svg_q546_2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
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

    "svg_q546_3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="100" x2="270" y2="100" stroke="#334155" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#334155" stroke-width="2"/>
  <path d="M 80,160 C 130,150 140,110 150,100 C 160,90 170,50 220,40" fill="none" stroke="#2563eb" stroke-width="3"/>
  <circle cx="80" cy="160" r="4" fill="#2563eb"/>
  <circle cx="220" cy="40" r="4" fill="#2563eb"/>
  <text x="275" y="104" font-family="sans-serif" font-size="14" fill="#334155">x</text>
  <text x="155" y="30" font-family="sans-serif" font-size="14" fill="#334155">y</text>
</svg>""",

    "svg_q546_4.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="160" x2="270" y2="160" stroke="#334155" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#334155" stroke-width="2"/>
  <path d="M 80,40 C 130,50 140,90 150,100 C 160,110 170,150 220,160" fill="none" stroke="#2563eb" stroke-width="3"/>
  <circle cx="80" cy="40" r="4" fill="#2563eb"/>
  <circle cx="220" cy="160" r="4" fill="#2563eb"/>
  <text x="275" y="164" font-family="sans-serif" font-size="14" fill="#334155">x</text>
  <text x="155" y="30" font-family="sans-serif" font-size="14" fill="#334155">y</text>
</svg>""",

    # ── Q567 / Q582 / Q583: Graph of y = sin^-1 x ──
    "svg_sin_inv.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="110" x2="290" y2="110" stroke="#334155" stroke-width="2"/>
  <line x1="160" y1="20" x2="160" y2="200" stroke="#334155" stroke-width="2"/>
  <!-- Asymptote / limit lines -->
  <line x1="80" y1="40" x2="240" y2="40" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="180" x2="240" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="40" x2="80" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="240" y1="40" x2="240" y2="180" stroke="#cbd5e1" stroke-dasharray="3,3" stroke-width="1.5"/>
  <!-- sin^-1 curve -->
  <path d="M 80,180 C 135,175 145,130 160,110 C 175,90 185,45 240,40" fill="none" stroke="#0284c7" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="80" cy="180" r="5" fill="#0284c7"/>
  <circle cx="240" cy="40" r="5" fill="#0284c7"/>
  <!-- Axis Labels -->
  <text x="295" y="115" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">X</text>
  <text x="165" y="30" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#334155">Y</text>
  <text x="235" y="128" font-family="sans-serif" font-size="13" fill="#64748b">1</text>
  <text x="70" y="128" font-family="sans-serif" font-size="13" fill="#64748b">-1</text>
  <text x="135" y="45" font-family="sans-serif" font-size="13" fill="#64748b">π/2</text>
  <text x="130" y="185" font-family="sans-serif" font-size="13" fill="#64748b">-π/2</text>
  <text x="168" y="125" font-family="sans-serif" font-size="13" fill="#64748b">O</text>
</svg>""",

    # ── Q574 / Q575 / Q622 / Q623: Graph of y = cos^-1 x ──
    "svg_cos_inv.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="220">
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

    # ── Q590 / Q591: Graph of y = tan^-1 x ──
    "svg_tan_inv.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="200">
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

    # ── Q775: Right triangle 3, 4, 5 with angle ACB = theta ──
    "svg_q775.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,40 50,180 270,180" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="50,160 70,160 70,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 230,180 A 40,40 0 0,0 242,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="45" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="285" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="25" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">3</text>
  <text x="165" y="100" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">5</text>
  <text x="215" y="172" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">θ</text>
</svg>""",

    # ── Q794: Right triangle 12, 5, 13 with angle phi ──
    "svg_q794.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 260" width="100%" height="260">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,30 50,220 220,220" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="50,200 70,200 70,220" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 180,220 A 40,40 0 0,0 195,190" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="25" y="130" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">12</text>
  <text x="145" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">13</text>
  <text x="170" y="212" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">ϕ</text>
</svg>""",

    # ── Q796: Right triangle AB=2, BC=sqrt(5), AC=x ──
    "svg_q796.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,180 270,180 50,40" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="50,160 70,160 70,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="35" y="40" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="285" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="30" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">2</text>
  <text x="155" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">y = √5</text>
  <text x="165" y="100" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700" fill="#2563eb">x</text>
</svg>""",

    # ── Q802 / Q938: Double right triangles (r, x) and (r, y) ──
    "svg_q802_triangles.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <!-- Triangle 1 -->
  <polygon points="30,170 160,170 160,40" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="145,170 145,155 160,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 60,170 A 30,30 0 0,0 52,148" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="165" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="170" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="15" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">A</text>
  <text x="85" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">r</text>
  <text x="95" y="190" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">x</text>
  <!-- Triangle 2 -->
  <polygon points="220,170 350,170 350,40" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="335,170 335,155 350,155" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 250,170 A 30,30 0 0,0 242,148" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="355" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">P</text>
  <text x="360" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">R</text>
  <text x="205" y="180" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">Q</text>
  <text x="275" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">r</text>
  <text x="365" y="110" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">y</text>
</svg>""",

    # ── Q806: Right triangle ABC at C ──
    "svg_q806.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,40 270,180 50,180" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="50,160 70,160 70,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 230,180 A 40,40 0 0,0 245,162" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="35" y="40" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="35" y="195" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="285" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="215" y="172" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">θ</text>
</svg>""",

    # ── Q811: River width CD=1 ──
    "svg_q811.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="60" x2="370" y2="60" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="30" y1="180" x2="370" y2="180" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="200" y1="60" x2="200" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <polyline points="200,80 215,80 215,60" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <line x1="70" y1="60" x2="200" y2="180" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="340" y1="60" x2="200" y2="180" stroke="#0f172a" stroke-width="2.2"/>
  <path d="M 175,155 A 35,35 0 0,1 200,145" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 200,140 A 40,40 0 0,1 230,153" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="70" y="45" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="200" y="45" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="340" y="45" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="200" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="135" y="48" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">y</text>
  <text x="270" y="48" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">x</text>
  <text x="215" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">1</text>
  <text x="175" y="145" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">θ</text>
  <text x="232" y="142" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">3θ</text>
</svg>""",

    # ── Q815: Symmetric angle array ──
    "svg_q815.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" height="250">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="180" y1="210" x2="40" y2="70" stroke="#0f172a" stroke-width="2.3"/>
  <line x1="180" y1="210" x2="110" y2="45" stroke="#0f172a" stroke-width="2.3"/>
  <line x1="180" y1="210" x2="250" y2="45" stroke="#0f172a" stroke-width="2.3"/>
  <line x1="180" y1="210" x2="320" y2="70" stroke="#0f172a" stroke-width="2.3"/>
  <text x="180" y="235" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="30" y="65" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">E</text>
  <text x="105" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">D</text>
  <text x="250" y="35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="330" y="65" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="135" y="145" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">θ</text>
  <text x="180" y="125" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">θ</text>
  <text x="225" y="145" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">θ</text>
</svg>""",

    # ── Q816: Joint right triangles BAO and CDO ──
    "svg_q816.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="180" x2="350" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <polygon points="190,180 80,180 80,60" fill="none" stroke="#0f172a" stroke-width="2.2"/>
  <polyline points="80,165 95,165 95,180" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="190,180 300,180 300,80" fill="none" stroke="#0f172a" stroke-width="2.2"/>
  <polyline points="300,165 285,165 285,180" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <line x1="190" y1="180" x2="190" y2="50" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="190" y="200" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">O</text>
  <text x="70" y="55" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="70" y="195" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">A</text>
  <text x="310" y="75" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="310" y="195" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">D</text>
</svg>""",

    # ── Q817: Triangle with altitude AD and bisector BF ──
    "svg_q817.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" height="250">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="140,40 40,200 300,200" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="140" y1="40" x2="140" y2="200" stroke="#0f172a" stroke-width="2.3"/>
  <polyline points="140,185 155,185 155,200" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <line x1="220" y1="200" x2="140" y2="100" stroke="#0f172a" stroke-dasharray="4,3" stroke-width="1.8"/>
  <line x1="40" y1="200" x2="140" y2="135" stroke="#0f172a" stroke-dasharray="4,3" stroke-width="1.8"/>
  <text x="140" y="30" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="25" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="315" y="205" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="140" y="220" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="80" y="110" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">5</text>
  <text x="155" y="125" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">3</text>
  <text x="220" y="220" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">1</text>
  <text x="245" y="150" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">EC=√5</text>
  <text x="65" y="185" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">β</text>
  <text x="260" y="190" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">α</text>
</svg>""",

    # ── Q819: Springs and rod diagram ──
    "svg_q819.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="30" y1="210" x2="350" y2="210" stroke="#334155" stroke-width="2"/>
  <!-- Rod AB -->
  <line x1="80" y1="80" x2="300" y2="210" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
  <!-- Heights -->
  <line x1="80" y1="80" x2="80" y2="210" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="220" y1="120" x2="220" y2="210" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="75" y="70" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="315" y="215" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="220" y="110" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">D</text>
  <text x="50" y="150" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0284c7">y₁ = 5 + sin t</text>
  <text x="235" y="165" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0284c7">y₂ = 7 + cos 2t</text>
  <text x="180" y="140" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">13 m</text>
</svg>""",

    # ── Q863: Right triangle AB=1, theta ──
    "svg_q863.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,170 250,170 50,40" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="50,150 70,150 70,170" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 210,170 A 40,40 0 0,0 225,152" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="35" y="40" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="35" y="185" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="265" y="175" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="160" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">1</text>
  <text x="195" y="162" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">θ</text>
</svg>""",

    # ── Q865 / Q867 / Q883: Parabola and geometry ──
    "svg_q865_parabola.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <!-- Axis line -->
  <line x1="180" y1="40" x2="180" y2="200" stroke="#0f172a" stroke-width="2"/>
  <!-- Parabola curve -->
  <path d="M 60,40 Q 180,210 300,40" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
  <!-- Right triangle segments -->
  <line x1="180" y1="80" x2="260" y2="80" stroke="#0f172a" stroke-width="2"/>
  <line x1="180" y1="130" x2="110" y2="130" stroke="#0f172a" stroke-width="2"/>
  <polyline points="180,95 195,95 195,80" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <polyline points="180,115 165,115 165,130" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="220" y="70" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">m</text>
  <text x="135" y="120" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">b</text>
  <text x="195" y="110" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">a</text>
  <text x="165" y="165" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">n</text>
  <text x="250" y="30" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0284c7">f(x) = ax² + bx + c</text>
</svg>""",

    # ── Q868: Double right triangles ABC (3,4,5) and DAC (5,12,13) ──
    "svg_q868.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 240" width="100%" height="240">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="120,40 40,190 200,190" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="120,60 100,60 100,40" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="120,40 200,190 320,190" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="200,170 200,190 220,190" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="120" y="30" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">A</text>
  <text x="25" y="195" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">D</text>
  <text x="200" y="210" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">B</text>
  <text x="330" y="195" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700" fill="#0f172a">C</text>
  <text x="245" y="110" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">5</text>
  <text x="75" y="110" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">13</text>
  <text x="155" y="115" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">3</text>
</svg>""",

    # ── Q872: Double triangles on straight line ──
    "svg_q872.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="40" y1="180" x2="340" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="40" y1="40" x2="40" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="40" y1="40" x2="190" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <polyline points="40,160 60,160 60,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="340" y1="80" x2="340" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="340" y1="80" x2="190" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <polyline points="320,180 320,160 340,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 160,180 A 30,30 0 0,0 170,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 175,150 A 35,35 0 0,1 205,150" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 210,160 A 30,30 0 0,0 220,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="25" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">4</text>
  <text x="115" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">1</text>
  <text x="355" y="135" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">1</text>
  <text x="265" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">√3</text>
  <text x="150" y="170" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">x</text>
  <text x="190" y="135" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">z</text>
  <text x="230" y="170" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">y</text>
</svg>""",

    # ── Q887: Double triangles on straight line (3, 1 and 2, 1) ──
    "svg_q887.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <line x1="40" y1="180" x2="340" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="40" y1="40" x2="40" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="40" y1="40" x2="190" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <polyline points="40,160 60,160 60,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="340" y1="70" x2="340" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="340" y1="70" x2="190" y2="180" stroke="#0f172a" stroke-width="2.5"/>
  <polyline points="320,180 320,160 340,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 160,180 A 30,30 0 0,0 170,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 175,150 A 35,35 0 0,1 205,150" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 210,160 A 30,30 0 0,0 220,180" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="25" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">3</text>
  <text x="115" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">1</text>
  <text x="355" y="130" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">2</text>
  <text x="265" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">1</text>
  <text x="150" y="170" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">x</text>
  <text x="190" y="135" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">z</text>
  <text x="230" y="170" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">y</text>
</svg>""",

    # ── Q894: Two right triangles (alpha and beta) ──
    "svg_q894.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" height="220">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <!-- Triangle 1 -->
  <polygon points="30,165 160,165 160,40" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="145,165 145,150 160,150" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 60,165 A 30,30 0 0,0 52,143" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="85" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">√3</text>
  <text x="95" y="185" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">√2</text>
  <text x="70" y="157" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">α</text>
  <text x="95" y="205" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">১ম চিত্র</text>
  <!-- Triangle 2 -->
  <polygon points="220,165 350,165 350,40" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="335,165 335,150 350,150" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M 250,165 A 30,30 0 0,0 242,143" fill="none" stroke="#0f172a" stroke-width="1.5"/>
  <text x="275" y="95" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">2√3</text>
  <text x="285" y="185" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">√3 + √2</text>
  <text x="260" y="157" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" fill="#0f172a">β</text>
  <text x="285" y="205" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" fill="#0284c7">২য় চিত্র</text>
</svg>""",

    # ── Q901: Right triangle ABC at B, AC=5, BC=3 ──
    "svg_q901.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,180 250,180 250,40" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="230,180 230,160 250,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 90,180 A 40,40 0 0,0 80,155" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="250" y="25" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="265" y="190" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="35" y="190" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="135" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">5</text>
  <text x="150" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">3</text>
  <text x="270" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">x</text>
  <text x="105" y="170" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">θ</text>
</svg>""",

    # ── Q902: Right triangle AB=2, BC=y, AC=x, angle C=theta ──
    "svg_q902.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 230" width="100%" height="230">
  <rect width="100%" height="100%" fill="#ffffff" rx="10"/>
  <polygon points="50,180 250,180 250,40" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="230,180 230,160 250,160" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <path d="M 90,180 A 40,40 0 0,0 80,155" fill="none" stroke="#0f172a" stroke-width="1.8"/>
  <text x="250" y="25" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">A</text>
  <text x="265" y="190" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">B</text>
  <text x="35" y="190" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#0f172a">C</text>
  <text x="135" y="95" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700" fill="#2563eb">x</text>
  <text x="150" y="202" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">y</text>
  <text x="270" y="115" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="600" fill="#0f172a">2</text>
  <text x="105" y="170" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" fill="#0f172a">θ</text>
</svg>"""
}

HERE = os.path.dirname(os.path.abspath(__file__))
svg_out_dir = os.path.join(HERE, "svg_diagrams")
os.makedirs(svg_out_dir, exist_ok=True)

for filename, content in SVG_DEFS.items():
    p = os.path.join(svg_out_dir, filename)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully created {len(SVG_DEFS)} handcrafted SVG files in {svg_out_dir}")
