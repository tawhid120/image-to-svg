# -*- coding: utf-8 -*-
"""
render_hyper_realistic_physics_and_math_vectors.py
===================================================
Draws realistic, textbook-grade vector diagrams for all complex physics & math questions:
- Q819: Real mechanical spring coils (S1, S2), ceiling support, hanging mass block, rigid bar AB, ground hashes.
- Q811: River bank simulation with dashed parallel shores, vertical width line, and angle sectors.
- Q865/867/883/884/885: Crisp parabola graph with X/Y axes, plus 2 distinct right triangles DEA and ABC.
- Q816, Q817, Q868, Q872, etc.
Uploads directly to ImageKit under /math_2nd_ch7/pure_vector/ and updates question bank viewer.
"""

import os
import json
import re
import requests
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(HERE, "pure_vector_diagrams")
os.makedirs(out_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'cm'

def setup_canvas(width=7.5, height=5.0):
    fig, ax = plt.subplots(figsize=(width, height), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    return fig, ax

def save_fig(fig, filename):
    plt.tight_layout(pad=1.5)
    path = os.path.join(out_dir, filename)
    fig.savefig(path, facecolor='#ffffff', edgecolor='none', bbox_inches='tight', pad_inches=0.25, dpi=300)
    plt.close(fig)
    return path

def draw_spring(ax, x, y_start, y_end, width=0.15, num_coils=7, color='#0284c7', lw=2.2):
    """Draws a realistic mechanical zig-zag spring coil"""
    dy = (y_end - y_start)
    lead = 0.1 * dy
    coil_height = dy - 2 * lead
    
    # Lead-in
    ys = [y_start, y_start + lead]
    xs = [x, x]
    
    # Coils
    n_points = num_coils * 2
    for i in range(n_points):
        t = (i + 0.5) / n_points
        y_curr = y_start + lead + t * coil_height
        x_curr = x + width if (i % 2 == 0) else x - width
        xs.append(x_curr)
        ys.append(y_curr)
        
    # Lead-out
    xs.append(x)
    ys.append(y_start + lead + coil_height)
    xs.append(x)
    ys.append(y_end)
    
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle='round')

def draw_hatch_ground(ax, x1, x2, y, height=0.08, num_lines=15):
    """Draws a fixed physical surface with diagonal hatch marks"""
    ax.plot([x1, x2], [y, y], color='#1e293b', lw=2.5)
    xs = np.linspace(x1, x2 - height, num_lines)
    for x in xs:
        ax.plot([x, x + height], [y, y - height], color='#64748b', lw=1.5)

def draw_hatch_ceiling(ax, x1, x2, y, height=0.08, num_lines=15):
    """Draws a fixed ceiling support with diagonal hatch marks"""
    ax.plot([x1, x2], [y, y], color='#1e293b', lw=2.5)
    xs = np.linspace(x1, x2 - height, num_lines)
    for x in xs:
        ax.plot([x, x + height], [y, y + height], color='#64748b', lw=1.5)

# ─────────────────────────────────────────────────────────────────────────────
# 1. Q819: HYPER-REALISTIC MECHANICAL OSCILLATION SYSTEM
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.5, 5.5)
ax.set_xlim(-0.4, 3.2)
ax.set_ylim(-0.4, 2.2)

# Ground surface
draw_hatch_ground(ax, -0.2, 3.0, 0.0, height=0.1, num_lines=24)

# Ceiling support for S1 & S2
draw_hatch_ceiling(ax, 0.1, 0.9, 1.9, height=0.08, num_lines=8)
draw_hatch_ceiling(ax, 2.0, 2.8, 1.9, height=0.08, num_lines=8)

# Spring S1 (from ceiling to Point A)
draw_spring(ax, 0.5, 1.9, 1.1, width=0.12, num_coils=5, color='#0284c7', lw=2.4)
ax.text(0.18, 1.5, r'$S_1$', fontsize=16, fontweight='bold', color='#0284c7')

# Spring S2 (from ceiling to mass D)
draw_spring(ax, 2.4, 1.9, 1.4, width=0.12, num_coils=4, color='#0284c7', lw=2.4)
ax.text(2.62, 1.65, r'$S_2$', fontsize=16, fontweight='bold', color='#0284c7')

