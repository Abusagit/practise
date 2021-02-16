from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


def random_generator(k):
    for i in range(k):
        yield random()
# Верунть K раз случайное значение. YIELD -  вернуть значение функции сразу
    # несколько раз, спрашивать при помощи next, если есть yield - функция стала генератором
    # Исполнение тела функции начнётся тогда, когда попросим исполнить, начнёт с самого начала исполнять функцию
    # до первого ключевого слова yield, после возврата значения - запоминается состояние функции
    #  генератор знает целиком все тело функции


def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    yield 2
    print('Checkpoint 3')


gen = random_generator(3)
# for i in gen:
#     print(i)
# g = simple_gen()


"""
    Создание класса - итератора, который создаёт объект-итератор
    Итератор - это класс, в котором определена функция __next__
    __next_ - о что возвращает объект итератор
    __iter__ - возвращает итератор
    Итератор - отдельный класс
"""


class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            try:
                return self.lst[self.i - 2], self.lst[self.i - 1]
            except IndexError:
                return self.lst[self.i - 2], None
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


# L = [1, 2, 3, 4, 5]
# x = MyList(L)
# print(x)
# for pair in x:
#     print(pair)


