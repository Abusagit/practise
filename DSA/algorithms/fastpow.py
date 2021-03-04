def fpow(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * fpow(a, n - 1)
    else:
        return fpow(a ** 2, n // 2)


if __name__ == '__main__':
    print(fpow(3, 7))
    print(fpow(2, 4))