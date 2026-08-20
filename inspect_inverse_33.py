import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

nums = [3, 5, 7, 12, 26, 29, 30, 31, 36, 37, 41, 47, 59, 63, 70, 73, 78, 85, 86, 93, 95, 101, 102, 105, 121, 151, 171, 179, 192, 205, 212, 548, 620]

for n in nums:
    q = data['questions'][n - 1]
    print(f"=== Q{n} ===")
    print("Q:", q['q'])
    print("O:", q['o'])
    print("A:", q['a'])
    print("E:", q['e'])
    print()
