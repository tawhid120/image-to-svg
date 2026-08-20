import sys
import cv2
import numpy as np

src = sys.argv[1]
half = int(sys.argv[2]) if len(sys.argv) > 2 else 0  # 0=left, 1=right

img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("FAILED_TO_READ")
    sys.exit(1)
h, w = img.shape
cols = w // 2 if half == 0 else w - w // 2
x0 = 0 if half == 0 else w // 2
for r in range(h):
    line = ""
    for c in range(cols):
        line += "#" if img[r, x0 + c] > 100 else "."
    print(line)
