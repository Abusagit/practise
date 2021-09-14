import sys


def get_maximum_distance(houses) -> int:
    # shops_aparts = OrderedDict(list)
    # for index, house in enumerate(houses):
    #     shops_aparts[house].append(index)
    #
    # for apart in shops_aparts[1]:
    #     left = 0
    #     right = len(shops_aparts[2])
    #     while left < right:
    #         middle = left + (right - left) // 2
    #         if apart > shops_aparts[2][middle]:
    #             pa
    aparts_distances = {}
    aparts_shops_indices = tuple(filter(lambda x: houses[x], range(len(houses))))
    current_index = float("inf")
    for house_index in aparts_shops_indices:
        if houses[house_index] == 1:
            aparts_distances[house_index] = min(house_index - current_index, aparts_distances.get(house_index,
                                                                                                  float("inf")))
        else:
            current_index = house_index

    # current_index = len(aparts_shops_indices) - 1
    max_distance = float("-inf")

    for i in range(len(aparts_shops_indices) - 1, -1, -1):
        if houses[aparts_shops_indices[i]] == 1:
            aparts_distances[aparts_shops_indices[i]] = min(current_index - aparts_shops_indices[i],
                                                            aparts_distances[aparts_shops_indices[i]])

            max_distance = max(max_distance, aparts_distances[aparts_shops_indices[i]])
        else:
            current_index = aparts_shops_indices[i]

    return max_distance


def get_max_dist(houses) -> int:
    aparts_shops_idxs = tuple(filter(lambda x: houses[x], range(len(houses))))
    shortest_distances = {}

    current_shop_idx = float("inf")
    for house_idx in aparts_shops_idxs:
        if houses[house_idx] == 1:
            distance = house_idx - current_shop_idx
            shortest_distances[house_idx] = distance if distance >= 0 else float("inf")
        else:
            current_shop_idx = house_idx

    current_shop_idx = float("inf")
    max_distance = float("-inf")
    for i in range(len(aparts_shops_idxs) - 1, -1, -1):
        if houses[aparts_shops_idxs[i]] == 1:
            shortest_distances[aparts_shops_idxs[i]] = min(shortest_distances[aparts_shops_idxs[i]],
                                                           current_shop_idx - aparts_shops_idxs[i])
            max_distance = max(max_distance, shortest_distances[aparts_shops_idxs[i]])
        else:
            current_shop_idx = aparts_shops_idxs[i]

    return max_distance


h = tuple(map(int, sys.stdin.readline().split()))
print(get_max_dist(h))