import sys
import cv2
import numpy as np

src = sys.argv[1]
img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("FAILED_TO_READ")
    sys.exit(1)
h, w = img.shape
for r in range(h):
    line = ""
    for c in range(w):
        line += "#" if img[r, c] < 100 else "."
    print(line)
