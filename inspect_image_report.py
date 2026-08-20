import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\image_questions_report.json', encoding='utf-8') as f:
    items = json.load(f)

print(f'Total questions in report: {len(items)}')
for it in items:
    print(f"Q{it['n']} ({it['type']}): urls={len(it['urls'])}, defect={it['has_defect_keyword']}")
    print(f"  Q: {it['q']}")
    print(f"  URLs: {it['urls']}")
    print(f"  A: {it['answer']}")
    print(f"  E: {it['explanation']}")
    print("=" * 80)
