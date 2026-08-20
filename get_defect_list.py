import json

with open("image_questions_report.json", encoding="utf-8") as f:
    items = json.load(f)

defect_qs = [it["n"] for it in items if it["has_defect_keyword"]]
print("Defect question numbers:", defect_qs)
print(f"Total: {len(defect_qs)}")
