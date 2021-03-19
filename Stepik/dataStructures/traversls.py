import sys

class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.left = left
        self.right = right
        self.parent = parent


class Tree:
    def __init__(self, n):
        self.root = None
        self.n = n
        self.structure = {None: None}
        self.nodes = {}
        self.parents = {}

    def _print(self, node, indent='', last=True):
        if node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write('R----')
                indent += '\t'
            else:
                sys.stdout.write('L----')
                indent += '|\t'

            print(f'{node.key} ({node.payload})')
            self._print(node.left, indent, last=False)
            self._print(node.right, indent)

    def __str__(self):
        self._print(node=self.root)
        return ''

    def add(self, key, value, left, right):
        node = Node(key, value, left, right)
        if not self.root:
            self.root = node
        if left:
            self.parents[left] = value

        if right:
            self.parents[right] = value

        self.structure[value] = node
        self.nodes[key] = node

    def adjust_relation(self):
        for index in range(self.n):
            self.structure[index].parent = self.structure[self.parents.get(index)]
            self.structure[index].left = self.structure[self.structure[index].left]
            self.structure[index].right = self.structure[self.structure[index].right]

    def inorder(self, root: Node):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=' ')

    def _find(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if node.key > key:
            return self._find(node.left, key)
        if node.key < key:
            return self._find(node.right, key)

    def check2(self, keys):
        if keys:
            for key in keys:
                if not self._find(self.root, key):
                    break
            else:
                print('CORRECT')
                return

        print('INCORRECT')

    def __inorder(self, root, answer=None):
        answer = answer or []
        if root:
            self.__inorder(root.left, answer=answer)
            answer.append(root.key)
            self.__inorder(root.right, answer=answer)
        return answer

    def check(self):
        traversal = self.__inorder(self.root)
        print(traversal)
        min_ = float('-inf')
        for i in range(len(traversal) - 1):
            min_ = max(min_, traversal[i])
            if min_ > traversal[i + 1]:
                break
        else:
            return 'CORRECT'
        return 'INCORRECT'


def readTree():
    stdin = iter(sys.stdin.read().strip().split('\n'))
    n = int(next(stdin))
    t = Tree(n)
    nodes = tuple(tuple(map(int, next(stdin).split())) for _ in range(n))
    # print(nodes)
    keys_ = (i[0] for i in nodes)

    for index, (key, left, right) in enumerate(nodes):
        left = left if left != -1 else None
        right = right if right != -1 else None

        t.add(key, value=index, left=left, right=right)
    t.adjust_relation()
    return t, keys_


def read():
    n = int(sys.stdin.readline().strip())
    # print(n)
    stdin = sys.stdin.read().strip().split('\n')
    t = Tree(n)

    nodes = sorted(tuple(map(int, stdin[i].split())) for i in range(n))

    if nodes:
        for index, (key, left, right) in enumerate(nodes):
            left = left if left != -1 else None
            right = right if right != -1 else None

            t.add(key, value=index, left=left, right=right)
        t.adjust_relation()
        return t, (i[0] for i in nodes)
    return t, None


bin_tree, keys = read()
# bin_tree.inorder(bin_tree.root)
# print()
# bin_tree.preorder(bin_tree.root)
# print()
# bin_tree.postorder(bin_tree.root)
print(bin_tree.check())


