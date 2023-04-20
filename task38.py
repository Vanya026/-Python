#todo Задача 1. Транспонирование матрицы, transpose(matrix)
Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

lst = [number for number in range(11) for i_num in range(1, number + 1)]
print(lst)

#todo Задача 2. Транспонирование матрицы, transpose(matrix)
Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
Пример:
>>> transpose([[1, 2, 3], [4, 5, 6]])

[[1, 4], [2, 5], [3, 6]]


||1 2 3||      ||1 4||
||4 5 6||  =>  ||2 5||
               ||3 6||

def transponse(matrix):
    matrix_len = len(matrix[0])
    mid_list = [number for i_list in matrix for number in i_list]
    return [[mid_list[idx], mid_list[(idx + matrix_i_len) % len(mid_list)]] for idx in range(len(mid_list) // 2)]

matrix = [
        [1, 2, 3],
        [4, 5, 6]
]
print(transponse(matrix))

#todo Задача 3. Найти сумму элементов матрицы
Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
Задачу решить с помощью генераторов.

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> msum(matrix)

def msum(matrix):
        return sum([number for i_list in matrix for number in i_list])
print(msum(matrix))
