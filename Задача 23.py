a = [[1, 5, 3], [2, 44, 1, 4,], [3, 3]]
a.sort(key=len)
print("Сортировка по возрастанию", a)
for l in a:
    l.sort(reverse = True)
print(a)    