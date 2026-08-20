import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

interval_questions = []

for q in qs:
    qtext = q['q']
    is_interval = False
    
    # Check if question text specifies an interval for trigonometric solving
    if any(k in qtext for k in ['ব্যবধি', 'ব্যবধিতে', 'সীমা', 'পরিসরে', 'শর্তে']):
        is_interval = True
    elif re.search(r'(-\\pi|0|\\pi|2\\pi|90|180|360)\s*(\\le|\\leq|<|<=)\s*(x|\\theta|y)\s*(\\le|\\leq|<|<=)\s*(-\\pi|0|\\pi|2\\pi|90|180|360)', qtext):
        is_interval = True
    elif re.search(r'\[\s*(-\s*\\pi|0)\s*,\s*(\\pi|2\s*\\pi)\s*\]', qtext):
        is_interval = True
    elif 'যখন' in qtext and re.search(r'(\\le|\\leq|<|<=)', qtext) and any(trig in qtext for trig in ['\\sin', '\\cos', '\\tan', '\\cot', '\\sec', 'cosec']):
        is_interval = True
    elif re.search(r'(\d+°?|\d+\\pi)\s*<\s*(\w+|\\theta)\s*<\s*(\d+°?|\d+\\pi)', qtext):
        is_interval = True

    if is_interval:
        interval_questions.append(q)

print(f'Total interval-based questions found: {len(interval_questions)}')
for item in interval_questions:
    print(f"Q{item['n']} (type={item['t']}): Q={item['q'][:70]} | Ans={item['a'][:40]} | Exp={item['e'][:60]}...")
