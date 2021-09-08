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
        if len(deq) >= size:
            print(-1)
        elif not deq:
            deq.append((arrival, duration))
            print(arrival)
        else: # something in deque
            if arrival >= sum(deq[-1]):
                print(arrival)
                deq.append((arrival, duration))
            else:
                print(sum(deq[-1]))
                deq.append((sum(deq[-1]), duration))


if __name__ == '__main__':
    processing(1, 5)
