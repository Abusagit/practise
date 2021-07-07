a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\t', end='')
for g in range(c, d + 1):
    print(g, end='\t')
print()
for v in range(a, b + 1):
    print(v, end='\t')
    for g in range(c, d + 1):
        print(v * g, end='\t')
    print()