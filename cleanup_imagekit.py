# -*- coding: utf-8 -*-
"""
cleanup_imagekit.py
===================
Deletes all uploaded files in /math_2nd_ch7/ from ImageKit.
"""

import requests
import json

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
auth = (IMAGEKIT_PRIVATE_KEY, "")

# List all files in folder
list_url = "https://api.imagekit.io/v1/files?path=%2Fmath_2nd_ch7%2F&limit=100"
res = requests.get(list_url, auth=auth, timeout=30)
if res.ok:
    files = res.json()
    print(f"Found {len(files)} files in /math_2nd_ch7/ to delete.")
    for f in files:
        file_id = f.get("fileId")
        name = f.get("name")
        del_url = f"https://api.imagekit.io/v1/files/{file_id}"
        del_res = requests.delete(del_url, auth=auth, timeout=30)
        if del_res.status_code in [200, 204]:
            print(f"Deleted: {name} ({file_id})")
        else:
            print(f"Failed to delete {name}: {del_res.text}")
else:
    print("Failed to list files:", res.text)
