import os


def distance():
    s, t = [input() for _ in range(2)]
    distance = 0
    for i, j in zip(s, t):
        distance += 1 if i != j else 0
    return distance


if __name__ == '__main__':
    print(distance())