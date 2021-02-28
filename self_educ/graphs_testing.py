from structures.graphs import adjGraph as g


j = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


graph = g.build_graph(j)

print(graph.getVertices())

# for v in graph:
#     print(f'-------------{v.id}---------------')
#     for item in v.connectedTo:
#         print(item.id)
#     else:
#         print('\n\n')
# for v in graph:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

g.bfs(graph, graph['A'])

print('________________________________________________________________')
for v in graph:
    print(f'-------------{v.id}---------------')
    for item in v.connectedTo:
        print(item)
    else:
        print('\n\n')

g.traverse(graph['D'])

for item in graph:
    for i in item.connectedTo:
        print(item, i, sep='-----------')

