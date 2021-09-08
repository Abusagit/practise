a = int(input())
max_ = a
n = 1
a = int(input())
while a:
    if a > max_:
        n = 1
        max_ = a
    elif a == max_:
        n += 1
    a = int(input())
print(n)