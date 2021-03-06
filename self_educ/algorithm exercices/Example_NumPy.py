from numpy import *

a = array([2, 3, 4])  # Одномерный массив из списка целых чисел
print(a)
print(a.ndim)  # Просмотр размерности массива (a - одномерный массив)
print(a.shape)  # Размер массива - количество элементов - исло строк, столбцов и так далее
print()
print(type(a))
b = array([(1.5, 2, 3), (4, 5, 6)])  # оздание двумерного массива из двух последовательностей чисел
print(b)  # Все числа имеют 1 тип - число с плавющей точкой
print(b.ndim)  # Размерность - 2
print(b.shape)  # 2 строки, 3 столбца
print(b.size)  # Количество элементов - 6
print()
z = zeros((3, 2))  # 3 и 2 в отдельных скобках, чтобы считывалась как пара числе - двумерный массив
# из 3 строк и 2 столбцов
print(z)
print()
print(arange(10, 30, 5))  # Генерация массива, начальное значение - 10, конечное - 30, шак - 5. + ВОЗВРАЩАЕТ массив
print()
print(linspace(0, 2, 9))  # Генерация 9 числе на отрезке от 0 до 2 с равным шагом, конец интервала ВКЛЮЧЁН
b = arange(12).reshape(4, 3)  # Превращени еодномерного массива arange в двумерный с помощбю вункции reshape -
# 4 - троки, 3 - столбцы
print(b)
print()
a = array([10, 20, 30])
print(a ** 2)
print(2 * sin(a))
print(a < 20)
