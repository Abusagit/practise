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