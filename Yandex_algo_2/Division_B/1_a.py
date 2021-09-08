import sys


def interactive_module(r, i, c):
    verdict = {0: 3 if r else c,
               1: c,
               4: 3 if r else 4,
               6: 0,
               7: 1}

    return verdict.get(i, i)


r, i, c = map(int, sys.stdin.readlines())
print(interactive_module(r, i, c))