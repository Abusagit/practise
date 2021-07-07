L1 = [int(i) for i in input().split()]
L2 = []
n = len(L1)
if n == 1:
    print(L1[0])
elif n == 2:
    L2 += [str((L1[1]) * 2), str((L1[0]) * 2)]
    print(' '.join(L2))
else:
    for i in range(n - 1):
        if i == 0:
            L2.append(str(L1[1] + L1[-1]))
        else:
            L2.append(str(L1[i - 1] + L1[i + 1]))
    L2.append(str(L1[0] + L1[-2]))
    print(' '.join(L2))