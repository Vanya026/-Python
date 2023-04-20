#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.

import time

def with_timer(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        elapsed = time.time() - t
        print(f'Время выполнения: {elapsed}')
    return wrapper

@with_timer
def s_func():
    print('Hello world')

s_func()    