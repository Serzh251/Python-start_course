# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationery):
    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        print(f'{self.title} чертит')


class Handle(Stationery):
    def __init__(self, title):
        Stationery.title = title

    def draw(self):
        print(f'{self.title} рисует')


s = Stationery('test')
pen = Pen('Pen')
pencil = Pencil('Pencil')
h = Handle('Handle')

s.draw()
pen.draw()
pencil.draw()
h.draw()
