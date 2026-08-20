import json
import re

with open("question_bank_viewer.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract json inside DATA
m = re.search(r"const DATA = ({.*?});", html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print("Found DATA in HTML!")
    for q in data["questions"]:
        if q["n"] in [819, 865, 746, 863]:
            print(f"=== Q{q['n']} in HTML ===")
            print(q["q"])
            print()
else:
    print("DATA not found!")
