import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

for i in range(50, 60):
    q = data['questions'][i]
    print(f"=== Q{q['n']} ===")
    print("  Q:", q['q'])
    print("  Options:", q['o'])
    print("  Ans:", q['a'])
    print("  Exp:", q['e'])
    print()
