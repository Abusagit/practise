
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


class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0

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

def knights_graph(board_size):
    """makes one pass over the entire board"""
    ktGraph = g.Graph()
    for row in range(board_size):
        for col in range(board_size):
            nodeId = _posToNodeId(row, col, board_size)
            newPositions = _genLegalMoves(row, col, board_size)
            for x, y in newPositions:
                nid = _posToNodeId(x, y, board_size)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def _posToNodeId(row, column, board_size):
    return (row * board_size) + column


def _genLegalMoves(x, y, board_size):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for x_, y_ in moveOffsets:
        newX = x + x_
        newY = y + y_
        if legalCoord(newX, board_size) and legalCoord(newY, board_size):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x,bdSize):
    return True if 0 <= x < bdSize else False


def orderByAvail(n):
    """
    The problem with using the vertex with the most available moves as your next vertex on the path is that it tends
    to have the knight visit the middle squares early on in the tour. When this happens it is easy for the knight to
    get stranded on one side of the board where it cannot reach unvisited squares on the other side of the board. On
    the other hand, visiting the squares with the fewest available moves first pushes the knight to visit the squares
    around the edges of the board first. This ensures that the knight will visit the hard-to-reach corners early and
    can use the middle squares to hop across the board only when necessary. Utilizing this kind of knowledge to speed
    up an algorithm is called a heuristic. Humans use heuristics every day to help make decisions, heuristic searches
    are often used in the field of artificial intelligence. This particular heuristic is called Warnsdorff’s
    algorithm, named after H. C. Warnsdorff who published his idea in 1823.
    """
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def knights_tour(n, path, u, limit):
    """
    param n: current depth in the search tree
    param path: a list of vertices visited up to this point
    param u: the vertex in the graph we wish to explore
    param limit: he number of nodes in the path
    """
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knights_tour(n + 1, path, nbrList[i], limit)
            i += 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setcolor('black')
    else:
        done = True
    return done


if __name__ == '__main__':
    knights_graph(8)