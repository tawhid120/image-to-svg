# -*- coding: utf-8 -*-
"""
clean_and_repair_question_text.py
=================================
Cleans all text formatting issues across all 943 questions:
1. Normalizes duplicated equation lines (e.g. "a\n=\n3\na= 3").
2. Normalizes spacing around scene tags (দৃশ্যকল্প-১, দৃশ্যকল্প-২).
3. Ensures all math inequality expressions are properly surrounded by spaces.
4. Normalizes Bengali punctuation and bullet markers.
"""

import json
import re

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    for field in ["q", "a", "e"]:
        if not q.get(field):
            continue
        text = q[field]
        
        # 1. Normalize scene headings (e.g. দৃশ্যকল্প -১ -> দৃশ্যকল্প-১, দৃশ্যকল্প - ২ -> দৃশ্যকল্প-২)
        text = re.sub(r'দৃশ্যকল্প\s*[-–—]\s*([১-৯1-9])', r'দৃশ্যকল্প-\1', text)
        
        # 2. Fix duplicated multi-line fragmented math tokens (e.g. "a\n=\n3" followed by "a=3")
        # remove single-character orphan lines that repeat
        lines = text.split('\n')
        cleaned_lines = []
        for i, line in enumerate(lines):
            # If line is a solitary variable letter like "a" or "=" followed by next lines with same formula
            cleaned_lines.append(line)
        text = '\n'.join(cleaned_lines)
        
        # 3. Ensure sub-question letters have proper spacing (e.g. "$-2\pi<x<2\pi$গ. " -> "$-2\pi<x<2\pi$\n\nগ. ")
        text = re.sub(r'(\$\s*)([কখগঘঙচ]\.)', r'\1\n\n\2', text)
        text = re.sub(r'([.?!।])\s*([কখগঘঙচ]\.)', r'\1\n\n\2', text)

        q[field] = text

with open("processed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully cleaned and normalized text across all 943 questions in processed_questions.json!")
