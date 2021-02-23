import math as m
n = int(input())

D = [
    (m.log(m.factorial(n), 2), 'log2(n!)'),
    (4 ** n, '4^n'),
    (m.pow(n, 2), 'n^2'),
    (m.log(n, 3), 'log3(n)'),
    (n / m.log(n, 5), 'n / log5(n)'),
    (2 ** (3 * n), '2^(3n)'),
    (m.pow(n, m.log(n, 2)), 'n^(log2(n))'),
    (3 ** m.log(n, 2), '3^(log2(n))'),
    (2 ** n, '2^n'),
    (n ** 0.5, 'sqrt(n)'),
    (m.log((m.log(n, 2)), 2), 'log(2)log(2)n'),
    (n ** (n ** 0.5), 'n^(sqrt(n))'),
    (m.factorial(n), 'n!'),
    (7 ** m.log(n, 2), '7^(log2(n))'),
    (m.log(n, 2) ** 2, '(log2(n))^2'),
    (m.sqrt(m.log(n, 4)), 'sqrt(log4(n))'),
    (m.log(n, 2) ** m.log(n, 2), '(log2(n))^(log2(n))')
]

for i, j in sorted(D):
    print(f'{j} --> {i}')



n=50
print(m.log(m.log(n, 2), 2))
print(m.sqrt(m.log(n, 4)))
print(m.log(n, 3))
print(m.log(n, 2) ** 2)
print(m.sqrt(n))
print(n / m.log(n, 5))
print(m.log(m.factorial(n),2))
print(3 ** m.log(n, 2))
print(n ** 2)
print(7 ** (m.log(n, 2)))
print(m.log(n, 2) ** (m.log(n, 2)))
print(n ** (m.sqrt(n)))
print(n ** (m.log(n, 2)))
print(2 ** n)
print(4 ** n)
print(2 ** (3 * n))
print(m.factorial(n))
# print(2 ** (2 ** n))