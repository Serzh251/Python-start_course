# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    _income = dict()
    name = ''
    surname = ''
    position = ''

    def __init__(self):
        wage = int(input("Введите оклад сотрудника, р.: "))
        bonus = int(input("Введите премию сотрудника, р.: "))
        self._income = ({"wage": wage, "bonus": bonus})


class Position (Worker):

    def get_full_name(self):

        Worker.name = input('Введите имя сотрудника: ')
        Worker.surname = input('Введите фамилию сотрудника: ')
        Worker.position = input('Введите должность сотрудника: ')
        my_dict = ({"Name": Worker.name, "Surname": Worker.surname, "Position": Worker.position})
        print(f"Данные сотрудника {my_dict}")

    def get_total_income(self):
        return sum(self._income.values())


p = Position()
p.get_full_name()
print(f"доход сотрудника {p.get_total_income()} р.")
