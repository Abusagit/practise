import json


def read_and_set_inheritance(js):
    global inheritance
    # print(type(js)) - list
    for subject in js:
        inheritance[subject['name']] = subject['parents']


def graph_find_way(graph, start, end, order=[]):
    order = order + [start]
    if start == end:
        return order
    elif start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in order:
            new_order = graph_find_way(graph, node, end, order)
            if new_order:
                return new_order
    return None


def set_inheritance_number(value):
    count = 1
    for item in inheritance:
        if item != value and graph_find_way(inheritance, item, value) is not None:
            count += 1
    return count


def ordered_print():
    global values
    for value in values:
        print(value, set_inheritance_number(value), sep=' : ')


inheritance = dict()
test = [
    {"name": "beta", "parents": ["alpha", "gamma"]},
    {"name": "gamma", "parents": ["alpha"]},
    {"name": "alpha", "parents": []},
    {"name": "delta", "parents": ["gamma", "zeta"]},
    {"name": "epsilon", "parents": ["delta"]},
    {"name": "zeta", "parents": []}
]
read_and_set_inheritance(json.loads(input()))
values = sorted(inheritance.keys())
ordered_print()
