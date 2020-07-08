# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def numb_unpack(cls, data):
        data_list = data.split("-")
        for i in range(len(data_list)):
            data_list[i] = int(data_list[i])
        return cls(data_list)

    @staticmethod
    def numb_validate(self):
        if 0 < self.data_str[0] <= 31 and 0 < self.data_str[1] <= 12 and 1900 < self.data_str[2] <= 2100:
            return f'дата - {self.data_str[0]}.{self.data_str[1]}.{self.data_str[2]}'
        else:
            return f'формат ввода даты неверен, число должно быть от 1 до 31, месяц от 1 до 12, год от 1990 до 2100!'


d = Data.numb_unpack('03-07-2020')

print(d.numb_validate(d))

