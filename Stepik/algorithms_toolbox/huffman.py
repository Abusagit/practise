import heapq # очередь с приоритетами
from collections import Counter # считает сразу количество символов

class Node():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf():
    def __init__(self, char):
        self.char = char
    def walk(self, code, acc):
        code[self.char] = acc or '0'

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def encoder():
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)
    return encoded


def huffman_decode(s, codes):
    d = {code: char  for char, code in codes.items()}
    acc = ''
    string = ''
    for i in s:
        acc += i
        if acc in d:
            string += d[acc]
            acc = ''
    return string

def _test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = ''.join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s


if __name__ == '__main__':
    # encoder()
    def huffman_decode1(s, codes):
        acc = ''
        string = ''
        for i in s:
            acc += i
            if acc in codes:
                string += codes[acc]
                acc = ''
        return string


    a, b = map(int, input().split())
    codes = {}
    for _ in range(a):
        ch, code = input().split(': ')
        codes[code] = ch
    string = input()
    print(huffman_decode1(string, codes))
