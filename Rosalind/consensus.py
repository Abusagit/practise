import os


def profiler(filename):
    os.chdir(r'D:\Downloads')
    with open(f'{filename}.txt') as file:
        strings = {}
        string = file.readline().strip()
        while string:
            if string.startswith('>'):
                label = string
                strings[label] = ''
            else:
                strings[label] += string
            string = file.readline().strip()
    length = len(strings[label])
    # print(strings)
    consensus = ''
    dna = {base: lst for base, lst in zip('ACGT', [[0 for i in range(length)] for j in range(4)])}
    for i in range(length):

        for seq in strings.values():
            dna[seq[i]][i] += 1
        base = ''
        cur_max = 0
        for j in 'ACGT':
            if cur_max < dna[j][i]:
                cur_max = dna[j][i]
                base = j
        consensus += base

    with open(r'C:\Users\Fyodor\PycharmProjects\untitled\Rosalind\protein_motif.txt', 'w') as file:
        file.write(f'{consensus}\n')
        for base in dna:
            file.write(f'{base}: ')
            for i in dna[base][:-1]:
                file.write(f'{i} ')
            file.write(f'{dna[base][-1]}\n')


if __name__ == '__main__':
    # profiler('test')
    profiler('rosalind_cons (1)')
