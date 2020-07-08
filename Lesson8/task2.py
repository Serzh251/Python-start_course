# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise OwnError("На ноль делить нельзя!")
    else:
        result = a/b
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"результат деления: {round(result, 4)}")