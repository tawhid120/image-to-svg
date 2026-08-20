import json
import re

raw_file = "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json"
with open(raw_file, encoding="utf-8") as f:
    data = json.load(f)

questions = data["data"]["questions"]
url_map = {}

for q_idx, q in enumerate(questions, 1):
    s = json.dumps(q, ensure_ascii=False)
    # Match markdown images or entity URLs
    urls = re.findall(r"https://firebasestorage\.googleapis\.com/v0/b/q-bank-95803\.appspot\.com/o/images%2F[^\"\s)]+", s)
    for u in urls:
        if u not in url_map:
            # extract image filename from URL
            fn_match = re.search(r"images%2F([^?]+)", u)
            fn = fn_match.group(1) if fn_match else f"img_{len(url_map)+1}.png"
            import urllib.parse
            fn_decoded = urllib.parse.unquote(fn)
            url_map[u] = {
                "fn": fn_decoded,
                "questions": []
            }
        if q_idx not in url_map[u]["questions"]:
            url_map[u]["questions"].append(q_idx)

print(f"Total unique URLs: {len(url_map)}")
for u, info in url_map.items():
    print(f"File: {info['fn']:<40} | Qs: {info['questions']}")
