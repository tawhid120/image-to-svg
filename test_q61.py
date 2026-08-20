with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_viewer.html', encoding='utf-8') as f:
    html = f.read()

import json, re
idx = html.find('const DATA = ')
if idx != -1:
    end = html.find(';\n', idx)
    data = json.loads(html[idx + len('const DATA = '):end])
    q61 = data['questions'][60]
    print("Q61 Number:", q61['n'])
    print("Q61 Raw Text:\n" + q61['q'])
    print("Q61 Options:", q61['o'])
    print("Q61 Answer:", q61['a'])
    print("Q61 Explanation:\n" + q61['e'])
