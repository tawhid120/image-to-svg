import json
import re

with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

keywords = [
    "চিত্র অনুপস্থিত",
    "চিত্রনির্ভর",
    "চিত্র নির্ভর",
    "চিত্র ছাড়া",
    "চিত্র ছাড়া",
    "অনুমিত",
    "চিত্র-কাঠামো",
    "চিত্র-সাপেক্ষ",
    "চিত্র সাপেক্ষ",
    "অপ্রতুল",
    "সংজ্ঞাহীন",
    "অসমাধেয়"
]

found = []
for q in data["questions"]:
    text_all = f"{q.get('q', '')} {q.get('a', '')} {q.get('e', '')} {' '.join(q.get('o', []))}"
    for kw in keywords:
        if kw in text_all:
            found.append({
                "n": q["n"],
                "type": q["t"],
                "kw": kw,
                "a": q.get("a", ""),
                "e": q.get("e", "")
            })
            break

print(f"Total questions containing suspicious words: {len(found)}")
for it in found:
    print(f"Q{it['n']} (Found '{it['kw']}'):")
    print(f"  A: {it['a'][:150]}")
    print(f"  E: {it['e'][:150]}")
    print("=" * 60)
