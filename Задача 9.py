year = int(input('enter number:'))
if year % 100 > 0:
    print(year // 100 + 1)
else:
    print(year // 100)
    
