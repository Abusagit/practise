"""
Tree data structure implementation
"""


def tree_list_example():
    """
    example
    """
    myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
    print(myTree)
    print('left subtree = ', myTree[1])
    print('root = ', myTree[0])
    print('right subtree = ', myTree[2])


'''list implementation of binary tree'''


def tree(r):
    """
    recursive bin tree

    lists as trees
    """
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


'''Node and references'''


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if not self.left:
            self.left = BinaryTree(newNode)
        else:  # node with an existing left child
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if not self.right:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


