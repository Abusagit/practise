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


if __name__ == '__main__':
    print(*calculator(5))