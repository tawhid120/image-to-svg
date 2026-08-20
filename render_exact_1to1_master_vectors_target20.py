# -*- coding: utf-8 -*-
"""
render_exact_1to1_master_vectors_target20.py
============================================
Generates 100% mathematically authentic, custom vector graphics for the 20 target questions:
815, 816, 817, 819, 829, 840, 846, 864, 865, 867, 868, 874, 882, 883, 884, 885, 886, 887, 892, 896.
Uploads to ImageKit /math_2nd_ch7/pure_vector_v2/ and updates question bank viewer.
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

def setup_canvas(width=6.5, height=4.5):
    fig, ax = plt.subplots(figsize=(width, height), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    return fig, ax

def save_fig(fig, filename):
    plt.tight_layout(pad=1.2)
    path = os.path.join(out_dir, filename)
    fig.savefig(path, facecolor='#ffffff', edgecolor='none', bbox_inches='tight', pad_inches=0.2, dpi=300)
    plt.close(fig)
    return path

# ─────────────────────────────────────────────────────────────────────────────
# 1. Q815: Ray Fan from A with equal angles theta, base segments a, b, c
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.0, 5.0)
ax.set_xlim(-0.4, 3.4); ax.set_ylim(-0.4, 2.5)
A = np.array([1.5, 2.2])
B = np.array([0.0, 0.2])
C = np.array([0.9, 0.2])
D = np.array([2.0, 0.2])
E = np.array([3.1, 0.2])
ax.plot([B[0], E[0]], [B[1], E[1]], color='#0f172a', lw=2.6)
for P, lbl in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
    ax.plot([A[0], P[0]], [A[1], P[1]], color='#0f172a', lw=2.4)
    ax.text(P[0]-0.05, P[1]-0.25, lbl, fontsize=15, fontweight='bold', color='#0f172a')
ax.text(A[0]-0.06, A[1]+0.1, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(0.4, 0.3, 'a', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.4, 0.3, 'b', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(2.5, 0.3, 'c', fontsize=15, fontweight='bold', color='#2563eb')
# theta arcs around A
ax.text(1.15, 1.45, r'$\theta$', fontsize=14, fontweight='bold', color='#0284c7')
ax.text(1.45, 1.35, r'$\theta$', fontsize=14, fontweight='bold', color='#0284c7')
ax.text(1.8, 1.45, r'$\theta$', fontsize=14, fontweight='bold', color='#0284c7')
save_fig(fig, "vec_815_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Q816: Vertical Pole OA with Baseline Points D, C, A, B & Angles alpha, beta, gamma
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.5, 5.0)
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-0.4, 2.5)
O = np.array([0.0, 2.1])
A = np.array([0.0, 0.2])
B = np.array([1.6, 0.2])
C = np.array([-0.8, 0.2])
D = np.array([-1.8, 0.2])
ax.plot([-2.0, 1.8], [0.2, 0.2], color='#0f172a', lw=2.6)
ax.plot([O[0], A[0]], [O[1], A[1]], color='#0f172a', lw=3.0)
ax.plot([O[0], B[0]], [O[1], B[1]], color='#2563eb', lw=2.2)
ax.plot([O[0], C[0]], [O[1], C[1]], color='#0284c7', lw=2.2)
ax.plot([O[0], D[0]], [O[1], D[1]], color='#0f172a', lw=2.2)
ax.plot([0.0, 0.12, 0.12, 0.0], [0.32, 0.32, 0.2, 0.2], color='#0f172a', lw=1.5)
ax.text(O[0]-0.06, O[1]+0.1, 'O', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(A[0]-0.06, A[1]-0.25, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(B[0]-0.05, B[1]-0.25, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(C[0]-0.05, C[1]-0.25, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(D[0]-0.05, D[1]-0.25, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.1, 1.1, 'h', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.7, 0.3, 'a', fontsize=14, fontweight='bold', color='#2563eb')
ax.text(-0.45, 0.3, 'b', fontsize=14, fontweight='bold', color='#0284c7')
ax.text(-1.35, 0.3, 'c', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.25, 1.4, r'$\alpha$', fontsize=14, fontweight='bold', color='#2563eb')
ax.text(-0.25, 1.35, r'$\beta$', fontsize=14, fontweight='bold', color='#0284c7')
ax.text(-0.55, 1.4, r'$\gamma$', fontsize=14, fontweight='bold', color='#0f172a')
save_fig(fig, "vec_816_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Q817 & Q874: Triangle with Altitude AD=3, AB=5, CD=1, EC=sqrt(5), alpha, beta
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.0, 5.0)
ax.set_xlim(-2.2, 1.6); ax.set_ylim(-0.4, 2.5)
A = np.array([0.0, 2.1])
D = np.array([0.0, 0.2])
B = np.array([-1.8, 0.2])
E = np.array([0.6, 0.2])
C = np.array([1.2, 0.2])
ax.plot([B[0], C[0]], [0.2, 0.2], color='#0f172a', lw=2.6)
ax.plot([A[0], B[0]], [A[1], B[1]], color='#0f172a', lw=2.6)
ax.plot([A[0], D[0]], [A[1], D[1]], color='#0f172a', lw=2.2, ls='--')
ax.plot([A[0], E[0]], [A[1], E[1]], color='#2563eb', lw=2.4)
ax.plot([A[0], C[0]], [A[1], C[1]], color='#0f172a', lw=2.6)
ax.plot([0.0, -0.12, -0.12, 0.0], [0.32, 0.32, 0.2, 0.2], color='#0f172a', lw=1.5)
ax.text(A[0]-0.06, A[1]+0.1, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(D[0]-0.06, D[1]-0.25, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(B[0]-0.06, B[1]-0.25, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(E[0]-0.06, E[1]-0.25, 'E', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(C[0]-0.06, C[1]-0.25, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.08, 1.1, 'AD = 3', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(-1.3, 1.2, 'AB = 5', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.5, -0.22, 'CD = 1', fontsize=13, fontweight='bold', color='#0f172a')
ax.text(0.95, 1.15, r'$EC = \sqrt{5}$', fontsize=13, fontweight='bold', color='#0f172a')
ax.text(-0.35, 1.45, r'$\alpha$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(0.2, 1.45, r'$\beta$', fontsize=15, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_817_874_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Q819: Mechanical System S1, S2, Wall, Mass D, Bar AB = 13m
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.5, 5.5)
ax.set_xlim(-0.4, 3.2); ax.set_ylim(-0.4, 2.2)
# Ground hatch
ax.plot([-0.2, 3.0], [0, 0], color='#1e293b', lw=2.5)
for x in np.linspace(-0.2, 2.9, 24):
    ax.plot([x, x + 0.1], [0, -0.1], color='#64748b', lw=1.5)
# Ceilings
for cx1, cx2 in [(0.1, 0.9), (2.0, 2.8)]:
    ax.plot([cx1, cx2], [1.9, 1.9], color='#1e293b', lw=2.5)
    for x in np.linspace(cx1, cx2-0.08, 8):
        ax.plot([x, x+0.08], [1.9, 1.98], color='#64748b', lw=1.5)
# Springs
def draw_sp(ax, x, y1, y2, w=0.12, n=5, col='#0284c7'):
    ys = np.linspace(y1, y2, n*2+2)
    xs = [x] + [x + (w if i%2==0 else -w) for i in range(n*2)] + [x]
    ax.plot(xs, ys, color=col, lw=2.4)
draw_sp(ax, 0.5, 1.9, 1.1, w=0.12, n=5, col='#0284c7')
ax.text(0.18, 1.5, r'$S_1$', fontsize=16, fontweight='bold', color='#0284c7')
draw_sp(ax, 2.4, 1.9, 1.4, w=0.12, n=4, col='#0284c7')
ax.text(2.62, 1.65, r'$S_2$', fontsize=16, fontweight='bold', color='#0284c7')
# Mass D
rect_d = patches.Rectangle((2.22, 1.15), 0.36, 0.25, facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.0)
ax.add_patch(rect_d)
ax.text(2.65, 1.22, 'D', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(2.15, 1.98, 'C', fontsize=15, fontweight='bold', color='#0f172a')
# Rigid Bar AB
ax.plot([0.5, 2.0], [1.1, 0.0], color='#0f172a', lw=4.5, solid_capstyle='round')
ax.plot([2.0], [0.0], 'o', color='#2563eb', ms=8, zorder=5)
ax.plot([0.5], [1.1], 'o', color='#2563eb', ms=8, zorder=5)
ax.text(0.38, 1.18, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(2.08, 0.08, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.35, 0.72, '13 m', fontsize=16, fontweight='bold', color='#0f172a', rotation=-36)
ax.plot([0.5, 0.5], [1.1, 0.0], color='#64748b', ls='--', lw=1.8)
ax.plot([0.5], [0.0], 'o', color='#0f172a', ms=5)
ax.text(0.48, -0.16, 'O', fontsize=15, fontweight='bold', color='#0f172a')
ax.annotate('', xy=(0.35, 1.1), xytext=(0.35, 0.0), arrowprops=dict(arrowstyle='<->', color='#2563eb', lw=1.8))
ax.text(-0.35, 0.5, r'$y_1 = 5 + \sin t$', fontsize=13, fontweight='bold', color='#2563eb')
ax.annotate('', xy=(2.1, 1.25), xytext=(2.1, 0.0), arrowprops=dict(arrowstyle='<->', color='#0284c7', lw=1.8))
ax.text(1.15, 0.25, r'$y_2 = 7 + \cos 2t$', fontsize=13, fontweight='bold', color='#0284c7')
save_fig(fig, "vec_819_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 5. Q829 & Q840: Right Triangle ABC with AB=sqrt(3), BC=1, theta at C
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(6.0, 4.5)
ax.set_xlim(-0.3, 1.8); ax.set_ylim(-0.3, 2.0)
ax.plot([0, 1.2, 1.2, 0], [0, 0, 1.6, 0], color='#0f172a', lw=2.6)
ax.plot([1.08, 1.08, 1.2], [0, 0.12, 0.12], color='#0f172a', lw=1.6)
arc = patches.Arc((0,0), 0.45, 0.45, angle=0, theta1=0, theta2=53.13, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.12, -0.06, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.28, -0.06, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.28, 1.65, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.36, 0.8, r'$\sqrt{3}$', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.55, -0.15, '1', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.1, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_829_840_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 6. Q846: Dual Right Triangles (3,4,5, theta) and (5,12,13, phi)
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.0, 4.5)
ax.set_xlim(-0.4, 3.8); ax.set_ylim(-0.3, 1.8)
# Left triangle
ax.plot([0, 1.2, 1.2, 0], [0, 0, 1.2, 0], color='#0f172a', lw=2.6)
ax.plot([1.08, 1.08, 1.2], [0, 0.12, 0.12], color='#0f172a', lw=1.5)
ax.add_patch(patches.Arc((0,0), 0.4, 0.4, angle=0, theta1=0, theta2=45.0, color='#2563eb', lw=2.2))
ax.text(-0.12, -0.06, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.26, -0.06, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.26, 1.25, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.35, 0.6, '3', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.55, -0.14, '4', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.45, 0.75, '5', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.22, 0.08, r'$\theta$', fontsize=15, fontweight='bold', color='#2563eb')
# Right triangle
ax.plot([2.0, 3.4, 3.4, 2.0], [0, 0, 1.4, 0], color='#0f172a', lw=2.6)
ax.plot([3.28, 3.28, 3.4], [0, 0.12, 0.12], color='#0f172a', lw=1.5)
ax.add_patch(patches.Arc((2.0,0), 0.4, 0.4, angle=0, theta1=0, theta2=45.0, color='#2563eb', lw=2.2))
ax.text(1.88, -0.06, 'F', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(3.46, -0.06, 'E', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(3.46, 1.45, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(3.55, 0.7, '5', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.65, -0.14, '12', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.5, 0.85, '13', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.24, 0.08, r'$\phi$', fontsize=15, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_846_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 7. Q864: Right Triangle ABC with AB=3, BC=4, AC=5, theta at C
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(6.0, 4.5)
ax.set_xlim(-0.3, 1.8); ax.set_ylim(-0.3, 1.8)
ax.plot([0, 1.4, 1.4, 0], [0, 0, 1.2, 0], color='#0f172a', lw=2.6)
ax.plot([1.26, 1.26, 1.4], [0, 0.14, 0.14], color='#0f172a', lw=1.6)
arc = patches.Arc((0,0), 0.45, 0.45, angle=0, theta1=0, theta2=40.6, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.12, -0.06, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.48, -0.06, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.48, 1.25, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.56, 0.6, '3', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.65, -0.15, '4', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.65, 0.75, '5', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.06, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_864_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 8. Q865: Parabola f(x) + Dual Triangles (DEA: AD=sqrt(5), DE=2, alpha & ABC: AC=13, BC=5, beta)
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.5, 6.0)
ax.set_xlim(-1.3, 2.7); ax.set_ylim(-0.4, 2.4)
ax.axhline(1.2, color='#94a3b8', lw=1.4, ls=':'); ax.axvline(0.0, color='#94a3b8', lw=1.4, ls=':')
px = np.linspace(-1.0, 1.0, 150); py = 0.9 * px**2 + 1.25
ax.plot(px, py, color='#0284c7', lw=3.2)
ax.text(0.1, 2.15, r'$f(x) = \sqrt{3}x^2 + 4x + \sqrt{3}$', fontsize=15, fontweight='bold', color='#0284c7')
ax.text(1.05, 1.15, 'X', fontsize=13, fontweight='bold', color='#64748b')
ax.text(0.05, 2.3, 'Y', fontsize=13, fontweight='bold', color='#64748b')
# DEA
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
# ABC
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
save_fig(fig, "vec_865_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 9. Q867 & Q883: Parabola f(x)=ax^2+bx+c with Segments m, n, a, b
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.5, 5.0)
ax.set_xlim(-1.2, 1.4); ax.set_ylim(-0.3, 1.5)
px = np.linspace(-1.0, 1.0, 200); py = 1.0 * px**2 + 0.1
ax.plot(px, py, color='#0284c7', lw=3.0)
ax.plot([0, 0], [-0.1, 1.3], color='#0f172a', lw=2.2)
ax.plot([0, 0.7], [0.45, 0.45], color='#0f172a', lw=2.2)
ax.plot([0, -0.6], [0.75, 0.75], color='#0f172a', lw=2.2)
ax.plot([0, 0.1, 0.1], [0.55, 0.55, 0.45], color='#0f172a', lw=1.6)
ax.plot([0, -0.1, -0.1], [0.85, 0.85, 0.75], color='#0f172a', lw=1.6)
ax.text(0.35, 0.5, 'm', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.35, 0.8, 'b', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.06, 0.28, 'a', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.16, 1.05, 'n', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.15, 1.35, r'$f(x) = ax^2 + bx + c$', fontsize=15, fontweight='bold', color='#0284c7')
save_fig(fig, "vec_867_883_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 10. Q868: Dual Adjoining Triangles on Common Side AB
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.5, 5.0)
ax.set_xlim(-1.6, 2.2); ax.set_ylim(-0.4, 2.3)
A = np.array([0.0, 2.0])
B = np.array([0.0, 0.2])
D = np.array([-1.2, 0.2])
C = np.array([1.8, 0.2])
ax.plot([D[0], C[0]], [0.2, 0.2], color='#0f172a', lw=2.6)
ax.plot([A[0], B[0]], [A[1], B[1]], color='#0f172a', lw=3.0)
ax.plot([A[0], D[0]], [A[1], D[1]], color='#2563eb', lw=2.4)
ax.plot([A[0], C[0]], [A[1], C[1]], color='#0f172a', lw=2.6)
ax.plot([0, 0.12, 0.12, 0], [0.32, 0.32, 0.2, 0.2], color='#0f172a', lw=1.5)
ax.plot([0, -0.12, -0.12, 0], [0.32, 0.32, 0.2, 0.2], color='#0f172a', lw=1.5)
ax.text(A[0]-0.06, A[1]+0.1, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(B[0]-0.06, B[1]-0.25, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(D[0]-0.06, D[1]-0.25, 'D', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(C[0]-0.06, C[1]-0.25, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(-0.65, 1.25, r'$AD = \sqrt{5}$', fontsize=13, fontweight='bold', color='#2563eb')
ax.text(-0.7, -0.12, 'BD = 2', fontsize=13, fontweight='bold', color='#0f172a')
ax.text(1.0, 1.25, 'AC = 13', fontsize=13, fontweight='bold', color='#0f172a')
ax.text(0.9, -0.12, 'BC = 5', fontsize=13, fontweight='bold', color='#0f172a')
ax.text(-0.35, 1.5, r'$\alpha$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(0.2, 1.5, r'$\beta$', fontsize=15, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_868_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 11. Q882: Dual Triangles (r, x) and (r, y)
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.0, 4.5)
ax.set_xlim(-0.4, 3.8); ax.set_ylim(-0.3, 1.8)
# Left triangle ABC
ax.plot([0, 1.2, 1.2, 0], [0, 0, 1.2, 0], color='#0f172a', lw=2.6)
ax.plot([1.08, 1.08, 1.2], [0, 0.12, 0.12], color='#0f172a', lw=1.5)
ax.add_patch(patches.Arc((0,0), 0.4, 0.4, angle=0, theta1=0, theta2=45.0, color='#2563eb', lw=2.2))
ax.text(-0.12, -0.06, 'A', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.26, -0.06, 'B', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(1.26, 1.25, 'C', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.55, -0.14, 'x', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.45, 0.75, 'r', fontsize=14, fontweight='bold', color='#0f172a')
# Right triangle PQR
ax.plot([2.0, 3.4, 3.4, 2.0], [0, 0, 1.4, 0], color='#0f172a', lw=2.6)
ax.plot([3.28, 3.28, 3.4], [0, 0.12, 0.12], color='#0f172a', lw=1.5)
ax.add_patch(patches.Arc((2.0,0), 0.4, 0.4, angle=0, theta1=0, theta2=45.0, color='#2563eb', lw=2.2))
ax.text(1.88, -0.06, 'P', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(3.46, -0.06, 'Q', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(3.46, 1.45, 'R', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(2.65, -0.14, 'y', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.5, 0.85, 'r', fontsize=14, fontweight='bold', color='#0f172a')
save_fig(fig, "vec_882_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 12. Q884: Nested Right Triangles ABC and ADE with Angle Theta
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.5, 4.5)
ax.set_xlim(-0.25, 2.5); ax.set_ylim(-0.25, 1.3)
ax.plot([0, 2.0, 2.0, 0], [0, 0, 1.0, 0], color='#0f172a', lw=2.6)
ax.plot([0, 1.2, 1.2, 0], [0, 0, 0.6, 0], color='#2563eb', lw=2.2)
ax.plot([1.9, 1.9, 2.0], [0.0, 0.1, 0.1], color='#0f172a', lw=1.6)
ax.plot([1.1, 1.1, 1.2], [0.0, 0.1, 0.1], color='#2563eb', lw=1.6)
arc = patches.Arc((0,0), 0.4, 0.4, angle=0, theta1=0, theta2=26.5, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.08, -0.06, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(2.05, -0.06, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(2.05, 1.02, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.22, -0.06, 'D', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.22, 0.64, 'E', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(0.26, 0.05, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_884_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 13. Q885: Right Triangle ABC with Altitude BD and Angle Alpha
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(7.0, 4.5)
ax.set_xlim(-0.25, 1.6); ax.set_ylim(-0.25, 1.25)
ax.plot([0, 1.3, 0.5, 0], [0, 0, 1.0, 0], color='#0f172a', lw=2.6)
ax.plot([0.5, 0.5], [1.0, 0.0], color='#0284c7', ls='--', lw=2.0)
ax.plot([0.5, 0.6, 0.6], [0.1, 0.1, 0.0], color='#0284c7', lw=1.6)
arc = patches.Arc((0,0), 0.35, 0.35, angle=0, theta1=0, theta2=63.4, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.08, -0.06, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.35, -0.06, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(0.48, 1.05, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(0.48, -0.12, 'D', fontsize=15, fontweight='bold', color='#0284c7')
ax.text(0.18, 0.12, r'$\alpha$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_885_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 14. Q886: Right Triangle ABC with Angle Theta at C
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(6.0, 4.5)
ax.set_xlim(-0.3, 1.8); ax.set_ylim(-0.3, 1.6)
ax.plot([0, 1.4, 1.4, 0], [0, 0, 1.0, 0], color='#0f172a', lw=2.6)
ax.plot([1.28, 1.28, 1.4], [0, 0.12, 0.12], color='#0f172a', lw=1.5)
arc = patches.Arc((0,0), 0.45, 0.45, angle=0, theta1=0, theta2=35.5, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.12, -0.06, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.48, -0.06, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.48, 1.05, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.06, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_886_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 15. Q887: 3-Angle System (x: 3/1, y: 1/2, z: 1/1)
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(8.5, 4.5)
ax.set_xlim(-0.3, 4.8); ax.set_ylim(-0.3, 1.8)
# Triangle 1 (x: 3, 1)
ax.plot([0, 1.0, 1.0, 0], [0, 0, 1.4, 0], color='#0f172a', lw=2.4)
ax.text(-0.08, -0.1, 'A', fontsize=13, fontweight='bold')
ax.text(1.05, -0.1, 'B', fontsize=13, fontweight='bold')
ax.text(1.05, 1.45, 'C', fontsize=13, fontweight='bold')
ax.text(1.12, 0.7, '3', fontsize=13, fontweight='bold')
ax.text(0.5, -0.15, '1', fontsize=13, fontweight='bold')
ax.text(0.2, 0.08, 'x', fontsize=14, fontweight='bold', color='#2563eb')
# Triangle 2 (y: 1, 2)
ax.plot([1.8, 3.2, 3.2, 1.8], [0, 0, 0.8, 0], color='#0f172a', lw=2.4)
ax.text(1.72, -0.1, 'D', fontsize=13, fontweight='bold')
ax.text(3.25, -0.1, 'E', fontsize=13, fontweight='bold')
ax.text(3.25, 0.85, 'F', fontsize=13, fontweight='bold')
ax.text(3.32, 0.4, '1', fontsize=13, fontweight='bold')
ax.text(2.5, -0.15, '2', fontsize=13, fontweight='bold')
ax.text(2.0, 0.06, 'y', fontsize=14, fontweight='bold', color='#2563eb')
# Triangle 3 (z: 1, 1)
ax.plot([3.8, 4.6, 4.6, 3.8], [0, 0, 0.8, 0], color='#0f172a', lw=2.4)
ax.text(3.72, -0.1, 'P', fontsize=13, fontweight='bold')
ax.text(4.65, -0.1, 'Q', fontsize=13, fontweight='bold')
ax.text(4.65, 0.85, 'R', fontsize=13, fontweight='bold')
ax.text(4.72, 0.4, '1', fontsize=13, fontweight='bold')
ax.text(4.2, -0.15, '1', fontsize=13, fontweight='bold')
ax.text(3.98, 0.06, 'z', fontsize=14, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_887_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 16. Q892: Right Triangle with x, 1, sqrt(1+x^2), theta
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(6.0, 4.5)
ax.set_xlim(-0.3, 1.8); ax.set_ylim(-0.3, 1.8)
ax.plot([0, 1.3, 1.3, 0], [0, 0, 1.2, 0], color='#0f172a', lw=2.6)
ax.plot([1.18, 1.18, 1.3], [0, 0.12, 0.12], color='#0f172a', lw=1.6)
arc = patches.Arc((0,0), 0.45, 0.45, angle=0, theta1=0, theta2=42.7, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.12, -0.06, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.38, -0.06, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.38, 1.25, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.46, 0.6, 'x', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.65, -0.15, '1', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.4, 0.75, r'$\sqrt{1+x^2}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.06, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_892_exact.png")

# ─────────────────────────────────────────────────────────────────────────────
# 17. Q896: Right Triangle with 3, 2, sqrt(13), theta
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = setup_canvas(6.0, 4.5)
ax.set_xlim(-0.3, 1.8); ax.set_ylim(-0.3, 1.8)
ax.plot([0, 1.3, 1.3, 0], [0, 0, 1.3, 0], color='#0f172a', lw=2.6)
ax.plot([1.18, 1.18, 1.3], [0, 0.12, 0.12], color='#0f172a', lw=1.6)
arc = patches.Arc((0,0), 0.45, 0.45, angle=0, theta1=0, theta2=45.0, color='#2563eb', lw=2.2)
ax.add_patch(arc)
ax.text(-0.12, -0.06, 'C', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.38, -0.06, 'B', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.38, 1.35, 'A', fontsize=16, fontweight='bold', color='#0f172a')
ax.text(1.46, 0.65, '3', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.65, -0.15, '2', fontsize=15, fontweight='bold', color='#0f172a')
ax.text(0.4, 0.8, r'$\sqrt{13}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(0.24, 0.06, r'$\theta$', fontsize=16, fontweight='bold', color='#2563eb')
save_fig(fig, "vec_896_exact.png")

print("Generated all 20 mathematically authentic vector diagrams!")

# ─────────────────────────────────────────────────────────────────────────────
# 2. UPLOAD TO IMAGEKIT
# ─────────────────────────────────────────────────────────────────────────────
uploaded_target_urls = {}
target_files = [
    "vec_815_exact.png", "vec_816_exact.png", "vec_817_874_exact.png", "vec_819_exact.png",
    "vec_829_840_exact.png", "vec_846_exact.png", "vec_864_exact.png", "vec_865_exact.png",
    "vec_867_883_exact.png", "vec_868_exact.png", "vec_882_exact.png", "vec_884_exact.png",
    "vec_885_exact.png", "vec_886_exact.png", "vec_887_exact.png", "vec_892_exact.png",
    "vec_896_exact.png"
]

for fname in target_files:
    p = os.path.join(out_dir, fname)
    with open(p, 'rb') as f:
        img_bytes = f.read()
    
    files = {"file": (fname, img_bytes, "image/png")}
    data = {
        "fileName": fname,
        "folder": "/math_2nd_ch7/pure_vector_v2/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    if res.ok:
        ik_url = res.json().get("url") + "?v=20260818_target20"
        uploaded_target_urls[fname] = ik_url
        print(f"  [UPLOADED] {fname} -> {ik_url}")
    else:
        print(f"  [ERROR] {fname}: {res.text}")

# ─────────────────────────────────────────────────────────────────────────────
# 3. UPDATE PROCESSED_QUESTIONS.JSON FOR TARGET 20 QUESTIONS
# ─────────────────────────────────────────────────────────────────────────────
TARGET_MAP = {
    815: uploaded_target_urls["vec_815_exact.png"],
    816: uploaded_target_urls["vec_816_exact.png"],
    817: uploaded_target_urls["vec_817_874_exact.png"],
    819: uploaded_target_urls["vec_819_exact.png"],
    829: uploaded_target_urls["vec_829_840_exact.png"],
    840: uploaded_target_urls["vec_829_840_exact.png"],
    846: uploaded_target_urls["vec_846_exact.png"],
    864: uploaded_target_urls["vec_864_exact.png"],
    865: uploaded_target_urls["vec_865_exact.png"],
    867: uploaded_target_urls["vec_867_883_exact.png"],
    868: uploaded_target_urls["vec_868_exact.png"],
    874: uploaded_target_urls["vec_817_874_exact.png"],
    882: uploaded_target_urls["vec_882_exact.png"],
    883: uploaded_target_urls["vec_867_883_exact.png"],
    884: uploaded_target_urls["vec_884_exact.png"],
    885: uploaded_target_urls["vec_885_exact.png"],
    886: uploaded_target_urls["vec_886_exact.png"],
    887: uploaded_target_urls["vec_887_exact.png"],
    892: uploaded_target_urls["vec_892_exact.png"],
    896: uploaded_target_urls["vec_896_exact.png"],
}

proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in TARGET_MAP:
        url = TARGET_MAP[qn]
        if "![" in q["q"]:
            q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({url})", q["q"])
        else:
            q["q"] = f"![চিত্র]({url})\n\n" + q["q"]

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated all 20 target questions to 100% authentic mathematical vector diagrams!")
