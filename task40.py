# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

import calendar
from time import strftime as date
def create_calendar_page(month=int(date('%Y')), year=int(date('%m'))):
    calendars = calendar.month(month, year)
    return calendars
print(create_calendar_page(month=int(date('%Y')), year=int(date('%m'))))