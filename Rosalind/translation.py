import os

table = {}
with open('Codon.txt') as file:
    for line in file:
        triplet, sense = line.strip().split()
        table[triplet] = sense
# print(table)

def process(filename):
    os.chdir(r'D:\Downloads')
    protein = ''
    seq = ''
    with open(f'{filename}.txt', 'r') as file:
        seq += file.readline().strip()
    for i in range(2, len(seq), 3):
        codon = seq[i - 2:i + 1]
        print(codon)
        signal = table[codon]
        if signal != 'Stop':
            protein += signal
        else:
            break
    return protein




if __name__ == '__main__':
    print(process('rosalind_prot (1)'))
