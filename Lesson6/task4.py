# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}км/ч')


class TowCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police
        print(f'Автомобиль {name} имеет цвет {color} , скорость {speed} км/ час, '
              f'используется в качестве полицейского авто- {is_police}')


class SportCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police
        print(f'Автомобиль {name} имеет цвет {color} , скорость {speed} км/ час, '
              f'используется в качестве полицейского авто- {is_police}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}км/ч')
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышает лимит на {self.speed - 60}км/ч')


class WorkCar(Car):

    def __init__(self, speed: int, color, name, is_police: bool):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police
        print(f'Автомобиль {name} имеет цвет {color} , скорость {speed} км/ час, '
              f'используется в качестве полицейского авто- {is_police}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}км/ч')
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышает лимит на {self.speed - 40}км/ч')


class PoliceCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police
        print(f'Автомобиль {name} имеет цвет {color} , скорость {speed} км/ час, '
              f'используется в качестве полицейского авто- {is_police}')


t = TowCar(50, "blue", "nissan", False)
s = SportCar(100, "white", "mustang", False)
w = WorkCar(70, "green", "lada", False)
p = PoliceCar(90, "black", "ford", True)

t.show_speed()
s.show_speed()
w.show_speed()
p.show_speed()
