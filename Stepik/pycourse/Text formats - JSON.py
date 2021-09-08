import json

student1 = {
    'first_name': 'Greg',
    'last_name': 'Dean',
    'scores': [70, 80, 90],
    'description': 'Goood job',
    'certificate': True
}

student2 = {
    'first_name': 'Wirt',
    'last_name': 'Wood',
    'scores': [80, 80.2, 80],
    'description': 'Nicely done',
    'certificate': True
}

data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True))
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

# Сумма баллов второго студента
with open('students.json', 'r') as f:
    data_again = json.load(f)
    print(sum(data_again[1]['scores']))