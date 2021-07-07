a = []
f = [i for i in input().split()]
while f[0] != 'end':
    for i in range(len(f)):
        f[i] = int(f[i])
    a += [f]
    col = len(f)
    f = [i for i in input().split()]
row = len(a)
for i in range(row):
    for j in range(col):
        b = a[i][j - col + (col - 1)] + a[i - row + (row - 1)][j] + a[i][-(col - j) + 1] + a[-(row - i) + 1][j]
        print(b, end=' ')
    print()