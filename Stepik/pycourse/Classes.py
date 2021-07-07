class Dog():
    """Простая модель собаки"""  # жокументация

    def __init__(self, name, age):
        """Инициализируем атрибитов - имя и возраст"""
        self.name = name
        self.age = age
        print(self.name.title() + 'приручен(а)')

    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + ' садится по команде')  # Первое слово - заглавное

    def jump(self):
        print(self.name.title() + ' прыгает по команде')

    def info(self):
        print('Name: ' + self.name, 'Age: ' + str(self.age))


doge = Dog('Mishka', 2)
doge.sit()
doge.jump()
doge.info()


class MoneyBox():
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def can_add(self, amount):
        if amount <= (self.capacity - self.current):
            return True
        else:
            return False

    def add(self, amount):
        if self.can_add(amount):
            self.current += amount


x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)


class Bfr:
    def __init__(self):
        # конструктор без аргументов
        self.current = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.current.extend(a)
        while len(self.current) >= 5:
            print(sum(self.current[0:5]))
            del self.current[0:5]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.current


buf = Bfr()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()

family_tree = {}
answers = []


def define_generation(x):
    for _ in range(x):
        sample = file.readline().strip()
        if ":" in sample:
            child, parent = sample.split(' : ')
            family_tree[child] = parent.split(' ')
        else:
            family_tree[sample] = []


def graph_find_way(graph, start, end, order=[]):
    order = order + [start]
    if start == end:
        return order
    elif start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in order:
            new_order = graph_find_way(graph, node, end, order)
            if new_order:
                return new_order
    return None


with open('C:\\Users\\Fyodor\\Desktop\\test.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline().strip())
    define_generation(n)
    q = int(file.readline().strip())
    for i in range(q):
        x, y = file.readline().strip().split()
        print('%i:' % (i + 1), x, y, sep='\t')
        ANSWER = graph_find_way(family_tree, y, x)
        print(ANSWER)
        if ANSWER is None:
            answers.append('No')
            print("!!!!!!!!!!!!!!!!")
        else:
            answers.append('Yes')
        print()


with open('C:\\Users\\Fyodor\\Desktop\\my_answers.txt', 'w', encoding='utf-8') as file:
    file.writelines("%s\n" % answer for answer in answers)
with open('C:\\Users\\Fyodor\\Desktop\\my_answers.txt', 'r', encoding='utf-8') as my_answers:
    with open('C:\\Users\\Fyodor\\Desktop\\right_answers.txt', 'r', encoding='utf-8') as right_answers:
        string_count = 0
        for _ in range(q):
            my_answer = my_answers.readline().strip()
            right_answer = right_answers.readline().strip()
            string_count += 1
            if my_answer != right_answer:
                print('STRINGS:' + my_answer + '     ' + right_answer)
                print('String with difference: %s' % string_count)
                print('-' * 30)


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]


class Multifilter:

    def judge_half(self, pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(self, pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(self, pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for item in self.iterable:
            neg = 0
            pos = 0
            for function in self.funcs:
                if function(item):
                    pos += 1
                else:
                    neg += 1
            if self.judge(self, pos, neg):
                yield item


print(list(Multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))
# [0, 30]

