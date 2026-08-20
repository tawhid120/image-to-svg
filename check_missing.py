import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['data']['questions']

def blocks_to_html_or_text(val):
    if not val:
        return ''
    if isinstance(val, str):
        return val
    if isinstance(val, dict):
        blocks = val.get('blocks') or []
        emap = val.get('entityMap') or {}
        parts = []
        for b in blocks:
            t = (b or {}).get('text') or ''
            eranges = (b or {}).get('entityRanges') or []
            imgs = []
            for er in eranges:
                k = str(er.get('key'))
                if k in emap and emap[k].get('type') == 'IMAGE':
                    src = emap[k].get('data', {}).get('src')
                    if src:
                        imgs.append(f'![চিত্র]({src})')
            if imgs:
                parts.append(' '.join(imgs))
            if t:
                parts.append(t)
        return '\n'.join(parts) if parts else ''
    return ''

print(f'Total questions: {len(qs)}')

# Let us check for each question
missing_ans = []
missing_exp = []
for i, q in enumerate(qs, 1):
    qtext = blocks_to_html_or_text(q.get('question_text'))
    ans = blocks_to_html_or_text(q.get('answer_text'))
    exp = blocks_to_html_or_text(q.get('explanation_text'))
    idx = q.get('mcq_solution_index')
    is_mcq = q.get('question_type', {}).get('name') == 'বহুনির্বাচনি প্রশ্ন'
    if not ans:
        missing_ans.append(i)
    if not exp:
        missing_exp.append(i)

print(f'Missing ans count: {len(missing_ans)}')
print(f'Missing exp count: {len(missing_exp)}')
print('Missing ans Qs:', missing_ans[:20])
print('Missing exp Qs:', missing_exp[:20])
