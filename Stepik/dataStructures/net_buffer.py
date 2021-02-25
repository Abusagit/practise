from collections import deque
import sys


def processing(size, number):
    processes = [tuple(map(int, input().split())) for _ in range(number)]
    # for _ in range(number):
    #     arrival, duration = map(int, input().split())
    #     processes.append((arrival, duration))
    # print(processes)
    deq = deque()
    for arrival, duration in processes:
        while deq and arrival >= sum(deq[0]):
            deq.popleft()
        if not deq:
            print(arrival)
            deq.append((arrival, duration))
        elif len(deq) >= size or arrival < sum(deq[-1]):
            print(-1)
        else:
            print(arrival)
            deq.append((arrival, duration))



if __name__ == '__main__':
    processing(2, 8)
