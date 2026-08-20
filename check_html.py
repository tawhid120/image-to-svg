import os

file_path = r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_viewer.html'
with open(file_path, encoding='utf-8') as f:
    html = f.read()

print('File size:', os.path.getsize(file_path))
print('Has fabEyeBtn:', 'id="fabEyeBtn"' in html)
print('Has is-correct-ans:', 'is-correct-ans' in html)
print('Has modeBanner:', 'id="modeBanner"' in html)
print('Has KaTeX CSS embedded:', 'katex' in html)
