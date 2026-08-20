import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "question_bank_HSC_Admission_HSC_-_পদার্থ_বিজ্ঞান_২য়_পত্র_অধ্যায়-০২ঃ_স্থির_তড়িৎ.json")
WORKDIR = os.path.join(BASE, "physics_work")
os.makedirs(WORKDIR, exist_ok=True)

with open(SRC, encoding="utf-8") as f:
    data = json.load(f)
with open(os.path.join(WORKDIR, "image_map.json"), encoding="utf-8") as f:
    image_map = json.load(f)

questions = data["data"]["questions"]

def block_text(b):
    return b.get("text", "")

def draft_text(d):
    if not d:
        return ""
    return "\n".join(block_text(b) for b in d.get("blocks", []))

def opt_text(o):
    if isinstance(o, str):
        return o
    return draft_text(o).strip() or "(empty option)"

def extract_subsources(q):
    parts = []
    for ss in q.get("question_subsources", []) or []:
        sub = ss.get("sub_source", {})
        name = sub.get("name", "")
        desc = sub.get("description", "")
        year = (ss.get("year") or {}).get("name", "")
        src = (sub.get("source") or {}).get("name", "")
        parts.append(f"{name} ({desc}) {year} [{src}]")
    return "; ".join(parts) if parts else ""

recs = []
for q in questions:
    qt = q.get("question_text") or {}
    qtext = draft_text(qt)
    opts = q.get("option") or []
    rec = {
        "n": len(recs) + 1,
        "id": q["id"],
        "type": (q.get("question_type") or {}).get("name", ""),
        "q": qtext,
        "options": [opt_text(o) for o in opts],
        "images": image_map.get(q["id"], []),
        "src": extract_subsources(q),
    }
    recs.append(rec)

with open(os.path.join(WORKDIR, "questions_info.json"), "w", encoding="utf-8") as f:
    json.dump(recs, f, ensure_ascii=False, indent=1)

print("total:", len(recs))
print("with images:", sum(1 for r in recs if r["images"]))
print("MCQ:", sum(1 for r in recs if r["type"] == "বহুনির্বাচনি প্রশ্ন"))
print("সৃজনশীল:", sum(1 for r in recs if r["type"] == "সৃজনশীল প্রশ্ন"))
print("গাণিতিক:", sum(1 for r in recs if r["type"] == "গাণিতিক ও বিশ্লেষণধর্মী প্রশ্ন"))
print("জ্ঞানমূলক:", sum(1 for r in recs if r["type"] == "জ্ঞানমূলক প্রশ্ন"))