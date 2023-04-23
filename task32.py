#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:

def transcript(x):
    l = list(x)
    for i in range(len(x)):
        if(l[i]=='G'):
            l[i]='C'
        elif(l[i]=='C'):
            l[i]='G'
        elif(l[i]=='T'):
            l[i]='A'
        elif(l[i]=='A'):
            l[i]='T'
        else:
            print('Invalid Input')
    print("Translated DNA:", end="")
    for char in l:
        print(char, end="")

x = 'GGCTAA'
transcript(x)

                        



