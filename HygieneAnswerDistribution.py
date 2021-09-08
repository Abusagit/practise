L = [int(i+1) for i in range(11)]
P = [int(i+1) for i in range(47)]
R = [int(i+1) for i in range(27)]
T = [int(i+1) for i in range(20)]
Y = [int(i+1) for i in range(20)]
U = [int(i+1) for i in range(28)]
I = [int(i+1) for i in range(21)]
A = [int(i+1) for i in range(47)]
S = [int(i+1) for i in range(64)]
D = [int(i+1) for i in range(19)]
a = int(input('your number in distributive list:'))
L += P
L += R
L += T
L += Y
L += U
L += I
L += A
L += S
L += D
for i in range(300):
    if i % 25 == a:
        print(L[i - 1], end=' ')
print()
print(L[109])
