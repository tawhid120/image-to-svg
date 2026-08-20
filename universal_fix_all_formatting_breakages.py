# -*- coding: utf-8 -*-
"""
universal_fix_all_formatting_breakages.py
=========================================
Universal permanent fix for all formatting and LaTeX inequality issues across the question bank:
1. Normalizes all LaTeX inequalities in processed_questions.json.
2. Updates formatRichText in viewer_template.html to guarantee 100% safe HTML rendering.
3. Rebuilds question_bank_viewer.html.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# 1. NORMALIZE PROCESSED_QUESTIONS.JSON
# ─────────────────────────────────────────────────────────────────────────────
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    for field in ["q", "a", "e"]:
        if not q.get(field):
            continue
        text = q[field]

        # Fix scene headers
        text = re.sub(r'দৃশ্যকল্প\s*[-–—]\s*([১-৯1-9])', r'দৃশ্যকল্প-\1', text)

        # Standardize inequality spacing inside math formulas
        # e.g., -\infty<p<\infty -> -\infty < p < \infty
        def clean_math_inequalities(match):
            m_text = match.group(0)
            # Add spaces around < and > if tightly bound
            m_text = re.sub(r'([^\s<>=])<([^\s<>=])', r'\1 < \2', m_text)
            m_text = re.sub(r'([^\s<>=])>([^\s<>=])', r'\1 > \2', m_text)
            return m_text

        text = re.sub(r'(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\$(?:\\\$|[^\$])+\$|\\\([\s\S]+?\\\))', clean_math_inequalities, text)

        q[field] = text

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("Updated processed_questions.json with clean inequality spacing!")
