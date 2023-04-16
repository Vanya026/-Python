from math import*
def calculate(a, b, operation):
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/':
        result = a / b
    elif operation == '*':
        result = a * b
    else:
        print('Неизвестная операция')
    return result
def ask_operation():
    message = '''
Пожалуйста, введите символ операции, которую вы хотите совершить и нажмите Enter:
+ : Сложение
- : Вычетание
/ : Деление
* : Умножение
Ваш выбор:'''
    operation = input(message)
    return operation
def run_calculator():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    operation = ask_operation()
    result = calculate(a, b, operation)
    print(f'Результат вычислений: {result}')

