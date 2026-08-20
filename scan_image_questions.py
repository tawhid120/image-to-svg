import json
import re

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

image_questions = []
for q in data['questions']:
    full_text = q.get('q', '') + ' ' + q.get('e', '') + ' ' + q.get('a', '') + ' ' + ' '.join(q.get('o', []))
    has_img = '![চিত্র]' in full_text or ('http' in full_text and ('.png' in full_text or '.jpg' in full_text or 'firebasestorage' in full_text or 'firebase' in full_text))
    has_defect_keyword = 'চিত্র অনুপস্থিত' in full_text or 'চিত্র দেখা যাচ্ছে না' in full_text or 'চিত্র ছাড়া' in full_text or 'চিত্রনির্ভর' in full_text or 'চিত্র নির্ভর' in full_text
    
    # Extract image URLs
    img_urls = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', full_text)
    raw_urls = re.findall(r'https?://[^\s\)\"\']+(?:\.png|\.jpg|\.jpeg|firebasestorage[^\s\)\"\']+)', full_text)
    all_urls = list(set(img_urls + raw_urls))
    
    if has_img or has_defect_keyword or all_urls:
        image_questions.append({
            'n': q['n'],
            'type': 'MCQ' if q['t'] == 0 else 'CQ',
            'q': q['q'],
            'options': q.get('o', []),
            'answer': q.get('a', ''),
            'explanation': q.get('e', ''),
            'urls': all_urls,
            'has_defect_keyword': has_defect_keyword
        })

print(f'Total questions found: {len(image_questions)}')
with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\image_questions_report.json', 'w', encoding='utf-8') as out:
    json.dump(image_questions, out, ensure_ascii=False, indent=2)

for item in image_questions:
    print(f"Q{item['n']} ({item['type']}): urls={len(item['urls'])}, defect_keyword={item['has_defect_keyword']}")
    print(f"  Q: {item['q'][:120]}")
    if item['urls']:
        print(f"  URLs: {item['urls']}")
    print(f"  A: {item['answer']}")
    print(f"  E: {item['explanation'][:120]}")
    print("-" * 60)
