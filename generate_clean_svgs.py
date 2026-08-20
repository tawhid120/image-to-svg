# -*- coding: utf-8 -*-
"""
generate_clean_svgs.py
======================
Generates pristine, high-DPI vector SVG illustrations for question diagrams.
Theme-adaptive (supports CSS color styling / light-dark contrast).
"""

import os

SVG_TEMPLATES = {
    # Q796: Right triangle with perpendicular=2, base=sqrt(5), hypotenuse=x
    "svg_q796.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240" width="100%" height="240" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 16px; font-weight: 600; text-anchor: middle; }
      .accent { fill: #2563eb; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <polygon points="50,190 270,190 50,40" class="stroke-line" />
  <!-- Right angle square -->
  <polyline points="50,170 70,170 70,190" class="stroke-line" stroke-width="1.8" />
  <!-- Labels -->
  <text x="35" y="40" class="label">A</text>
  <text x="35" y="200" class="label">B</text>
  <text x="285" y="195" class="label">C</text>
  <text x="30" y="120" class="label">2</text>
  <text x="160" y="215" class="label">y = √5</text>
  <text x="175" y="105" class="label accent">x</text>
</svg>""",

    # Q806: Right triangle ABC at C, angle B = theta
    "svg_q806.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240" width="100%" height="240" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 16px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <polygon points="50,40 270,190 50,190" class="stroke-line" />
  <polyline points="50,170 70,170 70,190" class="stroke-line" stroke-width="1.8" />
  <!-- Angle arc at B -->
  <path d="M 230,190 A 40,40 0 0,0 245,172" class="stroke-line" stroke-width="1.8"/>
  <!-- Labels -->
  <text x="35" y="40" class="label">A</text>
  <text x="35" y="205" class="label">C</text>
  <text x="285" y="195" class="label">B</text>
  <text x="215" y="180" class="label">θ</text>
</svg>""",

    # Q811: River width CD=1, AD=y (theta), BD=x (3 theta)
    "svg_q811.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 240" width="100%" height="240" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .river-line { stroke: #0284c7; stroke-width: 2; stroke-dasharray: 4,4; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 15px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <!-- River Bank -->
  <line x1="40" y1="60" x2="360" y2="60" class="river-line" />
  <line x1="40" y1="180" x2="360" y2="180" class="river-line" />
  <!-- CD vertical line -->
  <line x1="200" y1="60" x2="200" y2="180" class="stroke-line" />
  <polyline points="200,80 215,80 215,60" class="stroke-line" stroke-width="1.5"/>
  <!-- A, B points -->
  <line x1="80" y1="60" x2="200" y2="180" class="stroke-line" />
  <line x1="330" y1="60" x2="200" y2="180" class="stroke-line" />
  <!-- Angle arcs at C -->
  <path d="M 180,154 A 35,35 0 0,1 200,145" class="stroke-line" stroke-width="1.5"/>
  <path d="M 200,140 A 40,40 0 0,1 228,153" class="stroke-line" stroke-width="1.5"/>
  <!-- Labels -->
  <text x="80" y="45" class="label">A</text>
  <text x="200" y="45" class="label">D</text>
  <text x="330" y="45" class="label">B</text>
  <text x="200" y="205" class="label">C</text>
  <text x="140" y="50" class="label">y</text>
  <text x="265" y="50" class="label">x</text>
  <text x="215" y="125" class="label">1</text>
  <text x="175" y="145" class="label">θ</text>
  <text x="232" y="142" class="label">3θ</text>
</svg>""",

    # Q817: Triangle with AD perp BC, angle bisector BF
    "svg_q817.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" width="100%" height="250" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 14.5px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <polygon points="140,40 40,200 300,200" class="stroke-line" />
  <!-- Altitude AD -->
  <line x1="140" y1="40" x2="140" y2="200" class="stroke-line" />
  <polyline points="140,185 155,185 155,200" class="stroke-line" stroke-width="1.5" />
  <!-- Points E, F -->
  <line x1="220" y1="200" x2="140" y2="100" class="stroke-line" stroke-dasharray="4,3"/>
  <line x1="40" y1="200" x2="140" y2="135" class="stroke-line" stroke-dasharray="4,3"/>
  <!-- Labels -->
  <text x="140" y="30" class="label">A</text>
  <text x="25" y="205" class="label">B</text>
  <text x="315" y="205" class="label">C</text>
  <text x="140" y="220" class="label">D</text>
  <text x="80" y="110" class="label">5</text>
  <text x="155" y="125" class="label">3</text>
  <text x="220" y="220" class="label">1</text>
  <text x="245" y="150" class="label">EC=√5</text>
  <text x="65" y="185" class="label">β</text>
  <text x="260" y="190" class="label">α</text>
</svg>""",

    # Q872 / Q887: Double right triangles on straight line (angles x, z, y)
    "svg_q872.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" height="240" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 16px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <!-- Ground straight line -->
  <line x1="40" y1="190" x2="340" y2="190" class="stroke-line" />
  <!-- Left triangle -->
  <line x1="40" y1="40" x2="40" y2="190" class="stroke-line" />
  <line x1="40" y1="40" x2="190" y2="190" class="stroke-line" />
  <polyline points="40,170 60,170 60,190" class="stroke-line" stroke-width="1.8" />
  <!-- Right triangle -->
  <line x1="340" y1="80" x2="340" y2="190" class="stroke-line" />
  <line x1="340" y1="80" x2="190" y2="190" class="stroke-line" />
  <polyline points="320,190 320,170 340,170" class="stroke-line" stroke-width="1.8" />
  <!-- Angle arcs -->
  <path d="M 160,190 A 30,30 0 0,0 170,170" class="stroke-line" stroke-width="1.8"/>
  <path d="M 175,160 A 35,35 0 0,1 205,160" class="stroke-line" stroke-width="1.8"/>
  <path d="M 210,170 A 30,30 0 0,0 220,190" class="stroke-line" stroke-width="1.8"/>
  <!-- Labels -->
  <text x="25" y="115" class="label">4</text>
  <text x="115" y="212" class="label">1</text>
  <text x="355" y="135" class="label">1</text>
  <text x="265" y="212" class="label">√3</text>
  <text x="150" y="180" class="label">x</text>
  <text x="190" y="145" class="label">z</text>
  <text x="230" y="180" class="label">y</text>
</svg>""",

    # Q887: Double right triangles on straight line (perp=3, base=1 & perp=2, base=1)
    "svg_q887.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" height="240" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 16px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <line x1="40" y1="190" x2="340" y2="190" class="stroke-line" />
  <line x1="40" y1="40" x2="40" y2="190" class="stroke-line" />
  <line x1="40" y1="40" x2="190" y2="190" class="stroke-line" />
  <polyline points="40,170 60,170 60,190" class="stroke-line" stroke-width="1.8" />
  <line x1="340" y1="70" x2="340" y2="190" class="stroke-line" />
  <line x1="340" y1="70" x2="190" y2="190" class="stroke-line" />
  <polyline points="320,190 320,170 340,170" class="stroke-line" stroke-width="1.8" />
  <path d="M 160,190 A 30,30 0 0,0 170,170" class="stroke-line" stroke-width="1.8"/>
  <path d="M 175,160 A 35,35 0 0,1 205,160" class="stroke-line" stroke-width="1.8"/>
  <path d="M 210,170 A 30,30 0 0,0 220,190" class="stroke-line" stroke-width="1.8"/>
  <text x="25" y="115" class="label">3</text>
  <text x="115" y="212" class="label">1</text>
  <text x="355" y="135" class="label">2</text>
  <text x="265" y="212" class="label">1</text>
  <text x="150" y="180" class="label">x</text>
  <text x="190" y="145" class="label">z</text>
  <text x="230" y="180" class="label">y</text>
</svg>""",

    # Q894: Two right triangles (alpha and beta)
    "svg_q894.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" height="220" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.3; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 15px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <!-- Triangle 1 -->
  <polygon points="30,170 160,170 160,40" class="stroke-line"/>
  <polyline points="145,170 145,155 160,155" class="stroke-line" stroke-width="1.5"/>
  <path d="M 60,170 A 30,30 0 0,0 52,148" class="stroke-line" stroke-width="1.5"/>
  <text x="90" y="95" class="label">√3</text>
  <text x="95" y="190" class="label">√2</text>
  <text x="70" y="162" class="label">α</text>
  <text x="95" y="210" class="label" font-size="13">১ম চিত্র</text>
  <!-- Triangle 2 -->
  <polygon points="220,170 350,170 350,40" class="stroke-line"/>
  <polyline points="335,170 335,155 350,155" class="stroke-line" stroke-width="1.5"/>
  <path d="M 250,170 A 30,30 0 0,0 242,148" class="stroke-line" stroke-width="1.5"/>
  <text x="275" y="95" class="label">2√3</text>
  <text x="285" y="190" class="label">√3 + √2</text>
  <text x="260" y="162" class="label">β</text>
  <text x="285" y="210" class="label" font-size="13">২য় চিত্র</text>
</svg>""",

    # Q901: Right triangle ABC at B, AC=5, BC=3, AB=x
    "svg_q901.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 240" width="100%" height="240" class="math-diagram">
  <defs>
    <style>
      .bg { fill: var(--card, #ffffff); }
      .stroke-line { stroke: var(--fg, #0f172a); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .label { fill: var(--fg, #0f172a); font-family: 'Hind Siliguri', 'Segoe UI', sans-serif; font-size: 16px; font-weight: 600; text-anchor: middle; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="12"/>
  <polygon points="50,190 250,190 250,40" class="stroke-line" />
  <polyline points="230,190 230,170 250,170" class="stroke-line" stroke-width="1.8" />
  <path d="M 90,190 A 40,40 0 0,0 80,165" class="stroke-line" stroke-width="1.8"/>
  <text x="250" y="25" class="label">A</text>
  <text x="265" y="200" class="label">B</text>
  <text x="35" y="200" class="label">C</text>
  <text x="135" y="105" class="label">5</text>
  <text x="150" y="212" class="label">3</text>
  <text x="270" y="115" class="label">x</text>
  <text x="105" y="180" class="label">θ</text>
</svg>"""
}

HERE = os.path.dirname(os.path.abspath(__file__))
svg_dir = os.path.join(HERE, "svg_diagrams")
os.makedirs(svg_dir, exist_ok=True)

for name, content in SVG_TEMPLATES.items():
    file_path = os.path.join(svg_dir, name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
print(f"Generated {len(SVG_TEMPLATES)} clean SVGs in {svg_dir}")
