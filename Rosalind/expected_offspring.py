def exp(filename):
    with open(f'{filename}.txt') as file:
        numbers = list(map(int, file.read().strip().split()))[: -1]
    print(numbers)
    expected = 0
    for i, j in zip(numbers[:], (1, 1, 1, 0.75, 0.5)):
        expected += 2 * i * j
    return expected


if __name__ == '__main__':
    print(exp('expect'))
    import os
    os.chdir(r'D:\Downloads')
    print(exp('rosalind_iev'))