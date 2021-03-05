# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
# deque.py
from collections import deque


class Deque:
    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return self.size()

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.appendleft(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)
