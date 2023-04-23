# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(n):
    if n <= 1:
        return n
    else:
        return n + sumn(n - 1)
num = int("3")
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", sumn(num))        