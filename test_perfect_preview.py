import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_perfect_benchmark():
    # Set up figure
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Mathematical Model
    a_p = 0.38
    x_min, x_max = -2.7, 2.75
    
    # Points on parabola:
    x_R = 2.45
    y_R = a_p * (x_R ** 2)  # ~2.28
    
    x_L = -1.95
    y_L = a_p * (x_L ** 2)  # ~1.445
    
    V = (0.0, 0.0)
    P_top = (0.0, y_R)
    P_mid = (0.0, y_L)
    
    slope_line = y_R / x_R  # ~0.93
    x_ext = -1.8
    y_ext = slope_line * x_ext
    P_ext = (x_ext, y_ext)
    
    # Left vertical drop inside left triangle:
    x_drop = -0.72
    P_drop_top = (x_drop, y_L)
    m_left_chord = y_L / x_L
    y_drop_bot = m_left_chord * x_drop
    P_drop_bot = (x_drop, y_drop_bot)

    # 1. Parabola curve
    xs = np.linspace(x_min, x_max, 250)
    ys = a_p * (xs ** 2)
    ax.plot(xs, ys, 'k-', lw=2.2, zorder=2)
    
    # Parabola Arrowheads (sharp and clean)
    dx_l = xs[1] - xs[0]
    dy_l = ys[1] - ys[0]
    ax.annotate('', xy=(xs[0], ys[0]), xytext=(xs[0]-dx_l*5, ys[0]-dy_l*5),
                arrowprops=dict(arrowstyle='<|-', lw=2.0, color='black', mutation_scale=16))
    dx_r = xs[-1] - xs[-2]
    dy_r = ys[-1] - ys[-2]
    ax.annotate('', xy=(xs[-1], ys[-1]), xytext=(xs[-1]+dx_r*5, ys[-1]+dy_r*5),
                arrowprops=dict(arrowstyle='-|>', lw=2.0, color='black', mutation_scale=16))

    # 2. Continuous Straight Secant Line
    ax.plot([P_ext[0], x_R], [P_ext[1], y_R], 'k-', lw=2.0, zorder=2)
    
    # 3. Central Vertical Line
    ax.plot([0, 0], [y_R, 0], 'k-', lw=1.8, zorder=2)
    
    # 4. Top horizontal line (m)
    ax.plot([0, x_R], [y_R, y_R], 'k-', lw=1.8, zorder=2)
    
    # 5. Left horizontal line (b)
    ax.plot([x_L, 0], [y_L, y_L], 'k-', lw=1.8, zorder=2)
    
    # 6. Left chord
    ax.plot([x_L, 0], [y_L, 0], 'k-', lw=1.8, zorder=2)
    
    # 7. Left vertical drop
    ax.plot([x_drop, x_drop], [P_drop_top[1], P_drop_bot[1]], 'k-', lw=1.6, zorder=2)
    
    # 8. Vertex Dot
    ax.plot([0], [0], 'ko', markersize=4.5, zorder=4)
    
    # 9. Right Angle Markers
    box_s1 = 0.28
    ax.plot([0, box_s1, box_s1], [y_R - box_s1, y_R - box_s1, y_R], 'k-', lw=1.4)
    
    box_s2 = 0.22
    ax.plot([x_drop, x_drop - box_s2, x_drop - box_s2], [y_L - box_s2, y_L - box_s2, y_L], 'k-', lw=1.4)

    # 10. Angle Arcs
    ang_line_deg = math.degrees(math.atan2(y_R, x_R)) # ~43 deg
    arc_A = patches.Arc((0, 0), 1.2, 1.2, angle=0, theta1=ang_line_deg, theta2=90, lw=1.4, color='black')
    ax.add_patch(arc_A)
    
    ang_B_chord = math.degrees(math.atan2(-y_L, -x_L))
    arc_B = patches.Arc((x_L, y_L), 0.85, 0.85, angle=0, theta1=ang_B_chord, theta2=0, lw=1.4, color='black')
    ax.add_patch(arc_B)
    
    ang_ext = math.degrees(math.atan2(y_ext, x_ext))
    arc_C = patches.Arc((0, 0), 1.15, 1.15, angle=0, theta1=143.5, theta2=ang_ext, lw=1.4, color='black')
    ax.add_patch(arc_C)
    
    # 11. Labels with perfect positioning
    # Formula: f(x) = ax^2 + bx + c
    ax.text(x_R + 0.35, y_R + 0.05, r"$\mathrm{f(x) = ax^2 + bx + c}$", fontsize=15, va='center', ha='left')
    
    # m
    ax.text(x_R * 0.52, y_R + 0.12, r"$m$", fontsize=15, ha='center', va='bottom')
    
    # a (centered between top horizontal and middle horizontal)
    ax.text(0.08, (y_R + y_L) * 0.5 - 0.02, r"$a$", fontsize=14, ha='left', va='center')
    
    # b
    ax.text((x_L + x_drop) * 0.5, y_L + 0.12, r"$b$", fontsize=15, ha='center', va='bottom')
    
    # n (centered between middle horizontal and vertex)
    ax.text(-0.08, y_L * 0.5, r"$n$", fontsize=14, ha='right', va='center')
    
    # A (positioned cleanly inside the sector)
    ax.text(0.12, 0.22, r"$A$", fontsize=15, ha='left', va='center')
    
    # B (positioned cleanly inside angle B)
    ax.text(x_L + 0.35, y_L - 0.22, r"$B$", fontsize=15, ha='center', va='center')
    
    # C (positioned cleanly to the left of arc C)
    ax.text(-0.65, -0.38, r"$C$", fontsize=16, ha='right', va='center')
    
    ax.set_xlim(-3.2, 5.2)
    ax.set_ylim(-2.2, 3.4)
    
    plt.tight_layout()
    plt.savefig('perfect_preview.png', bbox_inches='tight', dpi=300)
    plt.close()
    print('Updated perfect_preview.png')

if __name__ == '__main__':
    generate_perfect_benchmark()
