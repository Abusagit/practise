import os


def finder(filename):
    """

    :param filename: name of file
    :return: locations of looking things
    """
    locations = []
    os.chdir(r'D:\Downloads')
    with open(f'{filename}.txt') as file:
        seq = file.readline().strip()
        subseq = file.readline().strip()
        print(subseq, end='\n\n')
    for i in range(len(seq) - len(subseq) + 1):
        print(seq[i:i + len(subseq)])
        if seq[i:i + len(subseq)] == subseq:
            locations.append(i + 1)
    return locations


if __name__ == '__main__':
    print(*finder('rosalind_subs (1)'))