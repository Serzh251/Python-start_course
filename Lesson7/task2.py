# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_tissue(self):
        pass


class Coat(Clothes):
    # property = ''
    def __init__(self, v):
        self.v = v
        # self.size = size

    def calculate_tissue(self):
        return round(self.v/6.5 + 0.5, 2)

    # @property
    # def size(self):
    #     return self.property
    #
    # @size.setter
    # def size(self, size):
    #     if size < 42:
    #         self.property = 'young'
    #     else:
    #         self.property = 'adult'
    #
    # def property_coat(self):
    #     return f'{self.property}'


class Suit (Clothes):
    def __init__(self, h):
        self.h = h

    def calculate_tissue(self):
        return round(self.h * 2 + 0.3, 2)


s = Suit(2)
c = Coat(1.5)
print(f'расход ткани для пальто- {s.calculate_tissue()} м.')
print(f'расход ткани для костюма- {c.calculate_tissue()} м.')
print(f'общий расход ткани- {round(s.calculate_tissue() + c.calculate_tissue(), 2)} м.')
# print(c.property)
