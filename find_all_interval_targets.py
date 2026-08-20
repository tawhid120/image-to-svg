import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

target_qs = []

for q in qs:
    qtext = q['q']
    exp = q['e'] or ''
    
    has_interval = False
    if re.search(r'(-\\pi|0|\\pi|2\\pi|90|180|360|\\frac\{\\pi\}\{2\})\s*(\\le|\\leq|<|<=)\s*(x|\\theta|\\mathrm\{x\}|y)\s*(\\le|\\leq|<|<=)\s*(-\\pi|0|\\pi|2\\pi|90|180|360|\\frac\{\\pi\}\{2\})', qtext):
        has_interval = True
    elif re.search(r'\[\s*(-\\pi|0)\s*,\s*(\\pi|2\\pi|360|\d+|\\frac\{\\pi\}\{2\})\s*\]', qtext):
        has_interval = True
    elif ('ব্যবধি' in qtext or 'সীমা' in qtext) and any(trig in qtext for trig in ['\\sin', '\\cos', '\\tan', '\\cot', '\\sec', 'cosec']) and ('সমীকরণ' in qtext or 'সমাধান' in qtext):
        has_interval = True
    elif 'যখন' in qtext and re.search(r'(-\\pi|0|\\pi|2\\pi)\s*(<|<=|\\le|\\leq)\s*(x|\\theta)\s*(<|<=|\\le|\\leq)\s*(-\\pi|0|\\pi|2\\pi)', qtext):
        has_interval = True

    if has_interval:
        if 'ডোমেন' in qtext and 'এক এক' in qtext:
            continue
        target_qs.append(q)

print(f"Total target interval equation questions: {len(target_qs)}")
for item in target_qs:
    print(f"Q{item['n']} (t={item['t']}): {item['q'][:90]}")
