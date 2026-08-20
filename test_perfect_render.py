import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def test_render():
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    # Parabola: y = a_p * x^2
    a_p = 0.38
    x_min, x_max = -2.7, 2.75
    xs = np.linspace(x_min, x_max, 250)
    ys = a_p * (xs ** 2)

    # Key points in world space
    x_R = 2.45
    y_R = a_p * (x_R ** 2)  # ~2.281

    x_L = -1.95
    y_L = a_p * (x_L ** 2)  # ~1.445

    V = (0.0, 0.0)
    P_top = (0.0, y_R)
    P_mid = (0.0, y_L)

    slope_line = y_R / x_R  # ~0.931
    x_ext = -1.9
    y_ext = slope_line * x_ext

    x_drop = -0.75
    P_drop_top = (x_drop, y_L)
    m_left_chord = y_L / x_L
    P_drop_bot = (x_drop, m_left_chord * x_drop)

    # 1. Plot Parabola
    ax.plot(xs, ys, 'k-', lw=2.2, zorder=2)
    # Outward arrowheads on parabola tips
    ax.annotate('', xy=(xs[0], ys[0]), xytext=(xs[3], ys[3]),
                arrowprops=dict(arrowstyle='-|>', lw=2.0, color='black', mutation_scale=16))
    ax.annotate('', xy=(xs[-1], ys[-1]), xytext=(xs[-4], ys[-4]),
                arrowprops=dict(arrowstyle='-|>', lw=2.0, color='black', mutation_scale=16))

    # 2. Straight Secant Line (from bottom-left extension through vertex to right branch)
    ax.plot([x_ext, x_R], [y_ext, y_R], 'k-', lw=2.0, zorder=2)

    # 3. Central Vertical Stem (from top right corner down to vertex)
    ax.plot([0, 0], [y_R, 0], 'k-', lw=1.8, zorder=2)

    # 4. Top Horizontal Line (length m)
    ax.plot([0, x_R], [y_R, y_R], 'k-', lw=1.8, zorder=2)

    # 5. Left Horizontal Line (length b)
    ax.plot([x_L, 0], [y_L, y_L], 'k-', lw=1.8, zorder=2)

    # 6. Left Chord (from P_L to vertex)
    ax.plot([x_L, 0], [y_L, 0], 'k-', lw=1.8, zorder=2)

    # 7. Left Vertical Drop
    ax.plot([x_drop, x_drop], [P_drop_top[1], P_drop_bot[1]], 'k-', lw=1.6, zorder=2)

    # 8. Vertex Dot
    ax.plot([0], [0], 'ko', markersize=5.0, zorder=4)

    # 9. Right Angle Square Markers
    # Top right corner box at (0, y_R)
    box_s1 = 0.28
    ax.plot([0, box_s1, box_s1], [y_R - box_s1, y_R - box_s1, y_R], 'k-', lw=1.5, zorder=2)

    # Left drop corner box at (x_drop, y_L) - box in top-left quadrant of junction
    box_s2 = 0.22
    ax.plot([x_drop, x_drop - box_s2, x_drop - box_s2], [y_L - box_s2, y_L - box_s2, y_L], 'k-', lw=1.5, zorder=2)

    # 10. Arcs
    # Arc A: between vertical stem (90 deg) and secant line (~43 deg)
    ang_chord_A = math.degrees(math.atan2(y_R, x_R)) # 42.9 deg
    arc_A_rad = 1.35
    arc_A = patches.Arc((0, 0), arc_A_rad * 2, arc_A_rad * 2, angle=0, theta1=ang_chord_A, theta2=90, lw=1.4, color='black', zorder=2)
    ax.add_patch(arc_A)

    # Arc B: between horizontal line (0 deg) and left chord
    ang_chord_B = math.degrees(math.atan2(-y_L, -x_L))
    arc_B_rad = 0.95
    arc_B = patches.Arc((x_L, y_L), arc_B_rad * 2, arc_B_rad * 2, angle=0, theta1=ang_chord_B, theta2=0, lw=1.4, color='black', zorder=2)
    ax.add_patch(arc_B)

    # Arc C: between left chord and bottom-left extension
    ang_ext = math.degrees(math.atan2(y_ext, x_ext))
    ang_chord_left = 143.5
    arc_C_rad = 1.25
    arc_C = patches.Arc((0, 0), arc_C_rad * 2, arc_C_rad * 2, angle=0, theta1=ang_chord_left, theta2=ang_ext, lw=1.4, color='black', zorder=2)
    ax.add_patch(arc_C)

    # 11. Labels Placement (Exact visual positioning)
    # Formula
    ax.text(x_R + 0.35, y_R + 0.05, r"$\mathrm{f(x) = ax^2 + bx + c}$", fontsize=16, va='center', ha='left', zorder=5)

    # m
    ax.text(x_R * 0.52, y_R + 0.12, r"$m$", fontsize=16, ha='center', va='bottom', zorder=5)

    # a (on vertical stem, right side, below top box)
    ax.text(0.12, (y_R + y_L) * 0.5 - 0.05, r"$a$", fontsize=15, ha='left', va='center', zorder=5)

    # b
    ax.text((x_L + x_drop) * 0.5, y_L + 0.12, r"$b$", fontsize=16, ha='center', va='bottom', zorder=5)

    # n (on vertical stem, left side, lower half)
    ax.text(-0.12, y_L * 0.5, r"$n$", fontsize=15, ha='right', va='center', zorder=5)

    # A (inside the angle sector, positioned at x=0.20, y=0.60, completely away from chord and arc)
    ax.text(0.20, 0.60, r"$A$", fontsize=16, ha='center', va='center', zorder=5)

    # B (inside the angle sector B)
    ax.text(x_L + 0.42, y_L - 0.20, r"$B$", fontsize=16, ha='center', va='center', zorder=5)

    # C (to the left of arc C)
    ax.text(-0.78, -0.42, r"$C$", fontsize=17, ha='right', va='center', zorder=5)

    ax.set_xlim(-3.2, 5.5)
    ax.set_ylim(-2.2, 3.4)

    plt.tight_layout()
    plt.savefig('test_perfect_render.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Rendered test_perfect_render.png")

if __name__ == '__main__':
    test_render()
