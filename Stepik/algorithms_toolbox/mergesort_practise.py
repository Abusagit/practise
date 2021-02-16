inversion_count = 0

def merge_arrays2(left, right):
    global inversion_count
    new = [None for _ in range(len(left) + len(right))]
    i = j = n = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new[n] = left[i]

            i += 1
        else:
            new[n] = right[j]
            inversion_count += len(left) - i
            j += 1
        n += 1

    new[n:] = left[i:]
    n += len(left) - i
    new[n:] = right[j:]
    return new


def merge_sort_2(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    L = merge_sort_2(array[:middle])
    R = merge_sort_2(array[middle:])
    return merge_arrays2(L, R)


n = int(input())
A = [int(i) for i in input().split()]
merge_sort_2(A)
print(inversion_count)