import sys
from collections import defaultdict, deque
from DSA.basic import Stack
from DSA.graphs import PriorityQueue

''' Strongle connected components''' # TODO


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
    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.distance = float('inf')
        self.predecessor = None
        self.color = 'white'
        self.discoveryTime = 0
        self.finishTime = 0

    def __repr__(self):
        s = f'Vertex {self.name}: disc {self.disc}; fin {self.finish}; dist {self.distance}; pred\t[{self.predecessor}]'
        return s

    def __str__(self):
        s = f'Vertex {self.name}'
        return s


class GraphList:
    def __init__(self, directed=False):
        self.vertices = {}
        self.time = 0
        self.directed = directed

    def __iter__(self):
        return iter(self.vertices.items())

    def clean_color_predecessor_distance(self):
        for i in self.vertices:
            self[i].color = 'white'
            self[i].predecessor = None
            self[i].distance = float('inf')

    def __getitem__(self, item):
        return self.vertices[item]

    def __contains__(self, item):
        return item in self.vertices

    def __str__(self):
        f = ''
        for vertex, value in self.vertices.items():
            f += f'Vertex {vertex} (predecessor {value.predecessor}):\t-->'
            for connected in value.connections:
                f += f'\t{connected} (cost {value.connections[connected]})\t'
                f += '|'
            f += f'\n'
        return f

    # def addVertex(self, key):
    #     newVertex = Vertex(key)
    #     self.vertices[key] = newVertex
    #     return newVertex

    def addEdge(self, start, finish, cost=1):
        if start not in self.vertices:
            startVertex = Vertex(start)
            self.vertices[start] = startVertex
        if finish not in self.vertices:
            finishVertex = Vertex(finish)
            self.vertices[finish] = finishVertex
        self.vertices[start].connections[finish] = cost
        if not self.directed:
            self.vertices[finish].connections[start] = cost

    def dfs(self):
        self.clean_color_predecessor_distance()
        for aVertex in self:
            if self[aVertex].color == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex_key):
        self[startVertex_key].color = 'grey'
        self.time += 1
        self[startVertex_key].discoveryTime = self.time
        for nextVertex in self[startVertex_key].connections:
            if self[nextVertex].color == 'white':
                self[nextVertex].predecessor = startVertex_key
                self.dfsvisit(nextVertex)
        self[startVertex_key].color = 'black'
        self.time += 1
        self[startVertex_key].finish = self.time

    def bfs(self, start):
        """
                O(V)
                """
        self.clean_color_predecessor_distance()
        self[start].distance = 0
        self[start].predecessor = None
        queue = deque([start])
        while queue:
            currentVertex_key = queue.popleft()
            for neighbor_key in self[currentVertex_key].connections:
                neighbor = self[neighbor_key]
                if neighbor.color == 'white':
                    neighbor.color = 'gray'
                    neighbor.distance = self[currentVertex_key].distance + 1
                    neighbor.predecessor = currentVertex_key
                    queue.append(neighbor_key)
            self[currentVertex_key].color = 'black'

    def traverse(self, toVertex):
        x = self[toVertex]
        while x.predecessor:
            print(x.name)
            x = self[x.predecessor]
        print(x.name)

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
        self.clean_color_predecessor_distance()
        self[start].distance = 0
        pq.buildHeap([(vertex.distance, vertex_key) for vertex_key, vertex in self])
        while not pq.isEmpty():
            current_vertex = self[pq.delMin()]
            for nex_vert_key in current_vertex.connections:
                new_distance = current_vertex.distance + current_vertex.connections[nex_vert_key]
                if new_distance < self[nex_vert_key].distance:
                    self[nex_vert_key].distance = new_distance
                    self[nex_vert_key].predecessor = current_vertex.name
                    pq.decreaseKey(nex_vert_key, new_distance)


def build_graph(dic, costs=None, directed=False):
    g = GraphList(directed=directed)

    if costs:
        for vertex in dic:
            neighbours = dic[vertex]
            while neighbours:
                n = neighbours.pop()
                g.addEdge(vertex, n, cost=costs[vertex][n])  # ?????
    else:
        for vertex in dic:
            neighbours = dic[vertex]
            while neighbours:
                n = neighbours.pop()
                g.addEdge(vertex, n)
    return g

if __name__ == '__main__':
    j = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    weights = {
        'A': {'B': 2, 'C': 1},
        'B': {'A': 2, 'D': 1, 'E': 3},
        'C': {'A': 1, 'F': 1},
        'D': {'B': 1},
        'E': {'B': 3, 'F': 1},
        'F': {'C': 1, 'E': 1}
    }

    graph = build_graph(j, costs=weights)
    print(graph)
    graph.dfsvisit('A')
    print(graph)
    graph.bfs('A')
    print(graph)
    graph.traverse('C')

    print(graph['A'] == graph[graph['C'].predecessor])

    graph.dijkstra('A')

    for v, vertex in graph:
        print(v, vertex.distance, end=' ')
        while vertex.predecessor:
            print(vertex, end=' - ')
            vertex = graph[vertex.predecessor]
        print(vertex)