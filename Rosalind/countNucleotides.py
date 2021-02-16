import os


def count(d):
    res = {'A': 0,
           'C': 0,
           'G': 0,
           'T': 0}
    for i in d:
        res[i] += 1
    for i in ('A', 'C', 'G', 'T'):
        print(res[i], end=' ')


a = input()
with open(r'D:\Downloads\{}.txt'.format(a), 'r') as file:
    dna = file.read().strip()
    count(dna)