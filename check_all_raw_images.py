import json
import os
from PIL import Image

# Check the properties and dimensions of all original diagram files
for f in sorted(os.listdir("downloaded_diagrams")):
    if f.endswith(".png") or f.endswith(".webp"):
        p = os.path.join("downloaded_diagrams", f)
        im = Image.open(p)
        print(f"{f}: size={im.size}, mode={im.mode}")
