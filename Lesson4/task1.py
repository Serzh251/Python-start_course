# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script, production_hours, rate_per_hours, premium = argv


def salary():
    try:
        return (int(production_hours) * int(rate_per_hours)) + int(premium)
    except ValueError:
        print("Ошибка в воде данных, введите цифровые значения")


if salary() != None:
    print(f"Ваша заработная плата составляет - {salary()} р.")
