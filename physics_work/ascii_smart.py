import sys
import cv2
import numpy as np

src = sys.argv[1]
width = int(sys.argv[2]) if len(sys.argv) > 2 else 120

img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("FAILED_TO_READ")
    sys.exit(1)
h, w = img.shape
bh = max(1, round(h / (width * 0.6)))
bw = max(1, round(w / width))
rows = h // bh
cols = w // bw
for r in range(rows):
    line = ""
    for c in range(cols):
        blk = img[r*bh:(r+1)*bh, c*bw:(c+1)*bw]
        bright = (blk > 150).mean()
        line += "#" if bright > 0.25 else ("-" if bright > 0.05 else " ")
    print(line)
