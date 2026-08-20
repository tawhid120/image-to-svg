# -*- coding: utf-8 -*-
import json
import re

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total questions: {len(data['questions'])}")

# Check for < and > inside text that causes HTML tag parsing issues
issues_less_than = []
issues_broken_math = []
issues_duplicates = []

for q in data["questions"]:
    qn = q["n"]
    for field in ["q", "a", "e"]:
        val = q.get(field, "")
        if not val:
            continue
        # Check for < followed by letter or number (e.g. <x, <\pi, <2, <\theta)
        if re.search(r'<[a-zA-Z0-9\\_]', val):
            issues_less_than.append((qn, field, val))
        
        # Check for odd number of $ delimiters
        # count dollar signs not preceded by backslash
        dollar_count = len(re.findall(r'(?<!\\)\$', val))
        if dollar_count % 2 != 0:
            issues_broken_math.append((qn, field, dollar_count, val))

        # Check for single-character stacked duplicates like "a\n=\n3"
        if re.search(r'^[a-zA-Z0-9+\-=]\s*$', val, re.MULTILINE):
            issues_duplicates.append((qn, field, val))

print(f"Questions with '<' HTML tag collisions: {len(issues_less_than)}")
for qn, field, val in issues_less_than[:10]:
    print(f"  Q{qn} [{field}]: {val[:120].replace(chr(10), ' ')}")

print(f"\nQuestions with unbalanced '$' math delimiters: {len(issues_broken_math)}")
for qn, field, cnt, val in issues_broken_math[:10]:
    print(f"  Q{qn} [{field}] (count={cnt}): {val[:120].replace(chr(10), ' ')}")

print(f"\nQuestions with stacked single-character lines: {len(issues_duplicates)}")
for qn, field, val in issues_duplicates[:10]:
    print(f"  Q{qn} [{field}]: {val[:120].replace(chr(10), ' ')}")
