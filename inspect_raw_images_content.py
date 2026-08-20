# -*- coding: utf-8 -*-
"""
inspect_raw_images_content.py
"""
import os
import pytesseract
from PIL import Image

targets = [815, 816, 817, 819, 829, 840, 846, 864, 865, 867, 868, 874, 882, 883, 884, 885, 886, 887, 892, 896]

for qn in targets:
    raw_p = os.path.join("downloaded_diagrams", f"q_{qn}_img_1.png")
    if os.path.exists(raw_p):
        im = Image.open(raw_p)
        print(f"=== Q{qn} raw image size: {im.size} ===")
