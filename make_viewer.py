# -*- coding: utf-8 -*-
"""JSON -> standalone viewer generator.

Reads the enriched question bank JSON and produces a single self-contained
HTML file (question_bank_viewer.html) with all data and local KaTeX assets embedded.
Runs without requiring any internet connection.
"""
import base64
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PROCESSED_JSON = os.path.join(HERE, "processed_questions.json")
OUT = os.path.join(HERE, "question_bank_viewer.html")
KATEX_DIR = os.path.join(HERE, "katex_dist")
KATEX_VER = "0.16.11"

CDN_CSS = "https://cdn.jsdelivr.net/npm/katex@{}/dist/katex.min.css".format(KATEX_VER)
CDN_JS = "https://cdn.jsdelivr.net/npm/katex@{}/dist/katex.min.js".format(KATEX_VER)

def katex_assets():
    """Return (css_text, js_text) with KaTeX embedded locally, else CDN tags."""
    if not os.path.isdir(KATEX_DIR):
        print("warning: katex_dist/ not found - using CDN fallback")
        return ('<link rel="stylesheet" href="%s">' % CDN_CSS,
                '<script src="%s"></script>' % CDN_JS)

    with open(os.path.join(KATEX_DIR, "katex.min.css"), encoding="utf-8") as f:
        css = f.read()

    def repl(m):
        fname = m.group(1)
        font_path = os.path.join(KATEX_DIR, "fonts", fname)
        if os.path.exists(font_path):
            with open(font_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            return "url(data:font/woff2;base64," + b64 + ")"
        return m.group(0)

    css = re.sub(r"url\(fonts/([^)]+?\.woff2)\)", repl, css)
    css = re.sub(r',url\(fonts/[^)]*?\.(?:woff|ttf)\) format\("[^"]*"\)', "", css)
    with open(os.path.join(KATEX_DIR, "katex.min.js"), encoding="utf-8") as f:
        js = f.read()
    return "<style>" + css + "</style>", "<script>" + js + "</script>"

def main():
    if not os.path.exists(PROCESSED_JSON):
        # Run process_question_bank.py first
        import process_question_bank
        process_question_bank.main()

    with open(PROCESSED_JSON, encoding="utf-8") as f:
        data = json.load(f)

    stats = data["stats"]
    questions = data["questions"]
    total = len(questions)

    payload = json.dumps({"stats": stats, "questions": questions}, ensure_ascii=False)
    payload = payload.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

    with open(os.path.join(HERE, "viewer_template.html"), encoding="utf-8") as f:
        template = f.read()

    css_tag, js_tag = katex_assets()
    html = template.replace("__KATEX_CSS__", css_tag).replace("__KATEX_JS__", js_tag)
    html = html.replace("__APP_DATA__", payload)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print("Successfully generated {} ({:.2f} MB, {} questions, all {} solved)".format(
        OUT, os.path.getsize(OUT) / 1048576, total, stats.get("solved", total)
    ))

if __name__ == "__main__":
    main()
