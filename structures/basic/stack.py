# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
# stack.py

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class MaxStack(Stack):
    def __init__(self):
        super(MaxStack, self).__init__()
        self._max = None

    def max(self):
        print(self._max)  # shows current maximum value in stack

    def push(self, item):
        if self.isEmpty():
            self._max = item
            super(MaxStack, self).push((item, item))
        else:
            if item > self._max:
                super(MaxStack, self).push((item, item))
                self._max = item
            else:
                super(MaxStack, self).push((item, self._max))

    def pop(self):
        pop = super(MaxStack, self).pop()
        self._max = pop[1]
        return pop[0]