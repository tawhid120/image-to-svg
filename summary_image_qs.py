import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\image_questions_report.json', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    print(f"Question {it['n']} ({it['type']}):")
    print(f"  URLs: {it['urls']}")
    print(f"  Defect: {it['has_defect_keyword']}")
    print(f"  Statement: {it['q'][:100]}")
