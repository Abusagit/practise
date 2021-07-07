import datetime


# now_date = datetime.date.today()  # Текущая дата (без времени)
# now_time = datetime.datetime.now()  # Текущая дата со временем
# #print(now_date)
#
# cur_year = now_date.year  # Год текущий
# cur_month = now_date.month  # Месяц текущий
# cur_day = now_date.day  # День текущий
# cur_hour = now_time.hour  # Час текущий
# cur_minute = now_time.minute  # Минута текущая
# cur_second = now_time.second  # Секунда текущие
# num_week = now_date.isoweekday()  # узнаем день недели (от 1 до 7)
#
# now_date = now_date.replace(2011, 6, 30)  # меняем полностью дату на 30.06.2011
# now_date = now_date.replace(day=cur_day)  # меняем только день
# now_date = now_date.replace(month=cur_month)  # меняем только месяц
# now_date = now_date.replace(year=cur_year)  # меняем только год
#
# ny_2011 = datetime.date(2011, 2, 1)  # создали дату: 1 февраля 2011 года
# delta = ny_2011 - now_date  # разница (дельта) в между 2-мя датами
#
# delta = datetime.timedelta(days=2)  # дельта в 2 дня
# now_date = now_date + delta  # Узнаем какое число будет через 2 дня
# #print(now_date)
# now_date = now_date - delta  # или какое число было 2 дня назад
# #print(now_date)
# print(now_time.strftime("%d.%m.%Y %I:%M %p"))  # форматируем дату


"""
%S — секунды. От 0 до 61
%M — минуты. От 00 до 59
%H — час. От 00 до 23
%I — час. От 1 до 12
%p -После перед полуднем или после (AM или PM)
%d — день. От 1 до 31
%j — день как номер года. От 001 до 366
%m — месяц. От 01 до 12
%y — год в виде 2-х последних чисел. От 00 до 99
%Y — год в виде полного числа
"""


year, month, day = map(int, input().split())
date = datetime.date(year=year, month=month, day=day)
print(date)
x = int(input())
delta = datetime.timedelta(days=x)
new_date = date + delta
print(new_date.year, new_date.month, new_date.day)
