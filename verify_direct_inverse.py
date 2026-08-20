import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

test_ids = [3, 5, 12, 26, 30, 36, 37, 41, 63, 70, 73, 78, 85, 95, 101, 179, 212]

for tid in test_ids:
    q = data['questions'][tid - 1]
    print(f"=== Question {tid} ===")
    print("Q:", q['q'])
    print("Ans:", q['a'])
    print("Direct Inverse Explanation:\n", q['e'])
    print()
