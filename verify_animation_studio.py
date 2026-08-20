with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\question_bank_viewer.html', encoding='utf-8') as f:
    html = f.read()

assert 'anim-play-btn' in html, "Missing anim-play-btn"
assert 'id="animModal"' in html, "Missing animModal"
assert 'AnimStudio' in html, "Missing AnimStudio engine"
assert 'studioTriangleSvg' in html, "Missing triangle SVG visualizer"
assert 'studioVoiceBtn' in html, "Missing voice toggle"
print("Animation Studio successfully integrated and verified in standalone HTML viewer!")
