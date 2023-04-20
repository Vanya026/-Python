#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime
def g_date():
    return datetime.now().strftime('%d.%m.%Y %H:%M')

def c_date(func):
    times = 0
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        nonlocal times
        times += 1
        print(f'{func.__name__}, \t{times}, \t{g_date()}')
    return wrapper
@c_date
def some_func():
    pass
@c_date
def func_2():
    pass

some_func()
some_func()
some_func()
func_2()
func_2()
some_func()
some_func()
func_2()
func_2()