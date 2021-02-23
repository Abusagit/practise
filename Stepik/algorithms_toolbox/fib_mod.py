def fib_mod(n, m):
    """
    >>> fib_mod(1025, 55)
    5
    >>> fib_mod(12589, 369)
    89
    >>> fib_mod(1598753, 25897)
    20305
    """
    pisano = [0, 1]
    while True:
        if len(pisano) > 2 and pisano[-1] == 1 and pisano[-2] == 0:
            pisano = pisano[: -2]
            break
        pisano.append((pisano[-1] + pisano[-2]) % m)
    # print(pisano)
    # print(pisano[n % len(pisano)])
    return pisano[n % len(pisano)]


def slow_fm(n, m):
    """
    >>> slow_fm(1025, 55)
    5
    >>> slow_fm(12589, 369)
    89
    >>> slow_fm(1598753, 25897)
    20305
    """
    import algorithms.fib as f
    return f.fib(n) % m
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
