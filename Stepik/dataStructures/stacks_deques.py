from DSA.basic import stacks as s
from collections import deque


def commander():
    commands = (command.split() for command in sys.stdin)

    n = next(commands)
    f = s.MaxStack()
    command = {'pop': f.pop, 'max': f.max}
    for cmd, *v in commands:
        if v:
            f.push(int(v[0]))
        else:
            command[cmd]()


def slide_max1(n, m, numbers):
    d1 = deque()
    d2 = deque()
    for _, value in enumerate(numbers):
        if len(d1) < m:
            if d1:
                _max = d1[-1][1] if d1[-1][1] > value else value
                d1.append((value, _max))
            else:
                d1.append((value, value))
        else:
            print(d1[-1][1], end=' ')
            d1.popleft()
            if d1:
                pop = d1.popleft()[0]
                d2.append((pop, pop))
                while d1:
                    val, _ = d1.popleft()
                    _max = d2[-1][1] if d2[-1][1] > val else val
                    d2.append((val, _max))
                _max = d2[-1][1] if d2[-1][1] > value else value
                d2.append((value, _max))
            else:
                d2.append((value, value))
            d1, d2 = d2, d1
    print(d1[-1][1])


def slide_max2(n, m, numbers):
    """
    faster
    """
    if m == 1:
        print(*numbers)
        return
    entry = s.MaxStack()
    out = s.MaxStack()
    numbers = deque(numbers)
    while numbers:
        num = numbers.popleft()
        if out.isEmpty() and len(entry) < m:
            entry.push(num)
            if len(entry) == m:
                while not entry.isEmpty():
                    out.push(entry.pop())
                print(out.max(), end=' ')
                out.pop()
        else:
            entry.push(num)
            print(max(out.max(), entry.max()), end=' ')
            out.pop()



if __name__ == '__main__':
    def test(func):
        n = int(input())
        numbers = [int(i) for i in input().split()]
        m = int(input())
        func(n, m, numbers)

    test(slide_max2)
