import json

with open("processed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["n"] == 546:
        q["o"] = [
            "![চিত্র](https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/pure_vector_v2/vec_546_1.png?v=20260818_fresh)",
            "![চিত্র](https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/pure_vector_v2/vec_546_2.png?v=20260818_fresh)",
            "![চিত্র](https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/pure_vector_v2/vec_546_3.png?v=20260818_fresh)",
            "![চিত্র](https://ik.imagekit.io/9fi8p9fvr/math_2nd_ch7/pure_vector_v2/vec_546_4.png?v=20260818_fresh)"
        ]
        break

with open("processed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Q546 options with pure vector URLs!")
