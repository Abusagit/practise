def b_s(lst, key):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == key:
            return mid + 1
        elif lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return - 1


n, *A = map(int, input().split())
k, *numbers = map(int, input().split())

for number in numbers:
    print(b_s(A, number), end=' ')