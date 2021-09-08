import math
def minimal_points(n):
    d = [tuple(map(int, input().split())) for I in range(n)]
    for top in range(1, len(d)):
        k = top
        while k > 0 and d[k - 1][1] > d[k][1]:
            d[k], d[k - 1] = d[k - 1], d[k]
            k -= 1
    # print(d)
    points = []
    current_point = -1
    for left, right in d:
        if left <= current_point <= right:
            continue
        else:
            points.append(right)
            current_point = right
    # print(points)
    print(len(points))
    print(*points)


def max_terms(n):
    d_sqrt = math.sqrt(1 + 8 * n)
    k = math.floor((1 + d_sqrt) / 2)
    lst = list(range(1, k + 1))
    s = sum(lst)
    if s != n:
        lst.pop(sum(lst) - n - 1)
    print(len(lst))
    print(*lst)



if __name__ == '__main__':
    minimal_points(3)
    max_terms(4)