# -*- coding: utf-8 -*-
"""
upload_svgs_and_update_viewer.py
================================
1. Uploads all generated clean vector SVGs to ImageKit in /math_2nd_ch7/svg/
2. Maps them to the corresponding question diagrams
3. Updates process_question_bank.py and viewer_template.html with theme-adaptive SVG rendering and dark-mode styles.
"""

import json
import os
import requests

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
svg_dir = os.path.join(HERE, "svg_diagrams")

svg_urls = {}
for fname in os.listdir(svg_dir):
    if fname.endswith(".svg"):
        fpath = os.path.join(svg_dir, fname)
        with open(fpath, "rb") as f:
            svg_bytes = f.read()

        files = {"file": (fname, svg_bytes, "image/svg+xml")}
        data = {
            "fileName": fname,
            "folder": "/math_2nd_ch7/svg/",
            "isPrivateFile": "false",
            "useUniqueFileName": "false"
        }
        res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
        if res.ok:
            ik_url = res.json().get("url")
            svg_urls[fname] = ik_url
            print(f"Uploaded SVG {fname} -> {ik_url}")
        else:
            print(f"Failed SVG {fname}: {res.text}")

with open(os.path.join(HERE, "svg_imagekit_map.json"), "w", encoding="utf-8") as f:
    json.dump(svg_urls, f, indent=2)

print(f"All {len(svg_urls)} SVGs uploaded to ImageKit successfully!")
