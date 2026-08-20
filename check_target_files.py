import json
import os

files = [
    "clean_q_786_img_1.png",
    "clean_q_794_img_1.png",
    "clean_q_796_img_1.png",
    "clean_q_802_img_1.png",
    "clean_q_806_img_1.png",
    "clean_q_840_img_1.png",
    "clean_q_846_img_1.png",
    "clean_q_873_img_1.png"
]
for f in files:
    p = os.path.join("downloaded_diagrams", f.replace("clean_", ""))
    print(f, "exists:", os.path.exists(p))
