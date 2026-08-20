import sys
import cv2
import numpy as np

src = sys.argv[1]
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 120
rows = int(sys.argv[3]) if len(sys.argv) > 3 else 60

img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("FAILED_TO_READ")
    sys.exit(1)
img2 = cv2.resize(img, (cols, rows), interpolation=cv2.INTER_AREA)
chars = " .:-=+*#%@"
for r in range(rows):
    line = ""
    for c in range(cols):
        v = img2[r, c]
        idx = int(v / 256 * len(chars))
        if idx >= len(chars): idx = len(chars) - 1
        line += chars[idx]
    print(line)
