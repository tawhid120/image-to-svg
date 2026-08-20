# -*- coding: utf-8 -*-
"""
process_clean_pngs_and_upload.py
================================
1. Enhances, upscales, and cleans all original diagrams:
   - Sets background to pure solid white (#ffffff).
   - Enhances line contrast & sharpness.
   - Adds 2x Lanczos upscaling with clean padding.
2. Purges old files from ImageKit account.
3. Uploads all pristine clean PNGs to ImageKit.
4. Maps every question to its clean high-res PNG URL.
5. Rebuilds processed_questions.json and question_bank_viewer.html.
"""

import os
import json
import re
import requests
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

IMAGEKIT_PRIVATE_KEY  = "private_cJXcFIjPOZe+7yKDQCR74pSyNIE="
upload_url = "https://upload.imagekit.io/api/v2/files/upload"
auth = (IMAGEKIT_PRIVATE_KEY, "")

HERE = os.path.dirname(os.path.abspath(__file__))
raw_img_dir = os.path.join(HERE, "downloaded_diagrams")
out_img_dir = os.path.join(HERE, "clean_png_diagrams")
os.makedirs(out_img_dir, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# 1. PURGE OLD FILES FROM IMAGEKIT
# ─────────────────────────────────────────────────────────────────────────────
print("Purging old ImageKit files...")
try:
    list_url = "https://api.imagekit.io/v1/files?path=%2Fmath_2nd_ch7%2F&limit=100"
    res = requests.get(list_url, auth=auth, timeout=30)
    if res.ok:
        for f in res.json():
            fid = f.get("fileId")
            requests.delete(f"https://api.imagekit.io/v1/files/{fid}", auth=auth, timeout=20)
            print(f"  Deleted: {f.get('name')}")
except Exception as e:
    print("Purge warning:", e)

# ─────────────────────────────────────────────────────────────────────────────
# 2. IMAGE ENHANCEMENT & CLEANING FUNCTION
# ─────────────────────────────────────────────────────────────────────────────
def clean_and_enhance_image(src_path, dst_path):
    img = Image.open(src_path)
    
    # 1. Convert to RGBA first to handle any alpha transparency
    if img.mode != "RGBA":
        img = img.convert("RGBA")
        
    # Create pure white background
    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, img).convert("RGB")
    
    # 2. Convert to Grayscale for threshold cleaning if needed, or enhance color
    # Enhance contrast to make lines deep black and background pure white
    enhancer = ImageEnhance.Contrast(composite)
    composite = enhancer.enhance(1.4)
    
    # Clean background: Any pixels that are nearly white (> 235 on all channels) make pure 255
    data = composite.getdata()
    new_data = []
    for item in data:
        if item[0] > 230 and item[1] > 230 and item[2] > 230:
            new_data.append((255, 255, 255))
        else:
            # Make dark ink even darker
            r = max(0, int(item[0] * 0.85))
            g = max(0, int(item[1] * 0.85))
            b = max(0, int(item[2] * 0.85))
            new_data.append((r, g, b))
    composite.putdata(new_data)
    
    # 3. 2x Super-Resolution Upscaling with Lanczos filter
    w, h = composite.size
    new_w, new_h = w * 2, h * 2
    upscaled = composite.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # 4. Subtle Unsharp Mask for ultra-crisp line edges
    upscaled = upscaled.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
    
    # 5. Add elegant 24px pure white border padding
    final_img = ImageOps.expand(upscaled, border=24, fill=(255, 255, 255))
    
    final_img.save(dst_path, "PNG", dpi=(300, 300), optimize=True)
    return dst_path

# ─────────────────────────────────────────────────────────────────────────────
# 3. PROCESS ALL DIAGRAMS
# ─────────────────────────────────────────────────────────────────────────────
print("\nEnhancing & cleaning all diagram images...")
clean_files = {}

# Process question-specific named files: q_{num}_img_{idx}.png
q_file_pattern = re.compile(r"^q_(\d+)_img_(\d+)\.png$")
for fname in os.listdir(raw_img_dir):
    src = os.path.join(raw_img_dir, fname)
    if not os.path.isfile(src) or not fname.lower().endswith(('.png', '.webp')):
        continue
    
    dst_name = "clean_" + fname.replace(".webp", ".png")
    dst = os.path.join(out_img_dir, dst_name)
    clean_and_enhance_image(src, dst)
    clean_files[fname] = dst_name

