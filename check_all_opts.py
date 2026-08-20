import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['data']['questions']

print("Total questions:", len(qs))
for i, q in enumerate(qs, 1):
    q_type = q.get('question_type', {}).get('name')
    ans = q.get('answer_text')
    exp = q.get('explanation_text')
    idx = q.get('mcq_solution_index')
    opts = q.get('option') or []
    if q_type == 'বহুনির্বাচনি প্রশ্ন':
        if len(opts) < 4:
            print(f'Q{i} has fewer than 4 options: {len(opts)}')
