with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_viewer.html', encoding='utf-8') as f:
    html = f.read()

assert 'cinemaCanvas' in html, "Missing cinemaCanvas"
assert 'CanvasStudio' in html, "Missing CanvasStudio engine"
assert 'renderTriangleMotion' in html, "Missing renderTriangleMotion"
assert 'renderIntervalMotion' in html, "Missing renderIntervalMotion"
assert 'cinemaScrubProgress' in html, "Missing scrub progress"
print("HTML5 Canvas Motion Studio successfully integrated and verified!")
