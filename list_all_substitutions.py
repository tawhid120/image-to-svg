import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

all_sub_qs = []
for q in qs:
    exp = q['e'] or ''
    qtext = q['q'] or ''
    ans = q['a'] or ''
    # Check if uses variable substitution for inverse trig
    if 'ধরি' in exp and any(sym in exp for sym in ['\\alpha', '\\theta', '\\beta', 'alpha', 'theta']):
        all_sub_qs.append(q)

print(f"Total matching questions: {len(all_sub_qs)}")
for q in all_sub_qs:
    print(f"Q{q['n']}: {q['q'][:70]}")
