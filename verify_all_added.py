import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

for num in [53, 54, 55, 628, 708, 711, 743, 744, 747, 750, 802, 934, 937, 941]:
    q = data['questions'][num - 1]
    print(f"=== Verified Q{num} ===")
    print("Q:", q['q'][:80])
    print("Explanation:\n", q['e'])
    print()
