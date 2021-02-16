import os
import os.path


"""
with open('dataset_24465_4 (6).txt', 'r') as reading, open('answer.txt', 'w') as writing:
    lines = reading.readlines()
    for line in reversed(lines):
        writing.write(line)
"""

print(os.getcwd(), end='\n\n')
os.chdir('Stepik')
print(os.getcwd())
directories = []
with open('/Stepik/pycourse/answer.txt', 'w') as answer:
    for current_dir, dirs, files in os.walk("main"):
        print(current_dir, files)
        for file in files:
            if file.endswith('.py'):
                directories.append(current_dir)
                break
    directories.sort()
    to_write = '\n'.join(directories)
    answer.write(to_write)
