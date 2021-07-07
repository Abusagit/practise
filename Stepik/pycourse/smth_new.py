def define_generation(x, y):
    for _ in range(x):
        sample = input()
        if ":" in sample:
            child, parent = sample.split(' : ')
            y[child] = []
            y[child] = y[child] + parent.split(' ')
        else:
            y[sample] = []


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


answers = []
family_tree = {}
n = int(input())
define_generation(n, family_tree)
q = int(input())
for i in range(q):
    x, y = input().split()
    answer = graph_find_way(family_tree, y, x)
    if answer is None:
        answers.append('No')
    else:
        answers.append('Yes')
print(*answers, sep='\n')