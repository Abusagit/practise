import permutations as p

def all_combinations(k, n):
    if k > 0:
        number = [_ for _ in range(k)]
        last = [_ for _ in range(n - k, n)]
        pos_to_max = -1
        while True:
            print(*number)
            if number == last:
                break
            elif number[pos_to_max] < n + pos_to_max:
                number[pos_to_max] += 1
            else:
                pos_to_max -= 1
                number[pos_to_max] += 1


def permutations(n, k, prefix=None):
    if k == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for i in range(n):
        if i not in prefix:
            prefix.append(i)
            permutations(n, k-1, prefix)
            prefix.pop()
if __name__ == '__main__':
    all_combinations(2, 3)
    all_combinations(1, 1)
    all_combinations(0, 4)
    p.generate_numbers(N=4, M=2)
    permutations(4, 2)