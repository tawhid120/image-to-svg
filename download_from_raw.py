import json
import os
import urllib.request
import re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW_JSON = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
OUT_DIR = os.path.join(HERE, "downloaded_diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

with open(RAW_JSON, encoding="utf-8") as f:
    raw_data = json.load(f)

qs = raw_data["data"]["questions"]

def get_images_from_draftjs(val):
    if not val:
        return []
    if isinstance(val, str):
        val_s = val.strip()
        if val_s.startswith("{") and "blocks" in val_s:
            try:
                val = json.loads(val_s)
            except Exception:
                return []
        else:
            return []
    if isinstance(val, dict):
        emap = val.get("entityMap") or {}
        urls = []
        for k, ent in emap.items():
            if ent.get("type") == "IMAGE":
                src = ent.get("data", {}).get("src")
                if src:
                    urls.append(src)
        return urls
    return []

q_images = {}
for i, q in enumerate(qs, 1):
    q_urls = []
    # check question text
    q_urls.extend(get_images_from_draftjs(q.get("question_text")))
    # check explanation text
    q_urls.extend(get_images_from_draftjs(q.get("explanation_text")))
    # check options
    for o in q.get("option") or []:
        q_urls.extend(get_images_from_draftjs(o))
    
    if q_urls:
        q_images[i] = list(set(q_urls))

print(f"Found {len(q_images)} questions with image entities in raw JSON:")
for q_num, urls in sorted(q_images.items()):
    print(f"Q{q_num}: {len(urls)} image(s)")
    for idx, u in enumerate(urls, 1):
        local_file = os.path.join(OUT_DIR, f"q_{q_num}_img_{idx}.png")
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=8) as resp, open(local_file, 'wb') as out:
                out.write(resp.read())
            print(f"  [{idx}] SUCCESS -> {local_file} ({os.path.getsize(local_file)} bytes)")
        except Exception as e:
            print(f"  [{idx}] FAILED ({e}): {u[:80]}")
