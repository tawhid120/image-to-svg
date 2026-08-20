import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['data']['questions']

def format_subsources(subs):
    if not subs:
        return []
    res = []
    for s in subs:
        sub_source = s.get('sub_source') or {}
        name = sub_source.get('name') or ''
        desc = sub_source.get('description') or ''
        source_obj = sub_source.get('source') or {}
        source_name = source_obj.get('name') or ''
        year = (s.get('year') or {}).get('name') or ''
        
        # Build clean label
        label = ''
        if name and year:
            label = f"{name} '{year[-2:] if len(year)==4 else year}"
        elif name:
            label = name
        elif desc and year:
            label = f"{desc} '{year[-2:] if len(year)==4 else year}"
        elif desc:
            label = desc
        elif source_name:
            label = source_name
            
        full_title = f"{desc or name} ({year})" if year else (desc or name)
        res.append({
            "tag": label.strip(),
            "name": name.strip(),
            "desc": desc.strip(),
            "type": source_name.strip(),
            "year": year.strip(),
            "full": full_title.strip()
        })
    return res

sample_results = []
for i in range(30):
    subs = format_subsources(qs[i].get('question_subsources'))
    sample_results.append((i+1, [s['tag'] for s in subs], [s['full'] for s in subs]))

for item in sample_results[:15]:
    print(f"Q{item[0]}: tags={item[1]}, full={item[2]}")
