# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    def __init__(self, surname):
        self.surname = surname
        self.age = 29
    def set_age(self, age):
        if age == 29:
            self.age = age
        else:
            print("Недопустимый возраст")
    def get_age(self):
        return self.age
    def get_surname(self):
        return self.surname
    def display_info(self):
        print(f"Имя: {self.surname}\tВозраст: {self.age}")

iv = Person("Иванов")
iv.display_info()
iv.set_age(25)
iv.display_info()
                       

        