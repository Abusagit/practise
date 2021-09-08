import sys
import re

"""
pattern = re.compile(r'cat')
for line in sys.stdin.read():
    print(line)
    print(re.findall(pattern, line))
    break
answer = []
strings = [
    'catcat',
    'cat and cat',
    'catac',
    'cat',
    'ccaatt'
]


print(sys.stdin)

sye = sys.stdin.read()
print(sye)
print(repr(sye))
for line in sys.stdin.read():
    line = line.rstrip()
    print(line)
for string in strings:
    if len(pattern.findall(string)) >= 2:
        answer.append(string)
for line in sye:
    line = line.rstrip()
    print(line)


print(*answer, sep='\n')
"""

"""
pattern = re.compile(r'human')
answer = []
questions = sye.splitlines()
for question in questions:
    if pattern.search(question):
        answer.append(pattern.sub('computer', question))
    else:
        answer.append(question)
print(*answer,sep='\n')
"""


"""Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" 
(регистр не важен), на слово "argh
"""

pattern = r'(\ba+\b)'


x = sys.stdin.read()
print(x)
for line in x:
    line = line.rstrip()
    print(line)