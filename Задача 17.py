b = {0 : "ноль", 1 : "один", 2 : "два", 3 : "три", 4 : "четыре", 5 : "пять", 6 : "шесть", 7 : "семь", 8 : "восемь", 9 : "девять"}
n = input("Введите число:")
while not n.isdigit():
    n = input("Введите число:")
n = list(n)
for i in n:
    tmp = int(i)
    print(b.get(tmp, 0), end = " ")    