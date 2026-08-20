import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_perfect_100_percent():
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 1. Parabola: y = a_p * x^2
    a_p = 0.38
    x_min, x_max = -2.7, 2.75
    
    xs = np.linspace(x_min, x_max, 250)
    ys = a_p * (xs ** 2)
    
    # Parabola key points:
    x_R = 2.45
    y_R = a_p * (x_R ** 2)  # ~2.28
    
    x_L = -1.95
    y_L = a_p * (x_L ** 2)  # ~1.445
    
    V = (0.0, 0.0)
    P_top = (0.0, y_R)
    P_mid = (0.0, y_L)
    
    slope_line = y_R / x_R  # ~0.931
    x_ext = -1.9
    y_ext = slope_line * x_ext
    P_ext = (x_ext, y_ext)
    
    # Left drop
    x_drop = -0.75
    P_drop_top = (x_drop, y_L)
    m_left_chord = y_L / x_L
    y_drop_bot = m_left_chord * x_drop
    P_drop_bot = (x_drop, y_drop_bot)

    # 1. Plot Parabola
    ax.plot(xs, ys, 'k-', lw=2.2, zorder=2)
    
    # Explicit Outward Arrowheads on Parabola
    ax.annotate('', xy=(xs[0], ys[0]), xytext=(xs[3], ys[3]),
                arrowprops=dict(arrowstyle='-|>', lw=2.0, color='black', mutation_scale=16))
    ax.annotate('', xy=(xs[-1], ys[-1]), xytext=(xs[-4], ys[-4]),
                arrowprops=dict(arrowstyle='-|>', lw=2.0, color='black', mutation_scale=16))

    # 2. Straight Secant Line
    ax.plot([P_ext[0], x_R], [P_ext[1], y_R], 'k-', lw=2.0, zorder=2)
    
    # 3. Central Vertical Stem
    ax.plot([0, 0], [y_R, 0], 'k-', lw=1.8, zorder=2)
    
    # 4. Top Horizontal Line (m)
    ax.plot([0, x_R], [y_R, y_R], 'k-', lw=1.8, zorder=2)
    
    # 5. Left Horizontal Line (b)
    ax.plot([x_L, 0], [y_L, y_L], 'k-', lw=1.8, zorder=2)
    
    # 6. Left Chord
    ax.plot([x_L, 0], [y_L, 0], 'k-', lw=1.8, zorder=2)
    
    # 7. Left Vertical Drop
    ax.plot([x_drop, x_drop], [P_drop_top[1], P_drop_bot[1]], 'k-', lw=1.6, zorder=2)
    
    # 8. Vertex Dot
    ax.plot([0], [0], 'ko', markersize=4.5, zorder=4)
    
    # 9. Right Angle Markers
    box_s1 = 0.28
    ax.plot([0, box_s1, box_s1], [y_R - box_s1, y_R - box_s1, y_R], 'k-', lw=1.4, zorder=2)
    
    box_s2 = 0.22
    ax.plot([x_drop, x_drop - box_s2, x_drop - box_s2], [y_L - box_s2, y_L - box_s2, y_L], 'k-', lw=1.4, zorder=2)

    # 10. Angle Arcs & Anti-Collision Bisector Calculations
    # Angle A: arc radius 1.35
    ang_chord_A = math.degrees(math.atan2(y_R, x_R)) # 42.9 deg
    arc_A_rad = 1.35
    arc_A = patches.Arc((0, 0), arc_A_rad * 2, arc_A_rad * 2, angle=0, theta1=ang_chord_A, theta2=90, lw=1.4, color='black', zorder=2)
    ax.add_patch(arc_A)
    # Position A at r = 0.65, theta = 66 deg:
    bisect_A = math.radians((90 + ang_chord_A) / 2.0)
    pos_A_x = 0.65 * math.cos(bisect_A)
    pos_A_y = 0.65 * math.sin(bisect_A)
    ax.text(pos_A_x, pos_A_y, r"$A$", fontsize=15, ha='center', va='center', zorder=5)

    # Angle B:
    ang_chord_B = math.degrees(math.atan2(-y_L, -x_L))
    arc_B_rad = 0.95
    arc_B = patches.Arc((x_L, y_L), arc_B_rad * 2, arc_B_rad * 2, angle=0, theta1=ang_chord_B, theta2=0, lw=1.4, color='black', zorder=2)
    ax.add_patch(arc_B)
    bisect_B = math.radians(ang_chord_B / 2.0)
    pos_B_x = x_L + 0.50 * math.cos(bisect_B)
    pos_B_y = y_L + 0.50 * math.sin(bisect_B)
    ax.text(pos_B_x, pos_B_y, r"$B$", fontsize=15, ha='center', va='center', zorder=5)

    # Angle C:
    ang_ext = math.degrees(math.atan2(y_ext, x_ext)) # ~ -137 deg (223 deg)
    ang_chord_left = 143.5 # deg
    arc_C_rad = 1.25
    arc_C = patches.Arc((0, 0), arc_C_rad * 2, arc_C_rad * 2, angle=0, theta1=ang_chord_left, theta2=ang_ext, lw=1.4, color='black', zorder=2)
    ax.add_patch(arc_C)
    ax.text(-0.75, -0.42, r"$C$", fontsize=16, ha='right', va='center', zorder=5)

    # 11. Labels
    # Formula: f(x) = ax^2 + bx + c
    ax.text(x_R + 0.35, y_R + 0.05, r"$\mathrm{f(x) = ax^2 + bx + c}$", fontsize=15, va='center', ha='left', zorder=5)
    
    # m
    ax.text(x_R * 0.52, y_R + 0.12, r"$m$", fontsize=15, ha='center', va='bottom', zorder=5)
    
    # a
    ax.text(0.08, (y_R + y_L) * 0.5 - 0.02, r"$a$", fontsize=14, ha='left', va='center', zorder=5)
    
    # b
    ax.text((x_L + x_drop) * 0.5, y_L + 0.12, r"$b$", fontsize=15, ha='center', va='bottom', zorder=5)
    
    # n
    ax.text(-0.08, y_L * 0.5, r"$n$", fontsize=14, ha='right', va='center', zorder=5)

    ax.set_xlim(-3.2, 5.2)
    ax.set_ylim(-2.2, 3.4)
    
    plt.tight_layout()
    plt.savefig('perfect_100.png', bbox_inches='tight', dpi=300)
    plt.close()
    print('Updated perfect_100.png')

if __name__ == '__main__':
    generate_perfect_100_percent()
