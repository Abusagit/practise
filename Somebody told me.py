class MyDescriptor(object):
    """Это класс дескриптора."""

    def __get__(self, instance, owner):
        # Зачастую здесь возвращают значение, хранящееся в instance -
        # см. my_owner ниже.
        return 'Экземпляр %s, класс %s' % (instance, owner)


class MyOwner(object):
    """Это класс владелец дескрипторов."""

    field1 = MyDescriptor()
    field2 = MyDescriptor()


my_owner = MyOwner()
print(my_owner.field1)

my_owner.__dict__['field1'] = 'some'
print(my_owner.field1)  # some


# Rabin-Karp algorithm in python


d = 10

def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i+1))

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q


text = "baaaaaaa"
pattern = "aaaaa"
q = 13
search(pattern, text, q)
