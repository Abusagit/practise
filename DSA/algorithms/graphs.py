from DSA.structures import graph as gr
from collections import deque, defaultdict
import sys
import heapq as h


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        vertex, path_ = queue.pop(0)
        for next_ in graph[vertex] - set(path_):
            if next_ == goal:
                yield path_ + [next_]
            else:
                queue.append((next_, path_ + [next_]))


def dijkstra1(graph, costs, parents, start, finish):
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


'''Algorithms'''


# TODO make them generator functions


def dfs(g, start, visited=None):
    """The time complexity of the DFS algorithm is represented in the form of O(V + E),
    where V is the number of nodes and E is the number of edges.
    The space complexity of the algorithm is O(V).
    """
    visited = visited or set()
    visited.add(start)

    print(start)

    for next_ in g[start]:
        if next_ not in visited:
            dfs(g, next_, visited)
    return visited


def bfs(g, root):
    """
    The time complexity of the BFS algorithm is represented in the form of O(V + E),
    where V is the number of nodes and E is the number of edges.
    The space complexity of the algorithm is O(V)
    """
    visited, queue = {root}, deque([root])

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(f'{vertex} ', end='')

        # If not visited, mark it as visited, and
        # enqueue it

        for neighbor in g[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def dijkstra2(vertices):
    """
    Time Complexity: O(E Log V)
    where, E is the number of edges and V is the number of vertices.
    Space Complexity: O(V)
    """

    def to_be_visited():
        nonlocal visited_and_distance
        nonlocal num_of_vertices
        v = -10
        for index in range(num_of_vertices):
            if (visited_and_distance[index][0] == 0 and
                    (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1])):
                v = index
        return v

    num_of_vertices = len(vertices)
    visited_and_distance = [[0, 0]]

    for i in range(num_of_vertices - 1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(num_of_vertices):
        # Find next vertex to be visited
        to_visit = to_be_visited()
        for neighbor_index in range(num_of_vertices):
            # Updating new distances
            if vertices[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
                new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance

            visited_and_distance[to_visit][0] = 1
    i = 0

    # Printing the distance
    for distance in visited_and_distance:
        print("Distance of ", chr(ord('a') + i), " from source vertex: ", distance[1])
        i += 1


def dijkstra3(aGraph, start):
    pq = []
    h.heapify(pq)


if __name__ == '__main__':
    g = gr.Graph(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)

    print("Strongly Connected Components:")
    g.print_scc()

    print()

    g = gr.GraphMatrix(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    print(g)
    g.dijkstra()

    V = 5

    # Create graph and edges
    G = gr.GraphList()
    G.addEdge(0, 1)
    G.addEdge(0, 2)
    G.addEdge(0, 3)
    G.addEdge(1, 2)

    print(G)

    '''DFS'''
    graph = {'0': {'1', '2'},
             '1': {'0', '3', '4'},
             '2': {'0'},
             '3': {'1'},
             '4': {'2', '3'}}

    b = gr.build_graph(graph)
    print(b)
    dfs(graph, '0')
    bfs(graph, '0')
    graph = {
        0: {1, 2, 3},
        1: {0, 2},
        2: {0, 1, 4},
        3: {0},
        4: {2}
    }
    print()
    dfs(graph, 0)
    bfs(graph, 0)

    j = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    dfs(j, 'A')
    bfs(j, 'A')
    print()
    vertices = [[0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0],
                [1, 1, 0, 1, 1, 0, 0],
                [1, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0, 1, 0]]

    edges = [[0, 0, 1, 2, 0, 0, 0],
             [0, 0, 2, 0, 0, 3, 0],
             [1, 2, 0, 1, 3, 0, 0],
             [2, 0, 1, 0, 0, 0, 1],
             [0, 0, 3, 0, 0, 2, 0],
             [0, 3, 0, 0, 2, 0, 1],
             [0, 0, 0, 1, 0, 1, 0]]

    v = gr.GraphMatrix(edges=edges, adjMatrix=vertices, size=len(vertices))
    v.dijkstra()

    # g = {
    #     'A': {'B', 'C'},
    #     'B': {'A', 'D', 'E'},
    #     'C': {'A', 'F'},
    #     'D': {'B'},
    #     'E': {'B', 'F'},
    #     'F': {'C', 'E'}
    # }
    # print(list(bfs_paths(g, 'A', 'F')))
    # for path in bfs_paths(g, 'A', 'F'):
    #     print(path)
