import sys
from collections import defaultdict, deque
from DSA.basic import Stack
from DSA.graphs import PriorityQueue
import heapq

''' Strongle connected components'''


class Graph:

    def __init__(self, vertex):
        self.v = vertex
        self.graph = defaultdict(set)  # Changed to set factory

    def add_edge(self, s, d):
        self.graph[s].add(d)

    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end=' ')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.push(d)

    def transpose(self):
        g = Graph(self.v)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):  # TODO
        """ Kosaraju's Algorithm.
        O(V+E)
        """
        stack = Stack()
        visited_vertex = [False for _ in range(self.v)]

        for i in range(self.v):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False for _ in range(self.v)]

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print('')


class GraphMatrix:

    def __init__(self, size, edges=None, adjMatrix=None):
        self.edges = edges or [[0 for _ in range(size)] for _ in range(size)]

        self.adjMatrix = adjMatrix or [[0 for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_edge(self, v1, v2, cost=1):
        if v1 == v2:
            print(f'Same vertex {v1} and {v2}')
        else:
            self.adjMatrix[v1][v2], self.adjMatrix[v2][v1] = 1, 1
            self.edges[v1][v2], self.edges[v2][v1] = cost, cost

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f'No edge between {v1} and {v2}')
            return
        self.adjMatrix[v1][v2], self.adjMatrix[v2][v1] = 0, 0
        self.edges[v1][v2], self.edges[v2][v1] = 0, 0

    def __len__(self):
        return self.size

    def __str__(self):
        f = ''
        for row in self.adjMatrix:
            for val in row:
                f += f'{val}\t'
            f += '\n'
        return f

    def dijkstra(self):
        def to_be_visited():
            nonlocal visited_and_distance
            nonlocal num_of_vertices
            v = -10
            for index in range(num_of_vertices):
                if (visited_and_distance[index][0] == 0 and
                        (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1])):
                    v = index
            return v

        num_of_vertices = len(self.adjMatrix)
        visited_and_distance = [[0, 0]] + [[0, sys.maxsize] for _ in range(num_of_vertices - 1)]

        for vertex in range(num_of_vertices):
            # Find next vertex to be visited
            to_visit = to_be_visited()
            for neighbor_index in range(num_of_vertices):
                # Updating new distances
                if self.adjMatrix[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
                    new_distance = visited_and_distance[to_visit][1] + self.edges[to_visit][neighbor_index]
                    if visited_and_distance[neighbor_index][1] > new_distance:
                        visited_and_distance[neighbor_index][1] = new_distance

                visited_and_distance[to_visit][0] = 1
        i = 0

        # Printing the distance
        for distance in visited_and_distance:
            print("Distance of ", chr(ord('a') + i), " from source vertex: ", distance[1])
            i += 1


class Vertex:
    def __init__(self, key):
        self.v = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def __lt__(self, o):
        return self.v < o.v

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __repr__(self):
        s = f'Vertex {self.v}: color {self.color}; disc {self.disc}; fin {self.fin}; dist {self.dist}; pred\t[{self.pred}]'
        return s

    def __str__(self):
        s = f'Vertex {self.v}'
        return s

    def getId(self):
        return self.v


class GraphList:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.time = 0

    def __getitem__(self, item):
        return self.vertices[item]

    def __str__(self):
        f = ''
        for vertex, value in self.vertices.items():
            f += f'Vertex {vertex}: '
            for connected in value.connectedTo:
                f += f'{connected} '
            f += f'\n'
        return f

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertices[n] if n in self.vertices else None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setCOLOR('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def bfs(self, start: Vertex):
        """
        O(V)
        """
        start.setDistance(0)
        start.setPred(None)
        queue = deque([start])
        while queue:
            current_vertex = self[queue.popleft().id]
            # print('>>>', current_vertex.id)
            for neighbor in current_vertex.connectedTo:
                # print(neighbor.id, len(current_vertex.connectedTo))
                neighbor = self[neighbor.id]
                if neighbor.color == 'white':
                    neighbor.setColor('gray')
                    neighbor.setDistance(current_vertex.getDistance() + 1)
                    neighbor.setPred(current_vertex)
                    queue.append(neighbor)
            current_vertex.setColor('black')

    def dijkstra(self, start):
        """
        Finally, let us look at the running time of Dijkstra’s algorithm.
        We first note that building the priority queue takes O(V) time since we initially
        add every vertex in the graph to the priority queue. Once the queue is constructed the
        while loop is executed once for every vertex since vertices are all added at the
        beginning and only removed after that. Within that loop each call to delMin, takes
        O(logV) time. Taken together that part of the loop and the calls to delMin take O(Vlog(V)).
        The for loop is executed once for each edge in the graph, and within the for loop the call
        to decreaseKey takes time O(Elog(V)). So the combined running time is O((V+E)log(V)).
        """
        pq = PriorityQueue()
        start = self[start]
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v.v) for v in self])
        while not pq.isEmpty():
            currentVert = self[pq.delMin()]
            for nextVert in currentVert.getConnections():
                # nextVert = self[nextVert.v]
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert.v, newDist) # rework


def build_graph(graph_dict, weights=None):
    # weights =weights
    """
    values must be in sets or in lists
    """
    # g = graph_dict.copy
    graph = GraphList()
    for vertex in graph_dict:
        graph.addVertex(vertex)
        verteces = graph_dict[vertex]
        while verteces:
            graph.addEdge(vertex, verteces.pop()) # TODO

    return graph


def traverse(y: Vertex):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

# class AdjNode:
#
#     def __init__(self, value):
#         self.vertex = value
#         self.next = None
#
#
# class GraphList:
#
#     def __init__(self, num, weights=None):
#         self.v = num
#         self.graph = [None for _ in range(self.v)]
#         self.weights = weights or {}
#
#     def add_edge(self, s, d, weight):
#         node = AdjNode(d)
#         node.next = self.graph[s]
#         self.graph[s] = node
#
#         node = AdjNode(s)
#         node.next = self.graph[d]
#         self.graph[d] = node
#
#         self.weights[]
#
#     def __str__(self):
#         f = ''
#         for i in range(self.v):
#             f += f'Vertex {i}:\n'
#             temp = self.graph[i]
#             while temp:
#                 f += f' -> {temp.vertex}'
#                 temp = temp.next
#             f += '\n'
#         return f

# def dijkstra(self, start):
if __name__ == '__main__':
    j = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    b = build_graph(j)
    b.dijkstra('A')