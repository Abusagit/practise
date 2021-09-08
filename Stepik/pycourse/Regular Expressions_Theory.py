import re

pattern = r'abc'
string = 'abc'
string2 = 'acc'
string3 = 'babc'
match_object = re.match(pattern, string)  # Проверяем, подходит ли строка под шаблон
match_object2 = re.match(pattern, string2)
match_object3 = re.match(pattern, string3)  #
print(1, match_object)  # span - с какой по какую позицию в строке string находится pattern,
print(2, match_object2)  # строка не подходит под шаблон
print(3, match_object3)  # Строка начинается с другого символа
"""re.match()ищет совпадение по заданному шаблону в НАЧАЛЕ СТРОКИ"""

"""re.search"""
search_object = re.search(pattern, string3)
print(4, search_object)  # Нашёл вхождение

print()

"""Мета-символы"""

"""[] - множество символов, подходящих под шаблон"""

pattern = r'a[abc]c'
string = 'abc'
string2 = 'aac'
string3 = 'acc'
match_object = re.match(pattern, string)
match_object2 = re.match(pattern, string2)
match_object3 = re.match(pattern, string3)
print(match_object)
print(match_object2)
print(match_object3)

"""re.findall"""
string = 'abc, acc, aac, asdacawfdaw'
all_inclusions = re.findall(pattern, string)  # Все вхождения шаблона внутри строки
print(all_inclusions)

"""re.sub"""
fixed_typos = re.sub(pattern, 'ФФФ', string)  # Исправить то, что подходит под шаблон, на 'abc
print(fixed_typos)

""""""
pattern = r' english?'  # Вопросительный знак - метасимвол - поэтому match=' english'
string = 'Do you speak english?'
match = re.search(pattern, string)
print(match)  # Вопросительный знак - метасимвол - поэтому match=' english'

# надо экранировать
pattern = r'english\?'
match = re.search(pattern, string)
print(match)  # вот теперь match='english?'
print()

""". ^ $ * + ? {} [] \ | () - метасимволы!!!!!!"""

pattern = r'a[a-d]c'  # диапазон символов
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)

pattern = r'a[a-zA-z]c'  # перечислить все маленькие буквы и все большие буквы английского алфавита

string = 'abc, acc, aac, adc, aHC, azc, agc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)  # Всё подошло

pattern = r'a[^a-zA-Z]c'  # ^ - говорит, каких символов не должно быть, выведутся только подходящие
string = 'abc, a.c, a*c, adc, aHC, a,c, agc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

"""
^ - карет, обозначает либо начало строки, либо инвертирование группы символов. 
                (например: "^[^0-9]" — не-цифра в начале строки).

СОКРАЩЁННЫЕ СИМВОЛЫ
\d ~ [0-9] — цифры

\D ~ [^0-9] - не цифры

\s ~ [ \t\n\r\f\v] — пробельные символы (сам пробел + другие символы переноса)

\S ~ [^ \t\n\r\f\v]

\w ~ [a-zA-Z0-9_] — буквы + цифры + _

\W ~ [^a-zA-Z0-9_]
"""
print()

pattern = r'a\wc'
string = 'abc, a.c, a*c, adc, aHC, a,c, agc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'a[\w.]c'
string = 'abc, a.c, a*c, adc, aHC, a,c, agc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'a.c'  # метасимвол точка - под неё подходит любой символ кроме переноса строки
string = 'abc, a.c, a*c, adc, aHC, a,c, agc, AHSGD, hss, aJc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab*a'  # * - интересует любое число символов b, включая 0
string = 'aa, aba, abba, abc, abbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab+a'  # * - интересует только положительное число включений символов b
string = 'aa, aba, abba, abc, abbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab?a'  # ? - интересует 0 или 1 вхождение символа b
string = 'aa, aba, abba, abc, abbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab{3}a'  # {3} - интересует 3 вхождения символа b
string = 'aa, aba, abba, abc, abbba, abbbbbbbbbbbc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab{2,4}a'  # {2, 4} - интересует от 2 до 4 вхождений символа b
string = 'aa, aba, abba, abbba, abbbba, abbbbbbbbbbbc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

print("""Мета-символы по умолчанию жадные и берут максимальное вхождение""", end='\n\n')
pattern = r'a[ab]+a'  #
string = 'abaaba'
match = re.match(pattern, string)
print(match)
print(re.findall(pattern, string))

pattern = r'a[ab]+b'  #
string = 'abaaba'
match = re.match(pattern, string)
print(match)
print(re.findall(pattern, string))

print("""\nПопросить искать нежадным способом, искать наименьшее число вхождений""", end='\n\n')
pattern = r'a[ab]+?a'  #
string = 'abaaba'
match = re.match(pattern, string)
print(match)
print(re.findall(pattern, string))  # айдём оба вхождения строки aba  в строку string

print("""\nГруппировка символов""", end='\n\n')
"""Для использования метасимволов повтора для группы символов"""
pattern = r'(test)*'
string = 'testtesttest'
match = re.match(pattern, string)
print(match)

print("""\n| - символ или""", end='\n\n')
pattern = r'(test|text)*'  # подъодит и то, что слева и то, что справа
string = 'testtext'
match = re.match(pattern, string)
print(match)

pattern = r'abc|(test|text)*'  # подходит и то, что слева и то, что справа
string = 'testtext'
match = re.match(pattern, string)
print(match)

pattern = r'abc|(test|text)*'  # подъодит и то, что слева и то, что справа
string = 'abc'
match = re.match(pattern, string)
print(match)

print(
    """
Использование методов групп
"""
)

pattern = r'((abc)|(test|text)*)'  # подъодит и то, что слева и то, что справа
string = 'abc'
match = re.match(pattern, string)
print(match)
print(match.groups())  # значения, которые перечислены в порядке открывающих скобок

pattern = r'((abc)|(test|text)*)'  # подъодит и то, что слева и то, что справа
string = 'testtext'
match = re.match(pattern, string)
print(match)
print(match.groups())  # значения, которые перечислены в порядке открывающих скобок


pattern = r'Hello (abc|test)'
string = 'Hello abc'
match = re.match(pattern, string)
print(match)
print(match.group(0))  # Если 0 - всё содержимое
print(match.group(1))  # совпадение по 1-му элементу

print(
    """
Использование уже найденных групп внутри регулярного выражения
    """
)
pattern = r'(\w+)-\1'  # Первая найденная группа будет test, он будет искать совпадение по ней
string = 'test-test'
match = re.match(pattern, string)
print(match)


pattern = r'(\w+)-\1'  # !!????????????????????????????????
string = 'test-test chow-chow'
duplicates = re.sub(pattern, r'\1', string)
print(duplicates)

print(


    """
ПОСТАНОВКА ФЛАЖКОВ
"""
)

x = re.match(r'text', 'TEXT', re.IGNORECASE)
print(x, end='\n\n')

x = re.match(r'(te)*xt', 'TEXT', re.IGNORECASE | re.DEBUG)
print(x)

