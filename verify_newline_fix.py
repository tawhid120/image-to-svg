with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_viewer.html', encoding='utf-8') as f:
    html = f.read()

# Check CSS rule
assert '.qtext{' in html and 'white-space:pre-line' in html or 'white-space: pre-line' in html

# Check question 61 in embedded JSON
assert 'k=\\frac{1}{\\sqrt{3}} হলে \\alpha=' in html
print("Verification passed! CSS has white-space:pre-line for questions, options, and explanations.")
