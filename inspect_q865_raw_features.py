import json
import os
from PIL import Image

# Let's inspect q_865_img_1.png and print its details
p = os.path.join("downloaded_diagrams", "q_865_img_1.png")
im = Image.open(p)
print("q_865_img_1 size:", im.size)

# Also let's inspect the exact question stem for 865, 867, 883, 884, 885
with open("processed_questions.json", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["n"] in [865, 867, 883, 884, 885]:
        print(f"=== Q{q['n']} ===")
        print(q["q"])
        print()
