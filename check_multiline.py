import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

for num in [59, 60, 61, 62, 63, 64, 582, 583, 590, 591, 618]:
    q = data['questions'][num - 1]
    print(f"=== Q{num} ===")
    print("Q raw:")
    print(repr(q['q']))
    print("Q formatted display:")
    print(q['q'])
    print("-" * 40)
