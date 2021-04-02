import sortings as s

# if __name__ == '__main__':
#     ar = [5, 3, 6, 2, 10]
#     l = [1, 5, 6, 2]
#     print(s.selectionSort(ar))
#     print(s.quickSort(ar))
#     print(s.quickSort([5, 3, 6, 2, 10]))
#     print(s.quickSort(l))
#
#
#
#     def test_sort(func):
#         print(f'{func.__name__} is being tested')
#         print('Testcase #1', end=' - ')
#         a = [4, 2, 5, 1, 3]
#         a_sorted = [1, 2, 3, 4, 5]
#         func(a)
#         print('Ok' if a == a_sorted else 'Fail')
#
#         print('Testcase #1', end=' - ')
#         a = list(range(10, 20)) + list(range(10))
#         a_sorted = list(range(20))
#         func(a)
#         print('Ok' if a == a_sorted else 'Fail')
#
#         print('Testcase #1', end=' - ')
#         a = [4, 2, 4, 2, 1]
#         a_sorted = [1, 2, 2, 4, 4]
#         func(a)
#         print('Ok' if a == a_sorted else 'Fail')
#
#     test_sort(s.insert_sort)
#     test_sort(s.choise_sort)
#     test_sort(s.bubble_sort)
#
#     print(s.quickSort([4, 4, 4, 1, 5, 6, 8, 6, 9, 1]))
#
#     print(s.check_sorted([1, 1, 1, 1, 1, 1, 5, 5, 6], ascending=True))
#
#     print(s.check_sorted([1, 1, 1, 1, 1, 1, 5, 5, 6], ascending=False))
#
#     print(s.check_sorted([5, 4, 3, 2, 1], ascending=False), end='\n\n')
#
#     # print(merge_sort(ar))
#     r = [4, 4, 4, 1, 5, 6, 8, 6, 9, 1]
#     t = s.merge_sort(r)
#     print(t)
#     print(s.check_sorted(t))
#     print(r)
#
#
#     h = [4, 5, 1, 6, 7, 2, 8, 2, 4356, 9, 1, 3, 3, 3]
#
#     print(s.quickSort(h))
#     print(s.merge_sort(h))
#     print(s.heapsort(h))


print(s.countingSort([4, 2, 2, 8, 3, 3, 1]))
a = [121, 432, 564, 23, 1, 45, 788]
print(a)
s.radixSort(a)
print(a)
