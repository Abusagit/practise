def sum_(array):
    if array == []:
        return 0
    return array[0] + sum_(array[1:])


print(sum_([1, 2, 3, 4, 5]))