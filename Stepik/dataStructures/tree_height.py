def tree_height(n):
    tree = [int(i) for i in input().split()]
    structure = {}
    for index, value in enumerate(tree):
        if value not in structure:
            structure[value] = {index}
        else:
            structure[value].add(index)

    for i in structure:
        print(i, ': ', structure[i])

    root = structure[-1].pop()
    heights = {root: 1}
    heights.update({num: 2 for num in structure[root]})
    road = 1
    for i in range(n):
        h = 0
        j = i
        while True:
            if j in heights:
                heights[i] = heights[j] + h
                break
            else:
                j = tree[j]
                h += 1

        road = max(road, heights[i])
    return road


if __name__ == '__main__':
    print(tree_height(10))
