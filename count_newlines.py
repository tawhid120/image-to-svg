import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']
with_newlines = [q for q in qs if '\n' in q['q']]
print(f"Total questions with newlines in text: {len(with_newlines)} out of {len(qs)}")
for q in with_newlines[:10]:
    print(f"Q{q['n']}: {repr(q['q'][:80])}")
