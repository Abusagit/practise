import numpy as np



def matrix_build(rows):
    matrix = []
    for row in range(rows):
        matrix.append([int(i) for i in input().split()])
    return matrix


def matrix_transpose(matrix, rows, columns):
    matrix2 = []
    for column in range(columns):
        tmp = []
        for row in range(len(matrix)):
            tmp.append(matrix[row][column])
        matrix2.append(tmp)
    return matrix2


if __name__ == '__main__':
    n, m = (int(_) for _ in input().split())
    a = matrix_build(n)
    b = matrix_transpose(a, n, m)
    # print(a)
    # print(b)
    for i in enumerate(b):
        print(*i[1], sep=' ')