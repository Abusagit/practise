def define_generation(x, y):
    for _ in range(x):
        sample = input()
        if ":" in sample:
            child, parent = sample.split(' : ')
            y[child] = []
            y[child] = y[child] + parent.split(' ')
        else:
            y[sample] = []


# def breadth_search(graph, start, goal):
#     queue = [(start, [start])]
#     while queue:
#         (vertex, path) = queue.pop(0)
#         for next in graph[vertex] - set(path):
#             if next == goal:
#                 yield path + [next]
#             else:
#                 queue.append((next, path + [next]))


def graph_find_way(graph, start, end, order=[]):
    order = order + [start]
    if start == end and start in graph.keys() and end in graph.keys():
        return order
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in order:
            new_order = graph_find_way(graph, node, end, order)
            if new_order:
                return new_order
    return None


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


answers = []
family_tree = {}
n = int(input())
define_generation(n, family_tree)
m = int(input())
requests = tuple(input() for i in range(m))
# print(family_tree)
for request in requests:
    for error in requests:
        if request != error and graph_find_way(family_tree, request, error) is not None:
            path = graph_find_way(family_tree, request, error)
            # print(path)
            # print('Error: ', error)
            # print('Request: ', request)
            if requests.index(request) > requests.index(error) and request not in answers:
                answers.append(request)
print(*answers, sep='\n')
# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}
#
# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited
#
#
# print(dfs(graph, 'A'))