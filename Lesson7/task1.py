# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, my_m):
        self.my_m = my_m

    def __str__(self):
        for row in self.my_m:
            for item in row:
                print(item, "", end="")
            print()
        return ' '

    def __abs__(self, other):
        result = list()
        count = 0
        for row in self.my_m:
            result.append([])
            for item in range(len(row)):
                result[count].append(self.my_m[count][item] + self.other[count][item])
            count += 1
        return f'{result}'

# вне ООП данный метод работает, не могу понять как прикрутить это в __add__
# my_list = [[1, 42], [3, 4], [5, 6]]
# all = [[1, 42], [3, 4], [5, 6]]
# result = list()
# count = 0
# for row in my_list:
#     result.append([])
#     for item in range(len(row)):
#         result[count].append(my_list[count][item] + all[count][item])
#     count += 1
# print(result)


matrix1 = Matrix([[1, 45], [3, 4], [5, 45]])
matrix2 = Matrix([[1, 2], [3, 4], [5, 88]])
print(matrix1)
print(matrix2)
print(matrix1+matrix2)