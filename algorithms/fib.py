def fib(n):
    F = [0, 1] + [None]*(n-1)
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]


if __name__ == '__main__':
    print(fib(2))
    print(fib(21))
    print(fib(4))
    print(fib(25))