# -*- coding: utf-8 -*-
import json, glob, os

results_dir = r"physics_work\results"
main_path = r"question_bank_HSC_Admission_HSC_-_পদার্থ_বিজ্ঞান_২য়_পত্র_অধ্যায়-০২ঃ_স্থির_তড়িৎ.json"

def to_draftjs_blocks(text):
    lines = [ln for ln in text.replace("\r\n", "\n").split("\n")]
    return {
        "blocks": [
            {
                "key": "sol%d" % i,
                "text": ln,
                "type": "unstyled",
                "depth": 0,
                "entityRanges": [],
                "inlineStyleRanges": [],
            }
            for i, ln in enumerate(lines)
        ],
        "entityMap": {},
    }

merged = {}
for fp in sorted(glob.glob(os.path.join(results_dir, "batch*.json"))):
    try:
        with open(fp, encoding="utf-8-sig") as f:
            data = json.load(f)
    except Exception as e:
        print("SKIP (bad json):", fp, e)
        continue
    for qid, entry in data.items():
        if not isinstance(entry, dict):
            print("SKIP (non-dict entry):", fp, qid)
            continue
        merged.setdefault(qid, {}).update(entry)

print("result entries total:", len(merged))

with open(main_path, encoding="utf-8") as f:
    main = json.load(f)

questions = main["data"]["questions"]
known = set(q.get("id") for q in questions)
matched = 0
multi = 0
for q in questions:
    qid = q.get("id")
    if qid in merged:
        e = merged[qid]
        if e.get("answer_text"):
            q["answer_text"] = to_draftjs_blocks(e["answer_text"])
        if e.get("explanation_text"):
            q["explanation_text"] = to_draftjs_blocks(e["explanation_text"])
        if e.get("mcq_solution_index") is not None:
            q["mcq_solution_index"] = e["mcq_solution_index"]
        matched += 1

unmatched_results = [qid for qid in merged if qid not in known]
dup_applied = [qid for qid in merged if list(known).count(qid) > 1]

print("questions matched:", matched)
print("result ids not found in main JSON:", unmatched_results)
print("result ids applied to duplicate questions:", dup_applied)

with open(main_path, "w", encoding="utf-8") as f:
    json.dump(main, f, ensure_ascii=False, indent=2)
print("saved", main_path)