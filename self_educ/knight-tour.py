from DSA.graphs import adjGraph as g


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