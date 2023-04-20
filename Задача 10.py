m = int(input('enter number:'))
n = int(input('enter number:'))
match n:
    case 1:
        print(n, 'kg')
    case 2:
        print(n / 1000000, 'kg')
    case 3:
        print(n / 1000, 'kg')
    case 4:
        print(n * 1000, 'kg')
    case 5:
        print(n * 100, 'kg')