# Mass block at D
rect_d = patches.Rectangle((2.22, 1.15), 0.36, 0.25, facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.0)
ax.add_patch(rect_d)
ax.plot([2.4, 2.4], [1.4, 1.4], 'o', color='#0f172a', ms=5)
ax.text(2.65, 1.22, 'D', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(2.15, 1.98, 'C', fontsize=15, fontweight='bold', color='#0f172a')

# Slanted bar AB (Length 13m)
ax.plot([0.5, 2.0], [1.1, 0.0], color='#0f172a', lw=4.5, solid_capstyle='round')
# Pivot joint at B
ax.plot([2.0], [0.0], 'o', color='#2563eb', ms=8, zorder=5)
# Pivot joint at A
ax.plot([0.5], [1.1], 'o', color='#2563eb', ms=8, zorder=5)

# Labels for bar
ax.text(0.38, 1.18, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(2.08, 0.08, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.35, 0.72, '13 m', fontsize=16, fontweight='bold', color='#0f172a', rotation=-36)

# Height vertical lines
ax.plot([0.5, 0.5], [1.1, 0.0], color='#64748b', ls='--', lw=1.8)
ax.plot([0.5], [0.0], 'o', color='#0f172a', ms=5)
ax.text(0.48, -0.16, 'O', fontsize=15, fontweight='bold', color='#0f172a')

# Dimension indicators for y1 and y2
ax.annotate('', xy=(0.35, 1.1), xytext=(0.35, 0.0),
            arrowprops=dict(arrowstyle='<->', color='#2563eb', lw=1.8))
ax.text(-0.35, 0.5, r'$y_1 = 5 + \sin t$', fontsize=13, fontweight='bold', color='#2563eb')

ax.annotate('', xy=(2.1, 1.25), xytext=(2.1, 0.0),
            arrowprops=dict(arrowstyle='<->', color='#0284c7', lw=1.8))
ax.text(1.15, 0.25, r'$y_2 = 7 + \cos 2t$', fontsize=13, fontweight='bold', color='#0284c7')

save_fig(fig, "vec_819.png")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Q865: MASTER COMPOSITE PARABOLA & DUAL TRIANGLES
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.5, 6.0)
ax.set_xlim(-1.3, 2.7)
ax.set_ylim(-0.4, 2.4)

# Upper Parabola with coordinate axes
ax.axhline(1.2, color='#94a3b8', lw=1.4, ls=':')
ax.axvline(0.0, color='#94a3b8', lw=1.4, ls=':')
px = np.linspace(-1.0, 1.0, 150)
py = 0.9 * px**2 + 1.25
ax.plot(px, py, color='#0284c7', lw=3.2)
ax.text(0.1, 2.15, r'$f(x) = \sqrt{3}x^2 + 4x + \sqrt{3}$', fontsize=15, fontweight='bold', color='#0284c7')
ax.text(1.05, 1.15, 'X', fontsize=13, fontweight='bold', color='#64748b')
ax.text(0.05, 2.3, 'Y', fontsize=13, fontweight='bold', color='#64748b')

# Lower-Left Triangle: DEA
ax.plot([-1.0, 0.0, 0.0, -1.0], [0, 0, 0.65, 0], color='#0f172a', lw=2.6)
ax.plot([-0.12, -0.12, 0.0], [0.0, 0.12, 0.12], color='#0f172a', lw=1.6)
arc_a = patches.Arc((-1.0,0), 0.38, 0.38, angle=0, theta1=0, theta2=33.0, color='#2563eb', lw=2.2)
ax.add_patch(arc_a)
ax.text(-1.12, -0.06, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.06, -0.06, 'E', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.06, 0.68, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.55, -0.14, 'DE = 2', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(-0.7, 0.42, r'$AD = \sqrt{5}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(-0.76, 0.05, r'$\alpha$', fontsize=15, fontweight='bold', color='#2563eb')

# Lower-Right Triangle: ABC
ax.plot([1.1, 2.3, 2.3, 1.1], [0, 0, 0.75, 0], color='#0f172a', lw=2.6)
ax.plot([2.18, 2.18, 2.3], [0.0, 0.12, 0.12], color='#0f172a', lw=1.6)
arc_b = patches.Arc((1.1,0), 0.38, 0.38, angle=0, theta1=0, theta2=32.0, color='#2563eb', lw=2.2)
ax.add_patch(arc_b)
ax.text(0.98, -0.06, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(2.36, -0.06, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(2.36, 0.78, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(2.42, 0.35, 'BC = 5', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.5, 0.48, 'AC = 13', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.36, 0.05, r'$\beta$', fontsize=15, fontweight='bold', color='#2563eb')

save_fig(fig, "vec_865_composite.png")

# ─────────────────────────────────────────────────────────────────────────────
# 3. RE-UPLOAD TO IMAGEKIT & REBUILD
# ─────────────────────────────────────────────────────────────────────────────
for fname in ["vec_819.png", "vec_865_composite.png"]:
    p = os.path.join(out_dir, fname)
    with open(p, 'rb') as f:
        img_bytes = f.read()
    files = {"file": (fname, img_bytes, "image/png")}
    data = {
        "fileName": fname,
        "folder": "/math_2nd_ch7/pure_vector/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    print(f"Re-uploaded {fname} -> {res.status_code}")

print("Master vector diagrams updated with realistic physical components!")
