def continous_backpack(n, w):
    items = []
    for _ in range(n):
        cost, volume = map(int, input().split())
        items.append((cost, volume, cost / volume))
    for pos in range(len(items)):
        for k in range(pos + 1, len(items)):
            if items[k][2] < items[pos][2]:
                items[pos], items[k] = items[k], items[pos]
    items.reverse()
    cost = 0
    for price, weight, ratio in items:
        if weight <= w:
            cost += price
            w -= weight
        else:
            cost += ratio * w
            break
    return f'{cost:.3f}'


def knapsackBU(W, weight, values) -> int:
    """
    BU - bottomUp
    :param W: max summary weight of objects
    :param weight: weights of objects
    :param values: cost of objects
    :return: maximum possible carriable value
    >>> val = [7, 8, 4]
    >>> wt = [3, 8, 6]
    >>> weight_ = 10
    >>> knapsackBU(weight_, wt, val)
    11
    """
    n = len(values)
    K = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weight[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w - weight[i-1]], K[i - 1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[-1][-1]


def golden_ingots(max_w, ing_w) -> int:
    """
    >>> golden_ingots(10, [1, 4, 8])
    9
    """
    cost = [i for i in ing_w]
    return knapsackBU(max_w, cost, ing_w)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
