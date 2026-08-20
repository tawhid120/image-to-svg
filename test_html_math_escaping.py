# -*- coding: utf-8 -*-
"""
test_html_math_escaping.py
"""
import re

def escapeHtml(s):
    return (s or "").replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def formatRichText_Universal(raw):
    if not raw:
        return ""
    str_val = raw.replace('\r\n', '\n').replace('\r', '\n')

    # 1. Protect Markdown Tables
    tables = []
    # 2. Protect Images
    images = []
    def save_img(m):
        idx = len(images)
        images.append(f'<img src="{m.group(2)}" alt="{escapeHtml(m.group(1))}" loading="lazy" class="q-img">')
        return f'___IMG_PH_{idx}___'
    str_val = re.sub(r'!\[(.*?)\]\((.*?)\)', save_img, str_val)

    # 3. ESCAPE ALL HTML in the ENTIRE string! (This converts < to &lt; everywhere, including inside $...$)
    str_val = escapeHtml(str_val)

    # 4. Headings & Dividers
    str_val = re.sub(r'^---\s*$', '<hr class="expl-divider">', str_val, flags=re.M)
    str_val = re.sub(r'^####\s+(.+)$', r'<h5 class="expl-h4">\1</h5>', str_val, flags=re.M)
    str_val = re.sub(r'^###\s+(.+)$', r'<h4 class="expl-h3">\1</h4>', str_val, flags=re.M)

    # 5. Bold
    str_val = re.sub(r'\*\*([\s\S]+?)\*\*', r'<b>\1</b>', str_val)

    # 6. Bullet Points
    str_val = re.sub(r'^[ \t]*[\*•][ \t]+(.+)$', r'<div class="expl-bullet"><span class="bullet-dot">•</span><span class="bullet-text">\1</span></div>', str_val, flags=re.M)
    str_val = re.sub(r'^[ \t]*(\d+|[১-৯])\.[ \t]+(.+)$', r'<div class="expl-bullet"><span class="bullet-num">\1.</span><span class="bullet-text">\2</span></div>', str_val, flags=re.M)

    # 7. Line breaks
    str_val = str_val.replace('\n\n', '<div class="expl-spacer"></div>').replace('\n', '<br>')

    # 8. Restore Images
    for idx, img in enumerate(images):
        str_val = str_val.replace(f'___IMG_PH_{idx}___', img)

    return str_val

q752_raw = "দৃশ্যকল্প-১: $q=\\tan ^{-1} p,-\\infty<p<\\infty$.\nদৃশ্যকল্প-২: $f(x)=\\cot \\left(\\frac{\\pi}{2}-x\\right)$"
result = formatRichText_Universal(q752_raw)
print("Q752 Output HTML:")
print(result)
