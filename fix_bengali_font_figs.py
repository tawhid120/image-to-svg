import os
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

def setup_canvas(width=7.0, height=4.0):
    fig, ax = plt.subplots(figsize=(width, height), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    return fig, ax

def save_and_close(fig, path):
    plt.tight_layout(pad=1.5)
    fig.savefig(path, facecolor='#ffffff', edgecolor='none', bbox_inches='tight', pad_inches=0.2, dpi=300)
    plt.close(fig)

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
ax.text(0.38, -0.15, '(i)', fontsize=14, fontweight='bold', color='#0284c7')
# Tri 2
ax.plot([1.4, 2.3, 1.9, 1.4], [0, 0, 0.9, 0], color='#0f172a', lw=2.5)
ax.text(1.34, -0.05, 'D', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(2.35, -0.05, 'E', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.88, 0.95, 'F', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.82, -0.15, '(ii)', fontsize=14, fontweight='bold', color='#0284c7')
p846 = os.path.join(out_dir, "diag_846.png")
save_and_close(fig, p846)

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
ax.text(0.38, -0.18, '(i)', fontsize=14, fontweight='bold', color='#0284c7')
# Tri 2
ax.plot([1.4, 2.3, 2.3, 1.4], [0, 0, 0.8, 0], color='#0f172a', lw=2.5)
ax.plot([2.2, 2.2, 2.3], [0.0, 0.1, 0.1], color='#0f172a', lw=1.5)
arc2 = patches.Arc((1.4,0), 0.35, 0.35, angle=0, theta1=0, theta2=41.6, color='#2563eb', lw=2)
ax.add_patch(arc2)
ax.text(1.72, 0.48, r'$2\sqrt{3}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.7, -0.1, r'$\sqrt{3}+\sqrt{2}$', fontsize=14, fontweight='bold', color='#0f172a')
ax.text(1.62, 0.05, r'$\beta$', fontsize=15, fontweight='bold', color='#2563eb')
ax.text(1.82, -0.18, '(ii)', fontsize=14, fontweight='bold', color='#0284c7')
p894 = os.path.join(out_dir, "diag_894.png")
save_and_close(fig, p894)

# Re-upload the two files
for fname, p in [("diag_846.png", p846), ("diag_894.png", p894)]:
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
    print("Re-uploaded", fname, "->", res.status_code)
