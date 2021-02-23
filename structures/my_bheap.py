class BinHeap:
    def __init__(self):
        self.heapList = [0] # isn`t used and simplifies division and parent recognition
        self.currentSize = 0

    def siftUp(self, i):
        while i // 2 > 0 and self.heapList[i] < self.heapList[i // 2]:
            self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.siftUp(self.currentSize)

    def minChild(self, i):
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        if self.heapList[2 * i] < self.heapList[2 * i + 1]:
            return 2 * i
        return 2 + i + 1

    def siftDown(self, i):
        while 2 * i <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.siftDown(1)
        return retval

    def buildHeap(self, lst):
        i = len(lst) // 2
        self.currentSize = len(lst)
        self.heapList.extend(lst)
        while i > 0:
            self.siftDown(i)
            i -= 1


if __name__ == '__main__':
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())