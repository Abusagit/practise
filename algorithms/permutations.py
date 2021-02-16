def generate_numbers(N:int=2, M:int=3, prefix:list=None)-> list:
    '''
    Generating numbers with leading zeros
    with combinating all possible conditions for every position
    for N-numerical system M-1-sigits contained number

    N: numeral system base
    M: number of digits in number to generate
    prefix: already permutated part of number
    '''

    if M == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


if __name__ == '__main__':
    generate_numbers(4, 3)
    print(generate_numbers.__doc__)
    print(generate_numbers.__annotations__)