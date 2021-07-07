def max_value(array):
    val = array[0]
    if len(array) == 1:
        return val
    return max(val, max_value(array[1:]))


print(max_value([1, 2, 4, 6, 10, 5, 6]))