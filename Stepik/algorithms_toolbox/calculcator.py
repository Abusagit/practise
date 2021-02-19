"""
2x, 3x, x+1

"""
import math


def calculator(x) -> list:
    """

    :param x: number to get
    :return: minimal list of intermediate terms
    """
    D = [0 for _ in range(x ** 3)]
    D[0] = x

    for index, value in enumerate(D):
        if value == 1:
            break
        elif value:
            if 3 * index + 1 < len(D):
                D[3 * index + 1] = value // 2 if value % 2 == 0 else None
            if 3 * index + 2 < len(D):
                D[3 * index + 2] = value // 3 if value % 3 == 0 else None
            if 3 * index + 3 < len(D):
                D[3 * index + 3] = value - 1
    ans = [1]
    ind = index
    while ind > 0:
        ans.append(D[ind // 3])
        ind //= 3
    else:
        ans.append(x)
    print(len(ans))
    return ans


def calcV2(x):
    """
    >>>

    """
    tmp = [[float('inf') for _ in range(x + 1)] for _ in range(2)] # 0 - steps, 1 - previous
    tmp[0][1] = 0
    result = [x]
    for i in range(1, x + 1):
        a = i * 3
        b = i * 2
        c = i + 1
        for j in (a, b, c):
            if j <= x:
                steps = tmp[0][i] + 1
                if tmp[0][j] > steps:
                    tmp[0][j] = steps
                    tmp[1][j] = i
        if x < c < b < a:
            break
    i = tmp[-1][-1]
    while i != 1:
        result.append(i)
        i = tmp[1][i]
    result.append(1)
    result.reverse()
    print(tmp[0][-1])
    return result


if __name__ == '__main__':
    print(*calculator(5))
    print(*calcV2(5))
