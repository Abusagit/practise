from DSA.structures import balancedTree

import sys

class Tree(balancedTree.AVLTree):
    def __init__(self):
        super(Tree, self).__init__()
        self.s = 0

    def func(self, x, y):
        p = 1_000_000_001
        start = (x + self.s) % p
        finish = (y + self.s) % p

        return start, finish

    def summ(self, left, right):
        start, finish = self.func(left, right)


t = Tree()
commands = {'+': t.put, '-': t.remove, '?': t.__contains__, 's': t.summ}

stdin = iter(sys.stdin.read().strip().split('\n'))
n = next(stdin)

for i in stdin:
    i = i.split()
    cmd, values = i[0], tuple(map(int, i[1:]))
    commands[cmd](*values)
