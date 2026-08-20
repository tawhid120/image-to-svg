import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

substituted_qs = []

for q in qs:
    exp = q['e'] or ''
    qtext = q['q'] or ''
    # Check if explanation uses dummy variable substitution for inverse trig
    if re.search(r'ধরি.*?(?:\\alpha|\\theta|\\beta|\b\w\b)\s*=\s*(?:\\sin\^\{-1\}|\\cos\^\{-1\}|\\tan\^\{-1\}|\\cot\^\{-1\}|\\sec\^\{-1\}|\\operatorname\{cosec\}\^\{-1\}|cosec\^\{-1\})', exp):
        substituted_qs.append(q)
    elif re.search(r'(?:\\sin|\\cos|\\tan|\\cot|\\sec|\\operatorname\{cosec\})\s*(?:\^2\s*)?\(\s*(?:\\sin\^\{-1\}|\\cos\^\{-1\}|\\tan\^\{-1\}|\\cot\^\{-1\}|\\sec\^\{-1\}|\\operatorname\{cosec\}\^\{-1\})', qtext):
        if q not in substituted_qs:
            substituted_qs.append(q)

print(f"Total questions identified: {len(substituted_qs)}")
for q in substituted_qs[:25]:
    print(f"Q{q['n']}: Q={q['q'][:60]} | Exp={q['e'][:80]}...")
