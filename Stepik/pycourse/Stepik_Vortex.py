a = int(input())
M = [[0 for i in range(a)] for j in range(a)]
m = 1
while m <= a**2:
    for i in range(a):
        for j in range(a):
            if M[i][a - 1 - i] == 0:
                M[i][j + i] = m
                m += 1
        for j in range(a):
            if M[a - 1 - i][a - 1 - i] == 0:
                M[j + i + 1][a - 1 - i] = m
                m += 1
        for j in range(a):
            if M[a - 1 - i][i - a] == 0:
                M[a - 1 - i][a - 2 - j - i] = m
                m += 1
        for j in range(1, a):
            if M[1 - a + i][i] == 0:
                M[a - 1 - j - i][i] = m
                m += 1
for i in range(a):
    print(*M[i], end='\t')
    print()