import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['data']['questions']

def blocks_text(value):
    if value is None: return ''
    if isinstance(value, str): return value
    if isinstance(value, dict):
        blocks = value.get('blocks') or []
        parts = []
        for b in blocks:
            t = (b or {}).get('text')
            if t: parts.append(t)
        return '\n'.join(parts) if parts else ''
    return ''

for i, q in enumerate(qs, 1):
    idx = q.get('mcq_solution_index')
    is_mcq = q.get('question_type', {}).get('name') == 'বহুনির্বাচনি প্রশ্ন'
    opts = [blocks_text(o) for o in (q.get('option') or [])]
    if is_mcq and (idx is None or idx < 0 or idx >= len(opts)):
        print(f'=== QUESTION #{i} (index={idx}, num_opts={len(opts)}) ===')
        print('Q:', blocks_text(q.get('question_text')))
        print('Options:', opts)
        print('Answer:', repr(blocks_text(q.get('answer_text'))))
        print('Explanation:', repr(blocks_text(q.get('explanation_text'))))
        print('Subsources:', q.get('question_subsources'))
        print()
