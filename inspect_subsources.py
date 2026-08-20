import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['data']['questions']

subsource_samples = []
subsource_types = set()

for i, q in enumerate(qs):
    subs = q.get('question_subsources') or []
    formatted_sources = []
    for s in subs:
        sub_source = s.get('sub_source') or {}
        name = sub_source.get('name') or ''
        desc = sub_source.get('description') or ''
        source_obj = sub_source.get('source') or {}
        source_name = source_obj.get('name') or ''
        year = (s.get('year') or {}).get('name') or ''
        
        # e.g., 'DB 2022' or 'Dhaka Board 2022' or 'BUET 2019-20'
        formatted_sources.append({
            'name': name,
            'desc': desc,
            'source_name': source_name,
            'year': year
        })
        subsource_types.add(source_name)
    if i < 15:
        subsource_samples.append((i+1, formatted_sources))

print('Source types found:', subsource_types)
print('First 10 subsource samples:')
for num, subs in subsource_samples[:10]:
    print(f'Q{num}:', subs)
