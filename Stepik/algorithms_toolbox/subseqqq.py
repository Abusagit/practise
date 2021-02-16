def longest_folding_subseq(a):
    d = [0 for _ in range(len(a))]
    for i in range(len(a)):

        d[i] = 1
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(len(a)):
        ans = max(ans, d[i])
    return ans


if __name__ == '__main__':
    print(longest_folding_subseq([3, 6, 7, 12]))
    A = [3, 6, 12, 7, 9, 24, 18, 3, 9, 24]
    print(longest_folding_subseq(A))