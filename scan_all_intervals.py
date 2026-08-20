import json, re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

all_interval_qs = []

# List of triggers
for q in qs:
    qtext = q['q']
    exp = q['e'] or ''
    ans = q['a'] or ''
    combined = qtext + " " + exp + " " + ans
    
    # Check if it has trigonometric terms
    has_trig = any(t in combined for t in ['\\sin', '\\cos', '\\tan', '\\cot', '\\sec', 'cosec', 'sin', 'cos', 'tan', 'cot', 'sec'])
    if not has_trig:
        continue
        
    # Check for interval indicators
    has_interval = False
    
    # 1. Inequality with <, <=, \le, \leq
    if re.search(r'(<|<=|\\le|\\leq)\s*(\w+|\\theta|\\mathrm\{x\}|x|y)\s*(<|<=|\\le|\\leq)', combined):
        has_interval = True
    elif re.search(r'(\d+|\\pi|\\frac\{\\pi\}\{\d+\}|-\s*\\pi)\s*(<|<=|\\le|\\leq)\s*(\w+|\\theta|x|y)', combined):
        has_interval = True
    elif re.search(r'(\w+|\\theta|x|y)\s*(<|<=|\\le|\\leq)\s*(\d+|\\pi|2\\pi|\\frac\{\\pi\}\{\d+\}|360|180|90)', combined):
        has_interval = True
    elif re.search(r'\[\s*(-?\s*\\pi|-?\s*\d+|0)\s*,\s*(\\pi|2\s*\\pi|360|180|90|\\frac\{\\pi\}\{\d+\}|\d+)\s*\]', combined):
        has_interval = True
    elif re.search(r'\(\s*(-?\s*\\pi|-?\s*\d+|0)\s*,\s*(\\pi|2\s*\\pi|360|180|90|\\frac\{\\pi\}\{\d+\}|\d+)\s*\)', combined):
        # make sure it's not just open interval for tan domain
        if 'সমাধান' in combined or 'মান' in combined or 'হলে' in combined:
            has_interval = True
    elif any(word in combined for word in ['ব্যবধি', 'ব্যবধিতে', 'সীমা', 'পরিসর', 'চতুর্ভাগ', 'চতুর্ভাগে']):
        if 'সমাধান' in combined or 'মান কত' in combined or 'সমীকরণ' in combined:
            has_interval = True

    # Filter out pure inverse trig definition questions if they don't involve solving equations
    if 'ডোমেন' in qtext and 'এক এক' in qtext and 'সমীকরণ' not in qtext:
        has_interval = False
    if 'মুখ্যমানের সীমা' in qtext and 'সমীকরণ' not in qtext and '=' not in qtext:
        has_interval = False
    if 'এর রেঞ্জ' in qtext and 'সমীকরণ' not in qtext:
        has_interval = False

    if has_interval:
        all_interval_qs.append(q)

print(f"Found {len(all_interval_qs)} interval-based questions in total.")
for q in all_interval_qs:
    print(f"Q{q['n']} (t={q['t']}): Q = {q['q'][:80]}")
