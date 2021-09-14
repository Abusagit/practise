import sys
from math import sqrt


def co_existance(d, x, y):
    if all((d >= x + y, y >= 0, x >= 0)):
        return 0
    distances = ((sqrt((0 - x) ** 2 + (0 - y) ** 2), 1),
                 (sqrt((d - x) ** 2 + (0 - y) ** 2), 2),
                 (sqrt((0 - x) ** 2 + (d - y) ** 2), 3))
    return min(distances)[1]


d, X = int(sys.stdin.readline()), map(int, sys.stdin.readline().split())
print(co_existance(d, *X))
