import os



with open(r'C:\Users\Fyodor\PycharmProjects\untitled\Rosalind\mass.txt') as file:
    mass = {}
    for line in file:
        line = line.strip().split('   ')
        mass[line[0]] = float(line[1])

def opener(filename):
    weight = 0
    os.chdir(r'D:\Downloads')
    with open(f'{filename}.txt') as file:
        protein = file.read().replace('\n', '')
        print(protein)
    for acid in protein:
        weight += mass[acid]
    return weight

if __name__ == '__main__':
    print(opener('test'))