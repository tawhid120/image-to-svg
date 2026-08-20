# -*- coding: utf-8 -*-
"""
render_all_perfect_diagrams.py
==============================
Renders every single mathematical diagram with:
- Pure white high-DPI canvas (300 DPI)
- Generous padding so NO text or formula ever overflows or clips.
- Deep, crisp black lines (#0f172a) and vibrant blue geometric accents (#2563eb).
- Professional KaTeX / LaTeX mathematical typography.
- Standard first-quadrant counter-clockwise orientation for all trigonometry angles.
- Uploads to ImageKit under /math_2nd_ch7/recreated/
- Updates question bank JSON and HTML viewer.
"""

import os
import json
import re
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(HERE, "recreated_diagrams")
os.makedirs(out_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['mathtext.fontset'] = 'cm'

def setup_canvas(width=6.0, height=4.5):
    fig, ax = plt.subplots(figsize=(width, height), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    return fig, ax

def save_and_close(fig, path):
    plt.tight_layout(pad=1.5)
    fig.savefig(path, facecolor='#ffffff', edgecolor='none', bbox_inches='tight', pad_inches=0.2, dpi=300)
    plt.close(fig)

# ─────────────────────────────────────────────────────────────────────────────
# 1. GENERATE ALL 48 DIAGRAMS
# ─────────────────────────────────────────────────────────────────────────────

# --- Q863 ---
fig, ax = setup_canvas()
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.1)
# B(0,0), C(1,0), A(1, 0.8)
ax.plot([0, 1, 1, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5, solid_capstyle='round')
# Right angle at C
ax.plot([0.9, 0.9, 1.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
# Angle arc at B
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=38.66, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.82, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.42, 0.48, '1', fontsize=16, fontweight='bold', color='#2563eb')
ax.text(0.22, 0.05, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
ax.text(0.5, -0.1, 'BC', fontsize=13, color='#64748b')
ax.text(1.08, 0.4, 'AC', fontsize=13, color='#64748b')
save_and_close(fig, os.path.join(out_dir, "diag_863.png"))

# --- Q806 / Q829 / Q840 / Q864 / Q873 / Q886 ---
fig, ax = setup_canvas()
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.1)
ax.plot([0, 1, 1, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5, solid_capstyle='round')
ax.plot([0.9, 0.9, 1.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=38.66, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.82, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.05, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_806.png"))

# --- Q796 / Q855 ---
fig, ax = setup_canvas()
ax.set_xlim(-0.2, 1.25)
ax.set_ylim(-0.2, 1.1)
ax.plot([0, 1, 1, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5, solid_capstyle='round')
ax.plot([0.9, 0.9, 1.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=38.66, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.82, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.08, 0.38, '2', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.45, -0.1, r'$y = \sqrt{5}$', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.42, 0.48, 'x', fontsize=16, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_796.png"))

# --- Q775 / Q756 ---
fig, ax = setup_canvas()
ax.set_xlim(-0.2, 1.25)
ax.set_ylim(-0.2, 1.1)
ax.plot([0, 1, 1, 0], [0, 0, 0.75, 0], color='#0f172a', lw=2.5, solid_capstyle='round')
ax.plot([0.9, 0.9, 1.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=36.87, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.77, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.08, 0.35, '3', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.45, 0.45, '5', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.05, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_775.png"))

# --- Q794 / Q786 ---
fig, ax = setup_canvas(5.0, 5.0)
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.plot([0, 0.9, 0.9, 0], [0, 0, 1.0, 0], color='#0f172a', lw=2.5, solid_capstyle='round')
ax.plot([0.8, 0.8, 0.9], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=48.0, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(0.96, 0.5, '12', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.35, 0.6, '13', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.07, r'$\phi$', fontsize=17, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_794.png"))

# --- Q802 / Q882 / Q938 ---
fig, ax = setup_canvas(7.0, 4.0)
ax.set_xlim(-0.2, 2.5)
ax.set_ylim(-0.2, 1.1)
# Tri 1
ax.plot([0, 0.9, 0.9, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([0.8, 0.8, 0.9], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
ax.text(-0.06, -0.05, 'A', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.95, -0.05, 'B', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.95, 0.82, 'C', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.38, 0.48, 'r', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.45, -0.1, 'x', fontsize=15, fontweight='bold', color='#0f172a')
# Tri 2
ax.plot([1.4, 2.3, 2.3, 1.4], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([2.2, 2.2, 2.3], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
ax.text(1.34, -0.05, 'Q', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.35, -0.05, 'R', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.35, 0.82, 'P', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.78, 0.48, 'r', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(2.38, 0.38, 'y', fontsize=15, fontweight='bold', color='#0f172a')
save_and_close(fig, os.path.join(out_dir, "diag_802.png"))

# --- Q811 ---
fig, ax = setup_canvas(7.0, 4.5)
ax.set_xlim(-0.2, 2.4)
ax.set_ylim(-0.3, 1.3)
ax.plot([-0.1, 2.3], [0.9, 0.9], color='#0284c7', ls='--', lw=1.8)
ax.plot([-0.1, 2.3], [0.0, 0.0], color='#0284c7', ls='--', lw=1.8)
ax.plot([1.1, 1.1], [0.0, 0.9], color='#0f172a', lw=2.5)
ax.plot([1.1, 1.2, 1.2], [0.8, 0.8, 0.9], color='#0f172a', lw=1.5)
ax.plot([0.3, 1.1], [0.9, 0.0], color='#0f172a', lw=2.2)
ax.plot([1.9, 1.1], [0.9, 0.0], color='#0f172a', lw=2.2)
ax.text(0.25, 0.95, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.08, 0.95, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.9, 0.95, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.08, -0.12, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.65, 0.96, 'y', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.45, 0.96, 'x', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.15, 0.45, '1', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.9, 0.22, r'$\theta$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.22, 0.22, r'$3\theta$', fontsize=15, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_811.png"))

# --- Q815 ---
fig, ax = setup_canvas(6.0, 4.5)
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.plot([0.5, 0.0], [0.0, 0.9], color='#0f172a', lw=2.2)
ax.plot([0.5, 0.3], [0.0, 1.0], color='#0f172a', lw=2.2)
ax.plot([0.5, 0.7], [0.0, 1.0], color='#0f172a', lw=2.2)
ax.plot([0.5, 1.0], [0.0, 0.9], color='#0f172a', lw=2.2)
ax.text(0.48, -0.1, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.08, 0.92, 'E', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.27, 1.05, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.68, 1.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.92, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.32, 0.42, r'$\theta$', fontsize=14, fontweight='bold', color='#2563eb')
ax.text(0.48, 0.48, r'$\theta$', fontsize=14, fontweight='bold', color='#2563eb')
ax.text(0.64, 0.42, r'$\theta$', fontsize=14, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_815.png"))

# --- Q816 ---
fig, ax = setup_canvas(7.0, 4.5)
ax.set_xlim(-0.2, 2.4)
ax.set_ylim(-0.2, 1.2)
ax.plot([-0.1, 2.3], [0.0, 0.0], color='#0f172a', lw=2.5)
ax.plot([1.1, 0.3, 0.3], [0.0, 0.0, 0.8], color='#0f172a', lw=2.2)
ax.plot([1.1, 0.3], [0.0, 0.8], color='#0f172a', lw=2.2)
ax.plot([0.3, 0.4, 0.4], [0.1, 0.1, 0.0], color='#0f172a', lw=1.5)
ax.plot([1.1, 1.9, 1.9], [0.0, 0.0, 0.8], color='#0f172a', lw=2.2)
ax.plot([1.1, 1.9], [0.0, 0.8], color='#0f172a', lw=2.2)
ax.plot([1.9, 1.8, 1.8], [0.1, 0.1, 0.0], color='#0f172a', lw=1.5)
ax.plot([1.1, 1.1], [0.0, 0.9], color='#0284c7', ls='--', lw=1.8)
ax.text(1.08, -0.1, 'O', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.82, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.24, -0.1, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.95, 0.82, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.95, -0.1, 'D', fontsize=15, fontweight='bold', color='#0f172a')
save_and_close(fig, os.path.join(out_dir, "diag_816.png"))

# --- Q817 / Q874 ---
fig, ax = setup_canvas(6.5, 4.5)
ax.set_xlim(-0.2, 1.5)
ax.set_ylim(-0.2, 1.2)
ax.plot([0.6, 0.0, 1.3, 0.6], [1.0, 0.0, 0.0, 1.0], color='#0f172a', lw=2.5)
ax.plot([0.6, 0.6], [1.0, 0.0], color='#0f172a', lw=2.2)
ax.plot([0.6, 0.7, 0.7], [0.1, 0.1, 0.0], color='#0f172a', lw=1.5)
ax.plot([0.0, 0.6], [0.0, 0.5], color='#0f172a', ls='--', lw=1.8)
ax.plot([0.6, 0.95], [0.5, 0.0], color='#0f172a', ls='--', lw=1.8)
ax.text(0.58, 1.05, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.08, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.35, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.58, -0.1, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.58, '5', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.64, 0.6, '3', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.95, -0.1, '1', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.02, 0.35, r'$EC=\sqrt{5}$', fontsize=13, fontweight='bold', color='#0f172a')
ax.text(0.15, 0.06, r'$\beta$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.1, 0.06, r'$\alpha$', fontsize=15, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_817.png"))

# --- Q819 ---
fig, ax = setup_canvas(7.0, 4.5)
ax.set_xlim(-0.2, 2.4)
ax.set_ylim(-0.2, 1.3)
ax.plot([-0.1, 2.3], [0.0, 0.0], color='#334155', lw=2.2)
ax.plot([0.3, 1.9], [0.9, 0.0], color='#0f172a', lw=4.0, solid_capstyle='round')
ax.plot([0.3, 0.3], [0.9, 0.0], color='#0284c7', ls='--', lw=1.8)
ax.plot([1.3, 1.3], [0.35, 0.0], color='#0284c7', ls='--', lw=1.8)
ax.text(0.24, 0.95, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.95, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.28, 0.42, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.15, 0.45, r'$y_1 = 5 + \sin t$', fontsize=13, fontweight='bold', color='#0284c7')
ax.text(1.36, 0.2, r'$y_2 = 7 + \cos 2t$', fontsize=13, fontweight='bold', color='#0284c7')
ax.text(0.9, 0.6, '13 m', fontsize=15, fontweight='bold', color='#0f172a')
save_and_close(fig, os.path.join(out_dir, "diag_819.png"))

# --- Q846 ---
fig, ax = setup_canvas(7.0, 4.0)
ax.set_xlim(-0.2, 2.5)
ax.set_ylim(-0.2, 1.2)
# Tri 1
ax.plot([0, 0.9, 0.9, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([0.8, 0.8, 0.9], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=41.6, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'B', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.95, -0.05, 'C', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.95, 0.82, 'A', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.05, r'$\theta$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(0.35, -0.15, '১ম চিত্র', fontsize=13, fontweight='bold', color='#0284c7')
# Tri 2
ax.plot([1.4, 2.3, 1.9, 1.4], [0, 0, 0.9, 0], color='#0f172a', lw=2.5)
ax.text(1.34, -0.05, 'D', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.35, -0.05, 'E', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.88, 0.95, 'F', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.75, -0.15, '২য় চিত্র', fontsize=13, fontweight='bold', color='#0284c7')
save_and_close(fig, os.path.join(out_dir, "diag_846.png"))

# --- Q865 / Q867 / Q883 / Q884 / Q885 ---
fig, ax = setup_canvas(6.5, 4.5)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.3, 1.3)
import numpy as np
px = np.linspace(-1.0, 1.0, 200)
py = 1.0 * px**2 + 0.1
ax.plot(px, py, color='#0284c7', lw=2.8)
ax.plot([0, 0], [-0.2, 1.2], color='#0f172a', lw=2.0)
ax.plot([0, 0.6], [0.4, 0.4], color='#0f172a', lw=2.0)
ax.plot([0, -0.5], [0.7, 0.7], color='#0f172a', lw=2.0)
ax.plot([0, 0.1, 0.1], [0.5, 0.5, 0.4], color='#0f172a', lw=1.5)
ax.plot([0, -0.1, -0.1], [0.8, 0.8, 0.7], color='#0f172a', lw=1.5)
ax.text(0.3, 0.45, 'm', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(-0.3, 0.75, 'b', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.06, 0.25, 'a', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(-0.15, 0.95, 'n', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.15, 1.15, r'$f(x) = ax^2 + bx + c$', fontsize=14, fontweight='bold', color='#0284c7')
save_and_close(fig, os.path.join(out_dir, "diag_865.png"))

# --- Q868 ---
fig, ax = setup_canvas(6.5, 4.5)
ax.set_xlim(-0.2, 1.6)
ax.set_ylim(-0.2, 1.2)
ax.plot([0.5, 0.0, 0.9, 0.5], [0.9, 0.0, 0.0, 0.9], color='#0f172a', lw=2.5)
ax.plot([0.5, 0.9, 1.4, 0.5], [0.9, 0.0, 0.0, 0.9], color='#0f172a', lw=2.5)
ax.plot([0.5, 0.4, 0.4], [0.8, 0.8, 0.9], color='#0f172a', lw=1.5)
ax.plot([0.9, 0.9, 1.0], [0.1, 0.1, 0.0], color='#0f172a', lw=1.5)
ax.text(0.48, 0.95, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.08, -0.05, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.88, -0.1, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.45, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.5, '5', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.18, 0.5, '13', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.68, 0.45, '3', fontsize=14, fontweight='bold', color='#0f172a')
save_and_close(fig, os.path.join(out_dir, "diag_868.png"))

# --- Q872 / Q887 / Q892 / Q896 ---
fig, ax = setup_canvas(7.0, 4.5)
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.2, 1.2)
ax.plot([-0.1, 2.1], [0.0, 0.0], color='#0f172a', lw=2.5)
ax.plot([0.0, 0.0, 1.0], [0.9, 0.0, 0.0], color='#0f172a', lw=2.5)
ax.plot([0.0, 1.0], [0.9, 0.0], color='#0f172a', lw=2.5)
ax.plot([0.0, 0.1, 0.1], [0.1, 0.1, 0.0], color='#0f172a', lw=1.5)
ax.plot([2.0, 2.0, 1.0], [0.6, 0.0, 0.0], color='#0f172a', lw=2.5)
ax.plot([2.0, 1.0], [0.6, 0.0], color='#0f172a', lw=2.5)
ax.plot([2.0, 1.9, 1.9], [0.1, 0.1, 0.0], color='#0f172a', lw=1.5)
arc1 = patches.Arc((1.0, 0.0), 0.35, 0.35, angle=0, theta1=138, theta2=180, color='#2563eb', lw=2)
arc2 = patches.Arc((1.0, 0.0), 0.45, 0.45, angle=0, theta1=31, theta2=138, color='#2563eb', lw=2)
arc3 = patches.Arc((1.0, 0.0), 0.35, 0.35, angle=0, theta1=0, theta2=31, color='#2563eb', lw=2)
ax.add_patch(arc1); ax.add_patch(arc2); ax.add_patch(arc3)
ax.text(-0.12, 0.45, '4', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.45, -0.1, '1', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.08, 0.3, '1', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.45, -0.1, r'$\sqrt{3}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.72, 0.08, 'x', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(0.96, 0.28, 'z', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.22, 0.08, 'y', fontsize=15, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_872.png"))

# --- Q894 ---
fig, ax = setup_canvas(7.0, 4.0)
ax.set_xlim(-0.2, 2.5)
ax.set_ylim(-0.2, 1.2)
# Tri 1
ax.plot([0, 0.9, 0.9, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([0.8, 0.8, 0.9], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=41.6, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(0.35, 0.48, r'$\sqrt{3}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.45, -0.1, r'$\sqrt{2}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.05, r'$\alpha$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(0.35, -0.18, '১ম চিত্র', fontsize=13, fontweight='bold', color='#0284c7')
# Tri 2
ax.plot([1.4, 2.3, 2.3, 1.4], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([2.2, 2.2, 2.3], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc2 = patches.Arc((1.4,0), 0.35, 0.35, angle=0, theta1=0, theta2=41.6, color='#2563eb', lw=2)
ax.add_patch(arc2)
ax.text(1.72, 0.48, r'$2\sqrt{3}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.7, -0.1, r'$\sqrt{3}+\sqrt{2}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.62, 0.05, r'$\beta$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.75, -0.18, '২য় চিত্র', fontsize=13, fontweight='bold', color='#0284c7')
save_and_close(fig, os.path.join(out_dir, "diag_894.png"))

# --- Q901 ---
fig, ax = setup_canvas()
ax.set_xlim(-0.2, 1.25)
ax.set_ylim(-0.2, 1.1)
ax.plot([0, 1, 1, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([0.9, 0.9, 1.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=38.66, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.82, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.42, 0.48, '5', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.5, -0.1, '3', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.08, 0.38, 'x', fontsize=16, fontweight='bold', color='#2563eb')
ax.text(0.22, 0.05, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_901.png"))

# --- Q902 ---
fig, ax = setup_canvas()
ax.set_xlim(-0.2, 1.25)
ax.set_ylim(-0.2, 1.1)
ax.plot([0, 1, 1, 0], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([0.9, 0.9, 1.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=38.66, color='#2563eb', lw=2)
ax.add_patch(arc)
ax.text(-0.06, -0.05, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, -0.05, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.05, 0.82, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.42, 0.48, 'x', fontsize=16, fontweight='bold', color='#2563eb')
ax.text(0.5, -0.1, 'y', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.08, 0.38, '2', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.05, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_and_close(fig, os.path.join(out_dir, "diag_902.png"))

# --- Q567 / Q582 / Q583 / Q746: sin^-1 x graph ---
fig, ax = setup_canvas(5.5, 4.0)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.0, 2.0)
ax.axhline(0, color='#334155', lw=1.8)
ax.axvline(0, color='#334155', lw=1.8)
ax.plot([-1, 1], [np.pi/2, np.pi/2], color='#94a3b8', ls='--', lw=1.2)
ax.plot([-1, 1], [-np.pi/2, -np.pi/2], color='#94a3b8', ls='--', lw=1.2)
ax.plot([-1, -1], [-np.pi/2, np.pi/2], color='#94a3b8', ls='--', lw=1.2)
ax.plot([1, 1], [-np.pi/2, np.pi/2], color='#94a3b8', ls='--', lw=1.2)
y_vals = np.linspace(-np.pi/2, np.pi/2, 200)
x_vals = np.sin(y_vals)
ax.plot(x_vals, y_vals, color='#0284c7', lw=3.0)
ax.plot([-1, 1], [-np.pi/2, np.pi/2], 'o', color='#0284c7', ms=6)
ax.text(1.35, 0.1, 'X', fontsize=13, fontweight='bold', color='#334155')
ax.text(0.08, 1.85, 'Y', fontsize=13, fontweight='bold', color='#334155')
ax.text(1.05, -0.25, '1', fontsize=12, color='#64748b')
ax.text(-1.18, -0.25, '-1', fontsize=12, color='#64748b')
ax.text(0.08, np.pi/2 - 0.05, r'$\pi/2$', fontsize=12, color='#64748b')
ax.text(0.08, -np.pi/2 - 0.15, r'$-\pi/2$', fontsize=12, color='#64748b')
save_and_close(fig, os.path.join(out_dir, "diag_sin_inv.png"))

# --- Q574 / Q575 / Q622 / Q623 / Q747: cos^-1 x graph ---
fig, ax = setup_canvas(5.5, 4.0)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 3.5)
ax.axhline(0, color='#334155', lw=1.8)
ax.axvline(0, color='#334155', lw=1.8)
ax.plot([-1, 1], [np.pi, np.pi], color='#94a3b8', ls='--', lw=1.2)
ax.plot([-1, -1], [0, np.pi], color='#94a3b8', ls='--', lw=1.2)
ax.plot([1, 1], [0, np.pi], color='#94a3b8', ls='--', lw=1.2)
y_vals = np.linspace(0, np.pi, 200)
x_vals = np.cos(y_vals)
ax.plot(x_vals, y_vals, color='#0284c7', lw=3.0)
ax.plot([-1, 1], [np.pi, 0], 'o', color='#0284c7', ms=6)
ax.text(1.35, 0.1, 'X', fontsize=13, fontweight='bold', color='#334155')
ax.text(0.08, 3.35, 'Y', fontsize=13, fontweight='bold', color='#334155')
ax.text(1.05, -0.25, '1', fontsize=12, color='#64748b')
ax.text(-1.18, -0.25, '-1', fontsize=12, color='#64748b')
ax.text(0.08, np.pi - 0.05, r'$\pi$', fontsize=12, color='#64748b')
ax.text(0.08, np.pi/2 - 0.05, r'$\pi/2$', fontsize=12, color='#64748b')
save_and_close(fig, os.path.join(out_dir, "diag_cos_inv.png"))

# --- Q590 / Q591: tan^-1 x graph ---
fig, ax = setup_canvas(5.5, 4.0)
ax.set_xlim(-3.0, 3.0)
ax.set_ylim(-2.0, 2.0)
ax.axhline(0, color='#334155', lw=1.8)
ax.axvline(0, color='#334155', lw=1.8)
ax.plot([-3, 3], [np.pi/2, np.pi/2], color='#94a3b8', ls='--', lw=1.2)
ax.plot([-3, 3], [-np.pi/2, -np.pi/2], color='#94a3b8', ls='--', lw=1.2)
x_vals = np.linspace(-3.0, 3.0, 200)
y_vals = np.arctan(x_vals)
ax.plot(x_vals, y_vals, color='#0284c7', lw=3.0)
ax.text(2.75, 0.1, 'X', fontsize=13, fontweight='bold', color='#334155')
ax.text(0.08, 1.85, 'Y', fontsize=13, fontweight='bold', color='#334155')
ax.text(0.08, np.pi/2 - 0.05, r'$\pi/2$', fontsize=12, color='#64748b')
ax.text(0.08, -np.pi/2 - 0.15, r'$-\pi/2$', fontsize=12, color='#64748b')
save_and_close(fig, os.path.join(out_dir, "diag_tan_inv.png"))

# --- Q546 options (4 graphs) ---
# opt 1: cot^-1 x
fig, ax = setup_canvas(5.0, 3.5)
ax.set_xlim(-3.0, 3.0); ax.set_ylim(-0.5, 3.5)
ax.axhline(0, color='#334155', lw=1.8); ax.axvline(0, color='#334155', lw=1.8)
ax.plot([-3, 3], [np.pi, np.pi], color='#94a3b8', ls='--', lw=1.2)
x_vals = np.linspace(-3.0, 3.0, 200)
y_vals = np.pi/2 - np.arctan(x_vals)
ax.plot(x_vals, y_vals, color='#2563eb', lw=2.8)
ax.text(2.7, 0.1, 'x', fontsize=13, color='#334155'); ax.text(0.08, 3.3, 'y', fontsize=13, color='#334155')
save_and_close(fig, os.path.join(out_dir, "diag_546_1.png"))

# opt 2: tan^-1 x
fig, ax = setup_canvas(5.0, 3.5)
ax.set_xlim(-3.0, 3.0); ax.set_ylim(-2.0, 2.0)
ax.axhline(0, color='#334155', lw=1.8); ax.axvline(0, color='#334155', lw=1.8)
ax.plot([-3, 3], [np.pi/2, np.pi/2], color='#94a3b8', ls='--', lw=1.2)
ax.plot([-3, 3], [-np.pi/2, -np.pi/2], color='#94a3b8', ls='--', lw=1.2)
ax.plot(x_vals, np.arctan(x_vals), color='#2563eb', lw=2.8)
ax.text(2.7, 0.1, 'x', fontsize=13, color='#334155'); ax.text(0.08, 1.8, 'y', fontsize=13, color='#334155')
save_and_close(fig, os.path.join(out_dir, "diag_546_2.png"))

# opt 3: sin^-1 x
fig, ax = setup_canvas(5.0, 3.5)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-2.0, 2.0)
ax.axhline(0, color='#334155', lw=1.8); ax.axvline(0, color='#334155', lw=1.8)
y_s = np.linspace(-np.pi/2, np.pi/2, 200)
ax.plot(np.sin(y_s), y_s, color='#2563eb', lw=2.8)
ax.text(1.3, 0.1, 'x', fontsize=13, color='#334155'); ax.text(0.08, 1.8, 'y', fontsize=13, color='#334155')
save_and_close(fig, os.path.join(out_dir, "diag_546_3.png"))

# opt 4: cos^-1 x
fig, ax = setup_canvas(5.0, 3.5)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.5, 3.5)
ax.axhline(0, color='#334155', lw=1.8); ax.axvline(0, color='#334155', lw=1.8)
y_c = np.linspace(0, np.pi, 200)
ax.plot(np.cos(y_c), y_c, color='#2563eb', lw=2.8)
ax.text(1.3, 0.1, 'x', fontsize=13, color='#334155'); ax.text(0.08, 3.3, 'y', fontsize=13, color='#334155')
save_and_close(fig, os.path.join(out_dir, "diag_546_4.png"))

print(f"Generated all fresh, perfectly padded high-DPI diagrams in {out_dir}")

# ─────────────────────────────────────────────────────────────────────────────
# 2. UPLOAD TO IMAGEKIT
# ─────────────────────────────────────────────────────────────────────────────
uploaded_urls = {}
for fname in os.listdir(out_dir):
    if not fname.endswith('.png'):
        continue
    p = os.path.join(out_dir, fname)
    with open(p, 'rb') as f:
        img_bytes = f.read()
    files = {"file": (fname, img_bytes, "image/png")}
    data = {
        "fileName": fname,
        "folder": "/math_2nd_ch7/recreated/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    if res.ok:
        ik_url = res.json().get("url")
        uploaded_urls[fname] = ik_url
        print(f"  [UPLOADED] {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] {fname}: {res.text}")

# ─────────────────────────────────────────────────────────────────────────────
# 3. MAP EVERY QUESTION TO ITS RECREATED DIAGRAM URL
# ─────────────────────────────────────────────────────────────────────────────
MAP = {
    546: [uploaded_urls["diag_546_1.png"], uploaded_urls["diag_546_2.png"], uploaded_urls["diag_546_3.png"], uploaded_urls["diag_546_4.png"]],
    567: uploaded_urls["diag_sin_inv.png"],
    574: uploaded_urls["diag_cos_inv.png"],
    575: uploaded_urls["diag_cos_inv.png"],
    582: uploaded_urls["diag_sin_inv.png"],
    583: uploaded_urls["diag_sin_inv.png"],
    590: uploaded_urls["diag_tan_inv.png"],
    591: uploaded_urls["diag_tan_inv.png"],
    622: uploaded_urls["diag_cos_inv.png"],
    623: uploaded_urls["diag_cos_inv.png"],
    746: uploaded_urls["diag_sin_inv.png"],
    747: uploaded_urls["diag_cos_inv.png"],
    756: uploaded_urls["diag_775.png"],
    775: uploaded_urls["diag_775.png"],
    786: uploaded_urls["diag_794.png"],
    794: uploaded_urls["diag_794.png"],
    796: uploaded_urls["diag_796.png"],
    802: uploaded_urls["diag_802.png"],
    806: uploaded_urls["diag_806.png"],
    811: uploaded_urls["diag_811.png"],
    815: uploaded_urls["diag_815.png"],
    816: uploaded_urls["diag_816.png"],
    817: uploaded_urls["diag_817.png"],
    819: uploaded_urls["diag_819.png"],
    829: uploaded_urls["diag_806.png"],
    840: uploaded_urls["diag_806.png"],
    846: uploaded_urls["diag_846.png"],
    855: uploaded_urls["diag_796.png"],
    863: uploaded_urls["diag_863.png"],
    864: uploaded_urls["diag_806.png"],
    865: uploaded_urls["diag_865.png"],
    867: uploaded_urls["diag_865.png"],
    868: uploaded_urls["diag_868.png"],
    872: uploaded_urls["diag_872.png"],
    873: uploaded_urls["diag_806.png"],
    874: uploaded_urls["diag_817.png"],
    882: uploaded_urls["diag_802.png"],
    883: uploaded_urls["diag_865.png"],
    884: uploaded_urls["diag_865.png"],
    885: uploaded_urls["diag_865.png"],
    886: uploaded_urls["diag_806.png"],
    887: uploaded_urls["diag_872.png"],
    892: uploaded_urls["diag_872.png"],
    894: uploaded_urls["diag_894.png"],
    896: uploaded_urls["diag_872.png"],
    901: uploaded_urls["diag_901.png"],
    902: uploaded_urls["diag_902.png"],
    938: uploaded_urls["diag_802.png"],
}

# ─────────────────────────────────────────────────────────────────────────────
# 4. UPDATE RAW JSON & PROCESSED_QUESTIONS.JSON
# ─────────────────────────────────────────────────────────────────────────────
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

# Update processed_questions.json directly
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

print("\nSuccessfully updated all questions with 100% freshly rendered, perfectly padded diagrams!")
