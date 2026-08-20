import json, re

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

no_dollar_latex = []
slash_delimiters = []
defects = []
unanswered = []
subsource_counts = 0

for i, q in enumerate(qs, 1):
    qtext = blocks_text(q.get('question_text'))
    ans = blocks_text(q.get('answer_text'))
    exp = blocks_text(q.get('explanation_text'))
    opts = [blocks_text(o) for o in (q.get('option') or [])]
    subsources = q.get('question_subsources') or []
    if subsources:
        subsource_counts += 1
    
    idx = q.get('mcq_solution_index')
    is_mcq = q.get('question_type', {}).get('name') == 'বহুনির্বাচনি প্রশ্ন'
    
    if is_mcq and (idx is None or idx < 0 or idx >= len(opts)):
        defects.append((i, idx, len(opts), qtext[:80], ans, exp[:80]))
        
    if not ans and not exp:
        unanswered.append((i, is_mcq, qtext[:80]))

    all_texts = [('q', qtext), ('a', ans), ('e', exp)] + [('o' + str(j), o) for j, o in enumerate(opts)]
    for tag, t in all_texts:
        if r'\(' in t or r'\[' in t:
            slash_delimiters.append((i, tag, t[:80]))
        # Check for LaTeX commands outside dollar signs
        stripped = re.sub(r'\$\$[\s\S]+?\$\$|\$[\s\S]+?\$', '', t)
        if re.search(r'\\(?:frac|sin|cos|tan|cot|sec|cosec|csc|theta|alpha|beta|pi|sqrt|pm|le|ge|neq|times|cdot|in|mathbb|mathrm|text|left|right)\b', stripped):
            no_dollar_latex.append((i, tag, stripped.strip()[:100]))

print(f'Total questions: {len(qs)}')
print(f'Questions with subsources: {subsource_counts}')
print(f'Slash delimiters \\( or \\[: {len(slash_delimiters)}')
if slash_delimiters:
    print('Sample slash delimiter:', slash_delimiters[:5])
print(f'Un-dollared LaTeX commands: {len(no_dollar_latex)}')
if no_dollar_latex:
    print('Sample un-dollared LaTeX:')
    for item in no_dollar_latex[:10]:
        print('  ', item)
print(f'Defective MCQ index: {len(defects)}')
if defects:
    print('Sample defects (first 10):')
    for d in defects[:10]:
        print('  ', d)
print(f'Unanswered questions: {len(unanswered)}')
if unanswered:
    print('Sample unanswered:', unanswered[:10])
