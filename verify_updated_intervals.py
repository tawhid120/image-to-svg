import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

test_nums = [53, 229, 334, 499, 552, 563, 566, 616, 631, 656, 706, 709, 721, 724]

for n in test_nums:
    q = data['questions'][n - 1]
    print(f"\n================ Question #{n} ================")
    print("Q:", q['q'])
    print("Ans:", q['a'])
    print("New Exp:\n", q['e'])
