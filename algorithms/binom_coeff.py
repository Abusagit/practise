def binom_coeff_recur(n, k):
    if n == k or k == 0:
        return 1
    return binom_coeff_recur(n - 1, k - 1) + binom_coeff_recur(n - 1, k)


def binom_coeff_fact(n,k):
    numerator, denominator = 1, 1
    for i in range(2, n + 1):
        numerator *= i
    for j in range(2, k + 1):
        denominator *= j
    for j in range(2, (n - k) + 1):
        denominator *= j

    return int(numerator / denominator)


if __name__ == '__main__':
    for i in (binom_coeff_recur, binom_coeff_fact):
        print(f'{i.__name__}: {i(3, 2)}')