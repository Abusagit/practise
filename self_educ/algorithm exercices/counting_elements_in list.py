def counting1(array):
    if len(array) == 1:
        return 1
    return 1 + counting1(array[1:])


def counting2(array):
    if array == []:
        return 0
    return 1 + counting2(array[1:])


a = [1 for i in range(10)]
print(counting1(a))
print(counting2(a))