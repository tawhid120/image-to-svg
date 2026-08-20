import json
import os

with open("clean_uploaded_map.json") as f:
    clean_urls = json.load(f)

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    qn = q["n"]
    k = f"clean_q_{qn}_img_1.png"
    if k in clean_urls:
        print(f"Q{qn} has downloaded original: {clean_urls[k]}")
