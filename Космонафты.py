meny = {
    1 : "борщ", 
    2 : "творог", 
    3 : "язык говяжий в желе с оливками", 
    4 : "грибы по-старорусски", 
    5 : "фасоль по-болгарски", 
    6 : "суп из чечевицы", 
    7 : "щи из свежей капусты", 
    8 : "паштет", 
    9 : "тыквенно-сырный суп", 
    10 : "творог с орехами", 
    11 : '''астраханская "щука с вином и черносливом в томатном соусе"''', 
    12 : "макароны с мясом в соусе2"}
r = random.randrange(1, 12)
print("Нужно скушать", meny.get(r))
