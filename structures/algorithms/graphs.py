def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path_ = queue.pop(0)
        for next_ in graph[vertex] - set(path):
            if next_ == goal:
                yield path + [next_]
            else:
                queue.append((next_, path + [next_]))


def dijkstra(graph, costs, parents, start, finish):
    processed = []
    def find_lowest_cost_node(costs):
        nonlocal processed
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    way = [finish, parents[finish]]
    while start not in way:
        way.append(parents[way[-1]])
    print(f'lowest cost is {costs[finish]}')
    return way[::-1]

if __name__ == '__main__':
    g = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print(list(bfs_paths(g, 'A', 'F')))
    for path in bfs_paths(g, 'A', 'F'):
        print(path)
    graph = {
        'start' : {'a' : 6, 'b': 2},
        'a': {'fin': 1},
        'b': {'a': 3, 'fin': 5},
        'fin': {}
    }
    infinity = float('inf')
    costs = {
        'a': 6,
        'b': 2,
        'fin': infinity
    }
    parents = {
        'a': 'start',
        'b': 'start',
        'fin': None
    }
    print(dijkstra(graph, costs, parents, 'start', 'fin'))  # TODO finish returning value