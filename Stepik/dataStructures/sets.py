from DSA.structures import disjoint_sets
import sys


class Solution:
    def __init__(self, elements, request_number: int):
        # self.rank = self.rank = {i: 0 for i in range(len(elements))}
        self.parent = {i: i for i in range(1, len(elements) + 1)}
        self.size = {i: element for i, element in zip(range(1, len(elements) + 1), elements)}
        self.requests = request_number
        self._max = max(elements)

    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def processing(self):
        print(self.size)
        for _ in range(self.requests):
            destination, source = map(int, input().split())

            d = self.find(destination)
            s = self.find(source)

            if d != s:
                self.size[d] += self.size[s]
                self.parent[s] = d
                self.size[s] = 0
                self._max = max(self.size[d], self._max)

            print(self._max)


class Variables:
    def __init__(self):
        stdin = iter(sys.stdin.read().strip().split('\n'))

        self.n, self.e, self.d = map(int, next(stdin).split())
        self.rank = {i: 0 for i in range(1, self.n + 1)}
        self.parent = {i: i for i in range(1, self.n + 1)}
        self.task = (tuple(map(int, i.split())) for i in stdin)

        self.processing()

    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def processing(self):
        for _ in range(self.e):
            i, j = next(self.task)
            self.union(i, j)
            # print(self.parent)
        f = ''
        for i in range(1, self.n + 1):
            f += f'{i} -> {self.find(i)}\t'
        f += '\n'
        # print(f)
        # print(self.find(i))
        for _ in range(self.d):
            i, j = next(self.task)
            # print(i, j)

            # print(f'{i} --> {find_i}    {j} --> {find_j}')
            # print(self.find(i), self.find(j))
            # print(self.find(i), self.find(j))
            if self.find(i) == self.find(j):
                # print()
                print(0)
                break
        else:
            # print()
            print(1)


if __name__ == '__main__':
    # a = Solution([10, 0, 5, 0, 3, 3], 4)
    # a.processing()

    b = Variables()
