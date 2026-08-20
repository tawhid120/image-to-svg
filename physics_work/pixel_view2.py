import sys
import cv2

src = sys.argv[1]
img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("FAILED_TO_READ")
    sys.exit(1)
# downscale back to original resolution? No - view as-is but subsample columns by 2
h, w = img.shape
for r in range(h):
    line = ""
    for c in range(0, w, 2):
        v = img[r, c]
        line += "#" if v > 100 else "."
    print(line)
