import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['data']['questions']

def get_full_text_and_images(val):
    if not val: return ''
    if isinstance(val, str): return val
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
                        imgs.append(f'![Image]({src})')
            if imgs:
                parts.append(' '.join(imgs))
            if t:
                parts.append(t)
        return '\n'.join(parts) if parts else ''
    return ''

defect_nums = [92, 126, 192, 546, 548, 582, 583, 590, 591, 618, 678, 720]

for n in defect_nums:
    q = qs[n - 1]
    print(f'================= QUESTION #{n} =================')
    print('Question:', get_full_text_and_images(q.get('question_text')))
    opts = [get_full_text_and_images(o) for o in (q.get('option') or [])]
    for idx, opt in enumerate(opts):
        print(f'  Opt {idx} ({["ক","খ","গ","ঘ"][idx]}): {opt}')
    print('Current Answer:', get_full_text_and_images(q.get('answer_text')))
    print('Current Explanation:', get_full_text_and_images(q.get('explanation_text')))
    print('Subsources:', q.get('question_subsources'))
    print()
