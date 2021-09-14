import sys


def check_unumbiguoity(x, y, z):
    leap_year = not z % 4
    if x == y:  # => AA.AA.YYYY
        return 1
    if all((x < 13, y < 13)):
        return 0
    if x > 12:  # x is DD => DD.MM.YYYY
        return 1
    if y > 12:  # y is DD => MM.DD.YYYY
        return 1


x, y, z = map(int, sys.stdin.readline().split())
print(check_unumbiguoity(x, y, z))