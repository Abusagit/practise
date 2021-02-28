def fib(n):
    f1, f2 = 0, 1
    for _ in range(n - 1):
        f1, f2 = f2, f1 + f2
    return f2


if __name__ == '__main__':
    print(fib(2))
    print(fib(21))
    print(fib(4))
    print(fib(25))