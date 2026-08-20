import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

found_list = []

for q in qs:
    qtext = q['q']
    exp = q['e'] or ''
    combined = qtext + " " + exp
    
    # Check if question has trigonometric equation solving with specific angles/intervals
    # Criteria:
    # 1. Contains trig equation like sin x = ..., cos x = ..., tan x = ...
    # 2. Asks for angle value(s) in an interval or quadrant
    if any(trig in qtext for trig in ['\\sin', '\\cos', '\\tan', '\\cot', '\\sec', 'cosec', 'sin', 'cos', 'tan', 'cot', 'sec']):
        if any(b in qtext for b in ['<', '>', '\\le', '\\leq', '\\ge', '\\geq', 'ব্যবধি', 'সীমা', 'পরিসর', 'চতুর্ভাগ', '[', '(']):
            if any(w in qtext for w in ['সমাধান', 'মান কত', 'মান কোনটি', 'মান হবে', 'হলে']):
                # Filter out pure inverse trig evaluation like tan(sin^-1(1/2))
                if '^{-1}' in qtext and '=' not in qtext and 'ব্যবধি' not in qtext and '<' not in qtext:
                    continue
                found_list.append(q)

print(f"Found {len(found_list)} questions.")
for q in found_list:
    print(f"Q{q['n']} (t={q['t']}): {q['q']}")
