import heapq

class Heap_Max():
    def __init__(self, heap):
        self.heap = []

    def __getitem__(self, item):
        return self.heap[item]

    def __len__(self):
        return len(self.heap)

    def ParentPosition(self, i):
        return int((i - 1) / 2)

    def LeftChildPos(self, i):
        return 2 * i + 1

    def RightChildPos(self, i):
        return 2 * i + 2

    def hasParent(self, i):
        return self.ParentPosition(i) < len(self.heap)

    def hasLeftChild(self, i):
        return self.LeftChildPos(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.RightChildPos(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self) - 1)

    def getMax(self):
        self.heap[0], self.heap[len(self) - 1] = self.heap[len(self) - 1], self.heap[0]
        m = self.heap.pop()
        self.siftDown(0)
        return m

    def heapify(self, i):
        while self.hasParent(i) and self.heap[i] > self.heap[self.ParentPosition(i)]:
            self.heap[i], self.heap[self.ParentPosition(i)] = self.heap[self.ParentPosition(i)], self.heap[i]
            i = self.ParentPosition(i)

    def siftDown(self, i):
        l = self.hasLeftChild(i)
        r = self.hasRightChild(i)
        while l or r:
            left = self.heap[self.LeftChildPos(i)] if l else -12124
            right = self.heap[self.RightChildPos(i)] if r else-124124
            if right < self[i] < left:
                self.heap[i], self.heap[self.LeftChildPos(i)] = self.heap[self.LeftChildPos(i)], self.heap[i]
                i = self.LeftChildPos(i)
            elif left < self[i] < right:
                self.heap[i], self.heap[self.RightChildPos(i)] = self.heap[self.RightChildPos(i)], self.heap[i]
                i = self.RightChildPos(i)

    def __str__(self):
        return self.heap


# class Heap():
#     def __init__(self):
#         self.heap = []
#
#     def parent(self, pos):
#         return (pos - 1) // 2





class Heap():
    def __init__(self, heap=[]):
        self.heap = heap

    def sift_up(self, i):
        while i > 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2

    def sift_down(self, i):
        while 2 * i + 1 <= len(self.heap) - 1:
            j = i
            if self.heap[2 * i + 1] > self.heap[i]:
                j = 2 * i + 1
            if 2 * i + 2 <= len(self.heap) - 1 and self.heap[2 * i + 2] > self.heap[j]:
                j = 2 * i + 2
            if i == j:
                break
            else:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j


    def insert(self, item):
        self.heap.append(item)
        self.sift_up(len(self.heap) - 1)


    def get_max(self):
        m = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return m


def commander(n):
    a = Heap()
    for _ in range(n):
        cmd = input().split()
        if len(cmd) == 2:
            a.insert(int(cmd[1]))
        else:
            print(a.get_max())


if __name__ == '__main__':
    # h = []
    # for _ in range(int(input())):
    #     cmd = input()
    #     if cmd.startswith('Insert'):
    #         val = int(cmd.split()[1])
    #         h.append(val)
    #         heapq._heapify_max(h)
    #     else:
    #         print(heapq._heappop_max(h))
    commander(int(input()))