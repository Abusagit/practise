from collections import deque
import sys


class HashFunc:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.table = [deque() for _ in range(m)]
        self.hash = {}
        self.funcs = {'add': self.add, 'del': self.delete, 'find': self.find, 'check': self.check}
        self.processing()

    def add(self, string):
        h = self.hash.get(string, self.hash_(string))
        if string not in self.table[h]:
            self.table[h].appendleft(string)

    def delete(self, key):
        h = self.hash.get(key, self.hash_(key))
        table = self.table[h]
        if key in table:
            del table[table.index(key)]

    def find(self, key):
        h = self.hash.get(key, self.hash_(key))

        a = 'yes' if key in self.table[h] else 'no'
        print(a)

    def check(self, i):
        i = int(i)
        if not self.table[i]:
            print('')
        else:
            print(*self.table[i])

    def hash_(self, string):
        m = self.m
        h = 0
        p = 1_000_000_007
        x = 263
        for index, value in enumerate(string):
            h += ((ord(value)) * (x ** index))
            # print(h)
        h %= p
        h %= m

        self.hash[string] = h

        return h

    def processing(self):
        global stdin
        for _ in range(self.n):
            cmd, val = next(stdin).split()
            self.funcs[cmd](val)


stdin = iter(sys.stdin.read().strip().split('\n'))
m = int(next(stdin))
n = int(next(stdin))

f = HashFunc(n=n, m=m)
# print(f.hash)

# h = 0
# x = 263
# p = 1_000_000_007
# for index, value in enumerate('world'):
#     h += ord(value) * x ** index
# h %= p
# h %= 5
#
# print(h)