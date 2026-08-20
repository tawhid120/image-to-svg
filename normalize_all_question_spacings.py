# -*- coding: utf-8 -*-
"""
normalize_all_question_spacings.py
==================================
Normalizes all line breaks and paragraph spacing across all 943 questions so that:
- Spacing between stimulus (উদ্দীপক) and sub-questions is uniform.
- Spacing between ক., খ., গ., ঘ. is 100% consistent (no uneven tight/wide gaps).
- Replaces 3+ consecutive newlines with clean double newlines.
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

        # 1. Clean up excessive consecutive newlines (3+ -> 2)
        text = re.sub(r'\n{3,}', '\n\n', text)

        # 2. Normalize sub-question breaks (ক., খ., গ., ঘ., ঙ., চ.)
        # Ensure each sub-question starts on its own line preceded by exactly \n\n
        def sub_q_repl(match):
            prefix = match.group(1)
            letter = match.group(2)
            return f"{prefix}\n\n{letter}"

        # If preceded by any character, make it \n\n
        text = re.sub(r'([^\n])\s*\n\s*([কখগঘঙচ]\.)', r'\1\n\n\2', text)
        text = re.sub(r'([^\n])\s*([কখগঘঙচ]\.)', r'\1\n\n\2', text)

        # Re-clean any accidental triple newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Clean leading and trailing whitespace per line
        lines = [l.strip() for l in text.split('\n')]
        text = '\n'.join(lines)
        text = re.sub(r'\n{3,}', '\n\n', text)

        q[field] = text.strip()

with open("processed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully normalized question spacing across all 943 questions!")
