import json
import re

with open(r"C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json", encoding="utf-8") as f:
    raw_data = json.load(f)

qs = raw_data["data"]["questions"]
print(f"Total original questions: {len(qs)}")

img_q_list = []
for i, q in enumerate(qs, 1):
    q_str = json.dumps(q, ensure_ascii=False)
    if "firebasestorage" in q_str or "IMAGE" in q_str:
        img_q_list.append(i)

print(f"Questions with images in raw JSON: {len(img_q_list)}")
print(img_q_list)
