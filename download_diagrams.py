import json
import os
import urllib.request
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "downloaded_diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

with open(os.path.join(HERE, "processed_questions.json"), encoding="utf-8") as f:
    data = json.load(f)

downloaded = {}
for q in data["questions"]:
    text = q.get("q", "") + " " + q.get("e", "") + " " + " ".join(q.get("o", []))
    urls = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', text)
    if not urls:
        urls = re.findall(r'https?://firebasestorage\.googleapis\.com[^\s\)\"\']+', text)
    
    if urls:
        q_num = q["n"]
        downloaded[q_num] = []
        for idx, u in enumerate(urls):
            # Clean url if needed
            clean_u = u.strip()
            # If missing alt=media and token, check if there's a token
            ext = ".png"
            local_path = os.path.join(OUT_DIR, f"q_{q_num}_img_{idx+1}{ext}")
            try:
                # Add headers to avoid 403
                req = urllib.request.Request(clean_u, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp, open(local_path, 'wb') as f_out:
                    f_out.write(resp.read())
                downloaded[q_num].append(local_path)
                print(f"Downloaded Q{q_num} image {idx+1} -> {local_path} ({os.path.getsize(local_path)} bytes)")
            except Exception as ex:
                print(f"Failed Q{q_num} image {idx+1} from {clean_u[:60]}: {ex}")

print(f"\nDone downloading! Total questions with downloaded images: {len(downloaded)}")
