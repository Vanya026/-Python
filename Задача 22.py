def code(string, n):
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
    st = []
    for symbol in string:
        i = 0
        for a_str in a:
            if symbol == a_str:
                i += n
                if i > 22:
                    i -= 23
                elif i > 45:
                    i -= 23
                st.append(a[i])
                break
            else:
                i += 1
        if i == 46:
            st.append(symbol)
    return st

n = int(input('Сдвиг:'))
string_txt = input('Строка:')
for i in code(string_txt, n):
    print(end = i)