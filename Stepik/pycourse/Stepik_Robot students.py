n = int(input())
x = 'программист'
x1 = 'а'
x2 = 'ов'
m = n % 10
o = (n - 11) % 100
v = (n - 12) % 100
b = (n - 13) % 100
s = (n - 14) % 100
if n == 11 or o == 0 or v == 0 or b == 0 or s == 0:
    print(n, x + x2)
elif m == 1:
    print(n, x)
elif 2 <= m <= 4:
    print(n, x + x1)
elif m == 0 or (5 <= m <= 9):
    print(n, x + x2)
