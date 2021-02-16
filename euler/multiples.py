def multiples(number:int, *pargs:int) -> int: #better
    '''returns sum of all integers below 'number'
    which are multiples of any numbers in *pargs'''
    A = [0] * number
    for i in pargs:
        for j in range(i, number, i):
            A[j] = j if A[j] == 0 else A[j]
            # print(A, sum(A))
    return sum(A)


def multiples2(number, *pargs): # worse
    a = 0
    for i in range(1, number):
        for j in pargs:
            if i % j == 0:
                a += i
                break
    return a


if __name__ == '__main__':
    print(multiples(10, 3, 5))
    print(multiples(1000, 3, 5))
    print(multiples2(1000, 3, 5))