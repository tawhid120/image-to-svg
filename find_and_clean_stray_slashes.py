# -*- coding: utf-8 -*-
"""
find_and_clean_stray_slashes.py
===============================
Finds and cleans all stray trailing backslashes, stray slash artifacts,
and duplicate phrases like "যে, যে," across all 943 questions.
"""

import json
import re

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned_count = 0

for q in data["questions"]:
    for field in ["q", "a", "e"]:
        if not q.get(field):
            continue
        text = q[field]
        orig_text = text

        # 1. Clean stray trailing backslashes at line endings (e.g. "প্রমাণ কর যে, \\\n")
        # Match backslash preceded by whitespace or punctuation and followed by newline/end
        text = re.sub(r'([,।?!;:\s])\\+(\s*\n|\s*$)', r'\1\2', text)
        text = re.sub(r'\s*\\+(\s*\n|\s*$)', r'\1', text)

        # 2. Clean duplicated Bengali phrases like "যে, যে," or "যে যে"
        text = re.sub(r'যে,\s*যে,', 'যে,', text)
        text = re.sub(r'যে\s+যে,', 'যে,', text)

        # 3. Clean stray solitary backslashes before math or lines
        text = re.sub(r'\\\s*\n', '\n', text)

        if text != orig_text:
            cleaned_count += 1
            q[field] = text

with open("processed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Cleaned stray slashes/backslashes and duplicate words in {cleaned_count} questions!")
