# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.


class Triangle(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        if self.x > 0 and self.y > 0 and self.z > 0:
            print("Числа больше 0!")
            if x + y > z and x + z > y and y + z > x:
                print("Сумма 2х любых чисел больше третьего!")
            else:
                if x + y > z:
                    print("Сумма x и y больше z")
                elif z + y > x:
                    print("Сумма z и y больше x")
                elif x + z > y:
                    print("Сумма x и z больше y")
        else:
            if self.x > 0:
                print("x больше 0")
            elif self.y > 0:
                print("y больше 0")
            elif self.z > 0:
                print("z больше 0")

    def print(self):
        print(self.x, self.y, self.z)

x = 3
y = 7
z = 6

a = Triangle(x, y, z)
a.print()


