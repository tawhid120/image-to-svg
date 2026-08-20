import json
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "processed_questions.json"), encoding="utf-8") as f:
    data = json.load(f)

q_map = {q["n"]: q for q in data["questions"]}

defect_keywords = ["চিত্র অনুপস্থিত", "চিত্র দেখা যাচ্ছে না", "চিত্রনির্ভর", "চিত্র নির্ভর", "অনুমিত", "চিত্র-কাঠামো", "মান বসালে সাংখ্যিক"]

defects = []
for q in data["questions"]:
    text = q.get("a", "") + " " + q.get("e", "")
    for kw in defect_keywords:
        if kw in text:
            defects.append((q["n"], kw, q))
            break

print(f"Found {len(defects)} questions with diagram defect keywords in solution/explanation:")
for qn, kw, q in defects:
    print(f"Q{qn} (Keyword: '{kw}'):")
    print(f"  Q: {q['q'][:120]}")
    print(f"  A: {q['a']}")
    print(f"  E: {q['e'][:150]}")
    print("-" * 70)
