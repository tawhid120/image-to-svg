import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

mcqs_with_intervals = []

for q in qs:
    if q['t'] == 0:
        qtext = q['q']
        exp = q['e'] or ''
        combined = qtext + " " + exp
        
        # Check if it solves an equation with interval condition
        # Look for <, <=, \le, \leq, ব্যবধি, যখন, চতুর্ভাগ, etc.
        has_bound = False
        
        if any(w in qtext for w in ['<', '>', '\\le', '\\leq', '\\ge', '\\geq', 'ব্যবধিতে', 'ব্যবধি', 'সীমা', 'পরিসর', 'চতুর্ভাগ']):
            # Filter out pure definitions of domain/range
            if 'ডোমেন' in qtext and '=' not in qtext:
                continue
            if 'মুখ্যমানের সীমা' in qtext and '=' not in qtext:
                continue
            if 'এর রেঞ্জ' in qtext and '=' not in qtext:
                continue
            has_bound = True
        
        if has_bound:
            mcqs_with_intervals.append(q)

print(f"Total MCQs with bounds / intervals: {len(mcqs_with_intervals)}")
for q in mcqs_with_intervals:
    print(f"Q{q['n']}: Q={q['q']}")
    print(f"       Ans={q['a']}")
