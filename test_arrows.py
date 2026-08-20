import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def test_arrows():
    # Parabola
    a_p = 0.38
    x_min, x_max = -2.7, 2.75
    
    xs = np.linspace(x_min, x_max, 250)
    ys = a_p * (xs ** 2)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.plot(xs, ys, 'k-', lw=2.4)
    
    # Left tip arrow pointing up-left
    # Tangent at start:
    dx_l = xs[0] - xs[2]
    dy_l = ys[0] - ys[2]
    len_l = math.hypot(dx_l, dy_l)
    ux_l, uy_l = dx_l / len_l, dy_l / len_l
    
    # Draw arrow polygon at left tip
    arrow_len = 0.35
    arrow_w = 0.16
    tip_l = (xs[0], ys[0])
    base_l = (xs[0] - ux_l * arrow_len, ys[0] - uy_l * arrow_len)
    perp_l = (-uy_l, ux_l)
    p_left_1 = (base_l[0] + perp_l[0] * arrow_w, base_l[1] + perp_l[1] * arrow_w)
    p_left_2 = (base_l[0] - perp_l[0] * arrow_w, base_l[1] - perp_l[1] * arrow_w)
    
    poly_left = plt.Polygon([tip_l, p_left_1, (base_l[0] + ux_l * 0.08, base_l[1] + uy_l * 0.08), p_left_2], color='black')
    ax.add_patch(poly_left)
    
    # Right tip arrow pointing up-right
    dx_r = xs[-1] - xs[-3]
    dy_r = ys[-1] - ys[-3]
    len_r = math.hypot(dx_r, dy_r)
    ux_r, uy_r = dx_r / len_r, dy_r / len_r
    
    tip_r = (xs[-1], ys[-1])
    base_r = (xs[-1] - ux_r * arrow_len, ys[-1] - uy_r * arrow_len)
    perp_r = (-uy_r, ux_r)
    p_right_1 = (base_r[0] + perp_r[0] * arrow_w, base_r[1] + perp_r[1] * arrow_w)
    p_right_2 = (base_r[0] - perp_r[0] * arrow_w, base_r[1] - perp_r[1] * arrow_w)
    
    poly_right = plt.Polygon([tip_r, p_right_1, (base_r[0] + ux_r * 0.08, base_r[1] + uy_r * 0.08), p_right_2], color='black')
    ax.add_patch(poly_right)
    
    # Save preview
    plt.savefig('arrow_preview.png', bbox_inches='tight', dpi=300)
    plt.close()
    print('Generated arrow_preview.png')

if __name__ == '__main__':
    test_arrows()
