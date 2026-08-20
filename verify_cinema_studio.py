with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_viewer.html', encoding='utf-8') as f:
    html = f.read()

assert 'CinemaStudio' in html, "Missing CinemaStudio"
assert 'cinemaMathFlow' in html, "Missing cinemaMathFlow"
assert 'cinemaTriStage' in html, "Missing cinemaTriStage"
assert 'cinemaNlStage' in html, "Missing cinemaNlStage"
assert 'math-motion-row' in html, "Missing math-motion-row"
print("KaTeX Math Motion CinemaStudio verified successfully!")
