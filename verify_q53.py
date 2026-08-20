import json

with open(r'C:\Users\WALTON\Downloads\dari-backup\dari\processed_questions.json', encoding='utf-8') as f:
    data = json.load(f)

q53 = data['questions'][52]
print('=== Question 53 verification ===')
print('n:', q53['n'])
print('q:', q53['q'])
