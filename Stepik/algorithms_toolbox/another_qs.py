n, m = [int(x) for x in input().split()]

a = []
for i in range(0, n):
    l, r = [int(x) for x in input().split()]
    a.append([l, -1])
    a.append([r, 1])

p = [int(x) for x in input().split()]
for i in range(m):
    a.append([p[i], 0, i])


a.sort()
res = [0] * m
print(a)
curr = 0
pi = 0
for i in range(len(a)):
    if a[i][1] == 0:
        res[a[i][2]] = curr
    else:
        curr -= a[i][1]
print(*res)