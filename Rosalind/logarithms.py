import math
import os


def gc_count_log(filename):

    with open(f'{filename}.txt') as file:
        s = file.readline().strip()
        gc = s.count('C') + s.count('G')
        at = len(s) - gc
        array = [float(i) for i in file.readline().strip().split()]
    results = [None for _ in range(len(array))]
    for index, number in enumerate(array):
        results[index] = round((math.log10((number / 2) ** gc) + math.log10((0.5 - number / 2) ** at)), 3)
    return results

if __name__ == '__main__':
    print(*gc_count_log('log10'))
    os.chdir(r'D:\Downloads')
    print(*gc_count_log('rosalind_prob'))