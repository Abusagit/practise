def perm(n, m, prefix=None):
    if m == 0:
        l = ' '.join(prefix)
        print(l, file=open('permut.txt', 'a'))
        return
    prefix = prefix or []
    for i in range(1, n + 1):
        if str(i) not in prefix:
            prefix.append(str(i))
            perm(n, m - 1, prefix)
            prefix.pop()

if __name__ == '__main__':
    import math
    n = int(input())
    print(math.factorial(n), file=open('permut.txt', 'w'))
    perm(n, n)
