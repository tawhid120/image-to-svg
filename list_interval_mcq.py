import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

mcq_list = []
for q in qs:
    if q['t'] == 0:
        txt = q['q']
        if any(w in txt for w in ['ব্যবধি', 'ব্যবধিতে', 'সীমা', 'পরিসর', 'শর্তে', 'যখন']) or re.search(r'(-\\pi|0|\\pi|2\\pi|90|180|360|\\frac\{\\pi\}\{2\})\s*(\\le|\\leq|<|<=)\s*(x|\\theta|\\mathrm\{x\}|y)\s*(\\le|\\leq|<|<=)\s*(-\\pi|0|\\pi|2\\pi|90|180|360|\\frac\{\\pi\}\{2\})', txt):
            if any(trig in txt for trig in ['\\sin', '\\cos', '\\tan', '\\cot', '\\sec', 'cosec', 'sin', 'cos', 'tan']):
                mcq_list.append(q)

print(f"Total interval MCQ questions: {len(mcq_list)}")
for q in mcq_list:
    print(f"\nQ{q['n']}:")
    print("Q:", q['q'])
    print("Ans:", q['a'])
    print("Old Exp:", q['e'])
