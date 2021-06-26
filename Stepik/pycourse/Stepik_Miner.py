import sys


n, m, k = map(int, sys.stdin.readline().strip().split())  # n - rows, m - columns
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
    a[row][col] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end=' ')
        else:
            print(a[i][j], end=' ')
    print()