import random
import bisect
from sortings import quickSort as q


def q_s(a, right=False):
    if len(a) < 2:
        return a
    else:
        pivot = random.randint(0, len(a) - 1)
        eq = [i for i in a if i[0 + right] == a[pivot][0 + right]]
        less = [i for i in a if i[0 + right] < a[pivot][0 + right]]
        greater = [i for i in a if i[0 + right] > a[pivot][0 + right]]
        return q_s(less) + eq + q_s(greater)





n, m = map(int, input().split())
edges_left, edges_right = ([None for _ in range(n)] for _ in range(2))
# print(edges_left, edges_right, edges_right is edges_left)
for i in range(n):
    j = tuple(map(int, input().split()))
    edges_left[i] = j[0]
    edges_right[i] = j[1]

# print(edges_left, edges_right)
spots = tuple(map(int, input().split()))
edges_left = q(edges_left)
edges_right = q(edges_right)

for spot in spots:
    i = bisect.bisect(edges_left, spot)
    j = bisect.bisect_left(edges_right, spot)
    print(i - j, end=' ')


