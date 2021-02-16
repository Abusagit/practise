def rabbits(n, k):
    # old = 0 on month 1
    old1 = 1 # month n
    old2 = 1 #month 2 old
    for _ in range(n - 2):
        old1, old2 = old2, old1 * k + old2
    return old2


if __name__ == '__main__':
    print(rabbits(5,3))