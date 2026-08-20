import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

mcq_interval_qs = []

for q in qs:
    if q['t'] == 0: # MCQ
        qtext = q['q']
        # Check if it has an interval for solving
        if any(k in qtext for k in ['ব্যবধি', 'ব্যবধিতে']) or re.search(r'(-\\pi|0|\\pi|2\\pi|90|180|360)\s*(\\le|\\leq|<|<=)\s*(x|\\theta|\\mathrm{x})\s*(\\le|\\leq|<|<=)\s*(-\\pi|0|\\pi|2\\pi|90|180|360)', qtext) or re.search(r'\[\s*(-\s*\\pi|0)\s*,\s*(\\pi|2\s*\\pi)\s*\]', qtext):
            mcq_interval_qs.append(q)

print(f"Total MCQ interval-based questions: {len(mcq_interval_qs)}")
for q in mcq_interval_qs:
    print(f"\n================ Q{q['n']} ================")
    print("Q:", q['q'])
    print("Options:", q['o'])
    print("Ans:", q['a'])
    print("Exp:", q['e'])
