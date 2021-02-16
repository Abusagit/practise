import kmp

def pi_func(s):
    P = [0 for _ in range(len(s))]
    i, j = 0, 1
    while j < len(s):
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        elif i:
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return P


if __name__ == '__main__':
    with open(r'D:\Downloads\rosalind_kmp.txt') as file:
        file.readline()
        s = ''
        for line in file:
            s += line.strip()
    print(*pi_func(s), file=open('prefix.txt', 'w'))