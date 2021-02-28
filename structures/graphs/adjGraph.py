#
#  adjGraph
#
#  Created by Brad Miller on 2005-02-24.
#  Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights reserved.
#

import sys
import os
import unittest
from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def __getitem__(self, item):
        return self.vertices[item]

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


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = float('inf')
        self.pred = None
        self.disc = 0
        self.fin = 0

    def __lt__(self, o):
        return self.id < o.id

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

    def __str__(self):
        s = f'{self.id}: color {self.color}; disc {self.disc}; fin {self.fin}; dist {self.dist}; pred \t[{self.pred}]'
        return s

    def getId(self):
        return self.id


def build_graph(graph_dict):
    """
    values must be in sets or in lists
    """
    graph = Graph()
    for vertex in graph_dict:
        graph.addVertex(vertex)
        verteces = graph_dict[vertex]
        while verteces:
            graph.addEdge(vertex, verteces.pop())

    return graph


def bfs(graph: Graph, start: Vertex):
    """
    O(V)
    """
    start.setDistance(0)
    start.setPred(None)
    queue = deque()
    queue.append(start)
    while queue:
        current_vertex = graph[queue.popleft().id]
        # print('>>>', current_vertex.id)
        for neighbor in current_vertex.connectedTo:
            # print(neighbor.id, len(current_vertex.connectedTo))
            neighbor = graph[neighbor.id]
            if neighbor.color == 'white':
                neighbor.setColor('gray')
                neighbor.setDistance(current_vertex.getDistance() + 1)
                neighbor.setPred(current_vertex)
                queue.append(neighbor)
        current_vertex.setColor('black')


def traverse(y: Vertex):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())
# def bfs(g, start):
#     start.setDistance(0)
#     start.setPred(None)
#     vertQueue = deque()
#     vertQueue.append(start)
#     while vertQueue:
#         currentVert = vertQueue.popleft()
#         for nbr in currentVert.getConnections():
#             if nbr.getColor() == 'white':
#                 nbr.setColor('gray')
#                 nbr.setDistance(currentVert.getDistance() + 1)
#                 nbr.setPred(currentVert)
#                 vertQueue.append(nbr)
#         currentVert.setColor('black')





def knight_tour():
    pass


class adjGraphTests(unittest.TestCase):
    def setUp(self):
        self.tGraph = Graph()

    def testMakeGraph(self):
        gFile = open("test.dat")
        for line in gFile:
            fVertex, tVertex = line.split('|')
            fVertex = int(fVertex)
            tVertex = int(tVertex)
            self.tGraph.addEdge(fVertex, tVertex)
        for i in self.tGraph:
            adj = i.getAdj()
            for k in adj:
                print(i, k)


if __name__ == '__main__':
    unittest.main()
