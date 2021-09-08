def expected_geom10(i) -> float:
    """
    solution for Exam 1 exercise 3 edX
    :param i: number of unseen values
    :return float: expected times for see every value in infinite number of repeats
    """
    exp_tmp = 0
    for x in range(i, -1, -1):
        a = round((10/(10 - x)), 1)
        exp_tmp += a
        print(f'exp_tmp at x ={x}: {exp_tmp} -------- {a}')
    return exp_tmp


if __name__ == '__main__':
    print(expected_geom10(9))
    print(expected_geom10.__doc__)