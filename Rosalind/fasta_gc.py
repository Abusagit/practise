import os

def gc_count(filename):
    os.chdir(r'D:\Downloads')
    filename += '.txt'

    max_gene = None
    max_value = float('-inf')

    with open(filename, 'r') as file:
        gene = file.readline().strip()[1:]
        print(gene)
        sequence = ''

        for line in file:
            # print(line)
            if line.startswith('>'):
                gc_count = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
                if gc_count > max_value:
                    max_value, max_gene = gc_count, gene
                gene = line.strip()[1:]
                sequence = ''
            else:
                sequence += line.strip()

    os.chdir(r'C:\Users\Fyodor\PycharmProjects\untitled')

    with open('Test_stdout.txt', 'w') as answer:
        answer.write(f'{max_gene}\n{max_value}')