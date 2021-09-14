import sys


def perfect_place_slow(coordinates):
    distances = {coord: sum(max(coord, house) - min(coord, house) for house in coordinates)
                 for coord in range(coordinates[0], coordinates[-1] + 1)}
    return min(distances, key=distances.get)


def perfect_place_fast(n, coordinates): # TODO showed WA on test 3
    middle_house = n // 2
    return coordinates[middle_house]


n, coords = sys.stdin.readline(), tuple(map(int, sys.stdin.readline().split()))
print(perfect_place_fast(int(n), coords))
