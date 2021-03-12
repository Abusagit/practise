import unittest


class HeapCounter:
    def __init__(self, items):
        self.heap = items
        self.exchanges = []
        self.margin_index = len(items) - 1
        self.heapify()

    def heapify(self):
        i = len(self.heap) // 2
        while i >= 0:
            self.perc_down(i)
            i -= 1
        print(len(self.exchanges))
        for x in self.exchanges:
            print(*x)


    def perc_down(self, index):
        while index * 2 + 1 <= self.margin_index:
            if index * 2 + 1 > self.margin_index:
                minimal_child_index = self.margin_index
            elif index * 2 + 2 > self.margin_index:
                minimal_child_index = index * 2 + 1
            elif self.heap[index * 2 + 2] > self.heap[index * 2 + 1]:
                minimal_child_index = index * 2 + 1
            else:
                minimal_child_index = index * 2 + 2

            if self.heap[index] > self.heap[minimal_child_index]:
                self.exchanges.append((index, minimal_child_index))
                self.heap[index], self.heap[minimal_child_index] = self.heap[minimal_child_index], self.heap[index]
            index = minimal_child_index


class HeapTest(unittest.TestCase):
    def test1(self):
        self.heap1 = HeapCounter([0, 1, 2, 3, 4, 5])
        self.assertTrue(len(self.heap1.exchanges) == 0)

    def test2(self):
        self.heap2 = HeapCounter([7, 6, 5, 4, 3, 2])
        self.assertTrue(len(self.heap2.exchanges) == 4, f'got {len(self.heap2.exchanges)}: {self.heap2.exchanges}, heap:'
                                                        f' {self.heap2.heap}')


if __name__ == '__main__':
    unittest.main()
