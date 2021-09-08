space = {'global': ['None', set()]}  # Список, [0] - родитель, [1] - множество переменной в директории
Answers = []


def create(namespace, parent):
    space[namespace] = []
    space[namespace].append(parent)
    space[namespace].append(set())


def add(namespace, var):
    space[namespace][1].add(var)


def get(namespace, var):
    global Answers
    if var in space[namespace][1]:
        Answers.append(namespace)
        return
    elif space[namespace][0] == 'None' and var not in space[namespace][1]:
        Answers.append('None')
        return
    else:
        get(space[namespace][0], var)


for _ in range(int(input())):
    cmd, namesp, other = input().split()
    if cmd == 'add':
        add(namesp, other)
    elif cmd == 'create':
        create(namesp, other)
    else:
        get(namesp, other)

for answer in Answers:
    print(answer)