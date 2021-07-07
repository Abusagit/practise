import unittest
from DSA.structures.queues import PriorityQueue


class Prior(PriorityQueue):

    def delMin(self):
        retval = self.heapArray[1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize -= 1
        self.heapArray.pop()
        self.percDown(1)
        return retval


class Parrallel:
    def __init__(self, number, tasks):
        self.number = number
        self.kernels = {kernel: 0 for kernel in range(number)}
        self.log = {}
        self.t = len(tasks)
        self.tasks = tasks
        self.queue = Prior()

    def __str__(self):
        f = ''
        for i in range(self.t):
            f += f'{self.log[i][0]} {self.log[i][1]}\n'
        return f.strip()

    def emulation(self):
        i = 0
        last = 0
        while i < self.t and last != self.number and len(self.queue) <= self.number:
            self.queue.add(((self.kernels[last] + self.tasks[i], last), i))
            last += 1
            i += 1
        while i < self.t:
            (time, last), task_index = self.queue.delMin()
            self.log[task_index] = (last, self.kernels[last])
            self.kernels[last] += self.tasks[task_index]
            self.queue.add(((self.kernels[last] + self.tasks[i], last), i))
            i += 1
        while self.queue:
            (time, last), task_index = self.queue.delMin()
            self.log[task_index] = (last, self.kernels[last])
            self.kernels[last] += self.tasks[task_index]
        print(self)

if __name__ == '__main__':
    # pc = Parrallel(number=2, tasks=[1, 2, 3, 4, 5])
    # pc.emulation()
    print()
    pc2 = Parrallel(4, [1 for _ in range(20)])
    pc2.emulation()


    class PriorityQueue:
        def __init__(self):
            self.heapArray = [(0, 0)]
            self.currentSize = 0

        def __bool__(self):
            return len(self.heapArray) > 1

        def __repr__(self):
            return f'{self.heapArray[1:]}'

        def __len__(self):
            return len(self.heapArray) - 1  # subtract first supporting element

        def percDown(self, i):
            while (i * 2) <= self.currentSize:
                mc = self.minChild(i)
                if self.heapArray[i][0] > self.heapArray[mc][0]:
                    tmp = self.heapArray[i]
                    self.heapArray[i] = self.heapArray[mc]
                    self.heapArray[mc] = tmp
                i = mc

        def minChild(self, i):
            if i * 2 > self.currentSize:
                return -1
            else:
                if i * 2 + 1 > self.currentSize:
                    return i * 2
                else:
                    if self.heapArray[i * 2][0] < self.heapArray[i * 2 + 1][0]:
                        return i * 2
                    else:
                        return i * 2 + 1

        def percUp(self, i):
            while i // 2 > 0:
                if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                    tmp = self.heapArray[i // 2]
                    self.heapArray[i // 2] = self.heapArray[i]
                    self.heapArray[i] = tmp
                i //= 2

        def add(self, k):
            self.heapArray.append(k)
            self.currentSize += 1
            self.percUp(self.currentSize)

        def delMin(self):
            retval = self.heapArray[1]
            self.heapArray[1] = self.heapArray[self.currentSize]
            self.currentSize -= 1
            self.heapArray.pop()
            self.percDown(1)
            return retval


    class Parallel:
        def __init__(self, number, tasks):
            self.number = number
            self.kernels = {kernel: 0 for kernel in range(number)}
            self.log = {}
            self.t = len(tasks)
            self.tasks = tasks
            self.queue = PriorityQueue()

        def __str__(self):
            f = ''
            for i in range(self.t):
                f += f'{self.log[i][0]} {self.log[i][1]}\n'
            return f.strip()

        def emulation(self):
            i = 0
            last = 0
            while i < self.t and last != self.number and len(self.queue) <= self.number:
                self.queue.add(((self.kernels[last] + self.tasks[i], last), i))
                last += 1
                i += 1
            while i < self.t:
                (time, last), task_index = self.queue.delMin()
                self.log[task_index] = (last, self.kernels[last])
                self.kernels[last] += self.tasks[task_index]
                self.queue.add(((self.kernels[last] + self.tasks[i], last), i))
                i += 1
            while self.queue:
                (time, last), task_index = self.queue.delMin()
                self.log[task_index] = (last, self.kernels[last])
                self.kernels[last] += self.tasks[task_index]
            print(self)


    n, m = map(int, input().split())
    a = Parallel(n, [int(i) for i in range(m)])
    a.emulation()