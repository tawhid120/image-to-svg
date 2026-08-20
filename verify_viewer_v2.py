import re

with open("question_bank_viewer.html", encoding="utf-8") as f:
    text = f.read()

matches = re.findall(r"svg_v2_[^\"' \)]+", text)
print(f"Found {len(matches)} V2 SVG URLs in question_bank_viewer.html")
for m in set(matches):
    print(" ", m)
