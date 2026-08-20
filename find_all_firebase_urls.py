import json
import re

raw_file = "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json"
with open(raw_file, encoding="utf-8") as f:
    data = json.load(f)

questions = data["data"]["questions"]
firebase_urls = {}
for q_idx, q in enumerate(questions, 1):
    s = json.dumps(q, ensure_ascii=False)
    # Find all firebasestorage urls
    urls = re.findall(r"https://firebasestorage\.googleapis\.com/v0/b/q-bank-95803\.appspot\.com/o/images%2F[^\"]+", s)
    for u in urls:
        # clean URL trailing chars
        u_clean = u.split("?alt=")[0] + "?alt=" + u.split("?alt=")[1] if "?alt=" in u else u
        if u_clean not in firebase_urls:
            firebase_urls[u_clean] = []
        firebase_urls[u_clean].append(q_idx)

print(f"Total unique Firebase URLs: {len(firebase_urls)}")
for u, qs in firebase_urls.items():
    print(f"URL: {u[:80]}... -> Used in Questions: {qs}")
