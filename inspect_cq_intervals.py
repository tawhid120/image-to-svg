import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

cq_interval_list = []
for q in qs:
    if q['t'] == 1: # CQ
        qtext = q['q']
        if any(w in qtext for w in ['ব্যবধি', 'ব্যবধিতে', 'সীমা', 'পরিসর', 'শর্তে']) or any(b in qtext for b in ['[0', '[-', '<= 2\pi', '<= \pi']):
            cq_interval_list.append(q)

print(f"Total CQ questions with interval terms: {len(cq_interval_list)}")
for q in cq_interval_list[:15]:
    print(f"\nQ{q['n']}:")
    print("Q:", q['q'][:120])
    print("Ans:", q['a'][:100])
