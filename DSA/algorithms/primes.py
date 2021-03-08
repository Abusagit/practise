def primes(n):
    """РЕШЕТО ЭРАТОСФЕНА:"""
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            for j in range(i, n + 1, i):
                a[j] = 0
            yield i
        i += 1


if __name__ == '__main__':
    for j in primes(31):
        print(j)
