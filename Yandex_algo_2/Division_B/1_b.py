import sys
import unittest

stations_num, i, j = map(int, sys.stdin.readline().split())


def minimal_stations(n, i_, j_):
    if i_ > j_:
        i_, j_ = j_, i_

    return min(j_ - i_ - 1, n - j_ + i_ - 1)


# TODO Unitests
# a = j - i - 1
# b = stations_num - a - 2
print(minimal_stations(stations_num, i, j))

