# 4.Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Storage:
    storage_space = dict()
    count = 0
    with open("storage_data_txt.txt", 'w', encoding='utf-8') as f_obj:
        f_obj.write("-------------Storage data------------" + '\n')

    def __init__(self, max_weight, max_piece):
        self.max_weight = max_weight
        self.max_piece = max_piece

    def delivery_goods(self, type, model, piece, unit):
        with open("storage_data_txt.txt", 'r+', encoding='utf-8') as f_obj:
            row = 0
            for line in f_obj:
                row += 1
                if line.find(type, 0, 15) != -1:
                    if line.find(model, 16, 26) != -1:
                        print(line, end='')
                        f_obj.seek(row*39)
                        f_obj.write(f'\n{type},{model},{piece}\n')
                        break

    def reception_goods(self, data):
        self.count += 1
        with open("storage_data_txt.txt", 'a+', encoding='utf-8') as f_obj:
            f_obj.write(data)


class OfficeEquipment:
    def __init__(self, piece, type, model):
        self.piece = piece
        self.type = type
        # self.weight = weight
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, print_technology, piece, type, model, weight):
        super().__init__(piece, type, model, weight)
        self.print_technology = print_technology


class Scanner(OfficeEquipment):
    def __init__(self, scan_resolution, piece, type, model, weight):
        super().__init__(piece, type, model, weight)
        self.scan_resolution = scan_resolution


class Xerox(OfficeEquipment):
    def __init__(self, type, model, copy_speed, piece):
        super().__init__(piece, type, model)
        self.copy_speed = copy_speed

    @property
    def create_xerox(self):
        return f'{self.type},{self.model},{self.copy_speed},{self.piece}\n'


s = Storage(120, 60)

s.reception_goods(Xerox('cannon         ', 'x200      ', '1200      ', 3).create_xerox)
s.reception_goods(Xerox('cannon         ', 'x100      ', '1200      ', 3).create_xerox)
s.delivery_goods("cannon", 'x200', 2, 'office')
# решил прекратить разработку кода с записью в файл, слишком сложно и громоздко реализовать стандартными методами
