def countLines(file):
    with open(file) as name:
        number = 0
        while name.readline():
            number += 1
    return number


def countChars(file):
    with open(file) as name:
        return len(name.read())


def test(name = 'test.txt'):
    for repeats in (countLines, countChars):
        print(repeats(name))

if __name__ == '__main__':
    test()
    test('my_mod.py')
    print(countChars('test.txt'))