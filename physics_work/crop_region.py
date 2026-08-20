import sys, os
import cv2

src = sys.argv[1]
outdir = sys.argv[2]
os.makedirs(outdir, exist_ok=True)
img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

def save(name, x0, y0, x1, y1, inv=True, scale=15):
    crop = img[y0:y1, x0:x1]
    crop = cv2.resize(crop, (crop.shape[1] * scale, crop.shape[0] * scale), interpolation=cv2.INTER_CUBIC)
    if inv:
        crop = 255 - crop
    p = os.path.join(outdir, name)
    cv2.imwrite(p, crop)
    print(name, crop.shape)

# q757 figure regions
save("mid3f.png", 60, 85, 135, 115)     # middle label region
save("bottom.png", 40, 165, 115, 200)   # bottom label region
save("topright.png", 170, 60, 260, 90)  # top-right
save("midright.png", 165, 110, 260, 145) # middle right
