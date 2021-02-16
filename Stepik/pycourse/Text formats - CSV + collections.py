import csv
import pandas as pd

with open('students.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open('students_programmed.tsv') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)

students = [
    ['Greg', 'Dean', 70, 80, 90, 'good job, Greg', 'adad'],
    ['Wirt', 'Wood', 80, 80.4, 82, 'Nice']
]

#  запись в файл
with open('students.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    for student in students:
        writer.writerow(student)
