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


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    storage_data = dict()
    delivery_data = dict()
    total_piece = 0
    reseption_flag = True
    delivery_flag = True

    def __init__(self, max_piece):
        self.max_piece = max_piece

    def delivery_goods(self, equipment, piece, unit):
        if self.storage_data.get(equipment) is not None:
            my_list = []
            if piece == int(self.storage_data.get(equipment)[2]):
                my_list.append(self.storage_data.get(equipment)[0])
                my_list.append(self.storage_data.get(equipment)[1])
                my_list.append(piece)
                my_list.append(unit)
                self.delivery_data.update({equipment: my_list})
                self.storage_data.pop(equipment)

            elif piece > int(self.storage_data.get(equipment)[2]):
                print('Запрошенное оборудование в нужном количестве отсутствует на складе!')
                print(f'На данный момент на складе имеется {self.storage_data.get(equipment)[2]} '
                      f'шт. запрашиваемого оборудования')
            else:
                new_piece = int(self.storage_data.get(equipment)[2]) - piece
                my_list.append(self.storage_data.get(equipment)[0])
                my_list.append(self.storage_data.get(equipment)[1])
                my_list.append(piece)
                my_list.append(unit)
                self.delivery_data.update({equipment: my_list})
                self.storage_data.get(equipment)[2] = new_piece

    def reception_goods(self, data):
        my_list = data.split(',')
        if int(my_list[3]) > self.max_piece - self.total_piece:
            print(f'На складе не достаточно свободного места! Доступно {self.max_piece - self.total_piece} мест')
            print(f'Необходимо что то выдать или уменьшить количество! Склад вмещает максимум {self.max_piece} мест')
        else:
            self.storage_data.update({my_list[0]: my_list[1:]})
            self.total_piece += int(my_list[3])


class OfficeEquipment:
    def __init__(self, piece, model):
        self.piece = piece
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, model, print_technology, piece):
        super().__init__(piece, model)
        self.print_technology = print_technology

    @property
    def create_printer(self):
        return f'{self.model},Printer,{self.print_technology},{self.piece}'


class Scanner(OfficeEquipment):
    def __init__(self, model, scan_resolution, piece):
        super().__init__(piece, model)
        self.scan_resolution = scan_resolution

    @property
    def create_scanner(self):
        return f'{self.model},Scanner,{self.scan_resolution},{self.piece}'


class Xerox(OfficeEquipment):
    def __init__(self, model, copy_speed, piece):
        super().__init__(piece, model)
        self.copy_speed = copy_speed

    @property
    def create_xerox(self):
        return f'{self.model},Xerox,{self.copy_speed},{self.piece}'


s = Storage(120)

while s.reseption_flag:
    try:
        inline = input('введите тип оборудования сдаваемого на склад, (Xerox, Scanner или Printer) '
                       'для окончания введите "stop": ')
        if inline == 'stop':
            break
        elif inline == 'Xerox':
            model = input('введите марку и модель оборудования: ')
            copy_speed = input('введите скорость копирования, лист/мин: ')
            piece = int(input('введите количество, шт.: '))
            s.reception_goods(Xerox(model, 'Copy speed- ' + copy_speed + ' лист/мин', piece).create_xerox)
        elif inline == 'Scanner':
            model = input('введите марку и модель оборудования: ')
            scan_resolution = input('введите разрешение копирования, dpi: ')
            piece = int(input('введите количество, шт.: '))
            s.reception_goods(Scanner(model, 'Scan resolution- ' + scan_resolution + 'dpi', piece).create_scanner)
        elif inline == 'Printer':
            model = input('введите марку и модель оборудования: ')
            print_technology = input('введите технологию печати "laser" or "jet": ')
            piece = int(input('введите количество, шт.: '))
            s.reception_goods(Printer(model, 'Print technology- ' + print_technology, piece).create_printer)
        else:
            raise OwnError("Вы ввели не поддерживаемый тип оборудования!")
    except OwnError as ErrTypeEq:
        print(ErrTypeEq)
    if s.total_piece == s.max_piece:
        print(f'склад полон! пора что то забрать!')
        s.reseption_flag = False

while s.delivery_flag:
    print(f'------на данный момент на складе имеется на хранении------')
    for el in s.storage_data.keys():
        print(f'{s.storage_data.get(el)[0]} модели {el}, краткие данные: {s.storage_data.get(el)[1]},  '
              f'в количестве {s.storage_data.get(el)[2]} шт.')
    try:
        if len(s.storage_data) == 0:
            raise OwnError("Склад пуст! Вам нечего оттуда взять.")
        equipment = input('Введите название оборудования, которое вы хотите забрать со склада: ')
        if s.storage_data.get(equipment) is None:
            print('данного оборудования нет на складе!')
            continue
        piece = int(input('Введите требуемое количество оборудования: '))
        unit = input('Введите подразделение компании, куда выдается оборудование: ')
        s.delivery_goods(equipment, piece, unit)
        print(f'{s.delivery_data.get(equipment)[0]} модели {equipment}, краткие данные: '
              f'{s.delivery_data.get(equipment)[1]}, в количестве {s.delivery_data.get(equipment)[2]} шт., '
              f'подразделение компании забравшей товар: {s.delivery_data.get(equipment)[3]}')
    except OwnError as ErrStorage:
        print(ErrStorage)
        s.delivery_flag = False
    except ValueError:
        print('Введите числовое значение количества!')