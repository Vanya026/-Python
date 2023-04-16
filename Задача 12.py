import random
words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это слово означает проектирование или процесс разработки проекта", "Это слово означает сущность в цифровом пространстве, имеющая поля и методы"]
randomdesc = random.randint(0, len(desc_) - 1)
print(desc_[randomdesc])
words = words[randomdesc]
star_answer = []
for i in range(len(words)):
    star_answer.append("*")

print(desc_[randomdesc])
print(* star_answer)
print("Введите букву:")
letter = input()
nxt_plr = False
for i in range(len(star_answer)):
    if letter == words[i]:
        nxt_plr = True
        star_answer[i] = letter
if nxt_plr == True:
    print(* star_answer)
print("Введите букву:")
letter = input()
n = 10
nxt_plr = False
for i in range(len(star_answer)):
    if letter == words[i]:
        nxt_plr = True
        star_answer[i] = letter
if nxt_plr == True:
    print(* star_answer)
else:
    print("Нет такой буквы.")
    print("У вас осталось", n - 1, "попыток!")
