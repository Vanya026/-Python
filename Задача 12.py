import random
words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Это слово означает проектирование или процесс разработки проекта", "Это слово означает сущность в цифровом пространстве, имеющая поля и методы"]
randomdesc = random.randint(0, len(desc_) - 1)
err_Score = 0
word_Choise = list(words[randomdesc])
symbol = '*'
word_Type = []
chanses = 3
print(desc_[randomdesc])
while err_Score <= chanses:
    score = 0
    for i in word_Choise:
        marker = 0
        for j in word_Type:
            if i == j:
                score += 1
                marker += 1
                print(j, end = " ")
        if marker == 0:
            print(symbol, end = " ")
    t = input("\n\nВведите букву:")
    print("\n\n")
    timer = 0
    for i in word_Choise:
        timer += 1
        if t == i:
            tmp = 0
            for j in word_Type:
                if t == j:
                    tmp += 1
            if tmp == 0:
                word_Type.append(t)
            else:
                err_Score += 1
        elif not t == i and timer == len(word_Choise):
            err_Score += 1
    if err_Score > 0:
        if err_Score == chanses:
            print("Игра закончена")
            break
    elif score == len(word_Choise) - 1:
        print(word_Choise, "\n\nПобеда!")
        break
    else:
        continue

