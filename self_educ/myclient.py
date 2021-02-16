import self_educ.my_mod as m  # В __dict__ нет этих модулей, так как мы просто ссылаемся на них
# если бы был оператор from, то имя бы сохранилось в пространстве имён модуля
print(m.countLines(r'C:\Users\Fyodor\PycharmProjects\untitled\rna_count.py'),
      m.countChars(r'C:\Users\Fyodor\PycharmProjects\untitled\rna_count.py'))