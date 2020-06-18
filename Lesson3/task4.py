# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# ------------------------вариант решения №1------------------------------


def pow_function1():
    """функция принимает положительное число х и возводится в отрицательную степень у и возвращает результат"""
    x = abs(int(input("введите действительное положительное число для возведения его в степень:")))
    y = int(input("введите отрицательное число, значение степени:"))
    return 1/x**abs(y) if y < 0 else x**y  # добавил вариант если степень положительная


print(f'результат возведения числа в степень {pow_function1()}')

# ------------------------вариант решения №2------------------------------


def pow_function2():
    """функция принимает положительное число х и возводится в отрицательную степень у и возвращает результат"""
    x = abs(int(input("введите действительное положительное число для возведения его в степень:")))
    y = abs(int(input("введите отрицательное число, значение степени:")))
    for i in range(1, y):
        x *= x
    return 1/x


print(pow_function2())