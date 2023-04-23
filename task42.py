#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def isPalindrome(s):
    s = str(s)
    return s == s[::-1]

def generate_palindrome(minx,maxx):
    tmpList = []
    for i in range(minx,maxx+1):
        if isPalindrome(i):
            tmpList.append(i)
    return tmpList
generate_palindrome(1,250)