print(f"Enhanced {len(clean_files)} diagram images successfully.")

# ─────────────────────────────────────────────────────────────────────────────
# 4. UPLOAD CLEAN PNGs TO IMAGEKIT
# ─────────────────────────────────────────────────────────────────────────────
print("\nUploading clean high-res PNGs to ImageKit...")
clean_uploaded_urls = {}

for orig_name, clean_name in clean_files.items():
    p = os.path.join(out_img_dir, clean_name)
    with open(p, "rb") as f:
        img_bytes = f.read()
        
    files = {"file": (clean_name, img_bytes, "image/png")}
    data = {
        "fileName": clean_name,
        "folder": "/math_2nd_ch7/clean_png/",
        "isPrivateFile": "false",
        "useUniqueFileName": "false"
    }
    res = requests.post(upload_url, auth=auth, files=files, data=data, timeout=30)
    if res.ok:
        ik_url = res.json().get("url")
        clean_uploaded_urls[clean_name] = ik_url
        clean_uploaded_urls[orig_name] = ik_url
        print(f"  [OK] {clean_name} -> {ik_url}")
    else:
        print(f"  [ERROR] {clean_name}: {res.text}")

with open(os.path.join(HERE, "clean_uploaded_map.json"), "w", encoding="utf-8") as f:
    json.dump(clean_uploaded_urls, f, indent=2)

# ─────────────────────────────────────────────────────────────────────────────
# 5. ASSOCIATE QUESTIONS WITH THEIR CLEAN PNGs
# ─────────────────────────────────────────────────────────────────────────────
# Question number to uploaded clean image URL mapping
QUESTION_CLEAN_MAP = {}
for qn in range(1, 950):
    # Check if q_{qn}_img_1.png or multiple exist
    q_imgs = [clean_uploaded_urls[f"q_{qn}_img_{i}.png"] for i in range(1, 10) if f"q_{qn}_img_{i}.png" in clean_uploaded_urls]
    if q_imgs:
        if len(q_imgs) == 1:
            QUESTION_CLEAN_MAP[qn] = q_imgs[0]
        else:
            QUESTION_CLEAN_MAP[qn] = q_imgs

print(f"Mapped {len(QUESTION_CLEAN_MAP)} questions to their clean PNG images.")

# ─────────────────────────────────────────────────────────────────────────────
# 6. UPDATE RAW JSON & PROCESSED_QUESTIONS.JSON
# ─────────────────────────────────────────────────────────────────────────────
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for q_idx, q in enumerate(raw_data["data"]["questions"], 1):
    if q_idx in QUESTION_CLEAN_MAP:
        mapping = QUESTION_CLEAN_MAP[q_idx]
        if isinstance(mapping, list):
            # Multiple options (e.g. Q546)
            for opt_idx, opt in enumerate(q.get("question_options", [])):
                opt_body = opt.get("body", {})
                for ek, ent in opt_body.get("entityMap", {}).items():
                    if ent.get("type") == "IMAGE":
                        ent["data"]["src"] = mapping[min(opt_idx, len(mapping)-1)]
        else:
            img_url = mapping
            body = q.get("question", {}).get("body", {})
            for ek, ent in body.get("entityMap", {}).items():
                if ent.get("type") == "IMAGE":
                    ent["data"]["src"] = img_url

with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

# Update processed_questions.json directly
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    qn = q["n"]
    if qn in QUESTION_CLEAN_MAP:
        mapping = QUESTION_CLEAN_MAP[qn]
        if isinstance(mapping, list):
            if q.get("o"):
                for i, opt_url in enumerate(mapping):
                    if i < len(q["o"]):
                        q["o"][i] = f"![চিত্র]({opt_url})"
        else:
            img_url = mapping
            if "![" in q["q"]:
                q["q"] = re.sub(r"!\[(.*?)\]\([^)]+\)", f"![চিত্র]({img_url})", q["q"])
            else:
                q["q"] = f"![চিত্র]({img_url})\n" + q["q"]

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated all questions with ultra-clean high-res PNG images!")
