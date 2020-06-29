#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
#  красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
#  второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
#  осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
#  и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов,
#  и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep
# -----------------------------------------------1--------------------------------------------

#
# class TrafficLight:
#
#     def running(self, mode):
#         if mode == 'Red':
#             print("\033[31m {}" .format("Red light"))
#         elif mode == 'Yellow':
#             print("\033[33m {}" .format('Yellow light'))
#         # elif mode == 'Green_blink':
#         #     print("\033[6m\033[32m{}".format("Green light")) # не смог реализовать мигающий зеленый. текст не мигает
#         else:
#             print("\033[32m {}" .format('Green light'))
#
#
# count = 0
# a = TrafficLight()
# while count < 10:
#     count += 1
#     a.running('Red')
#     sleep(7)
#     a.running('Yellow')
#     sleep(2)
#     a.running('Green')
#     sleep(5)

# -----------------------------------------------2--------------------------------------------


class TrafficLight:
    __red = "Red light"
    __yellow = "Yellow light"
    __green = "Green light"

    def running(self, mode):
        if mode == 'Red':
            print("\033[31m {}" .format(self.__red))
        elif mode == 'Yellow':
            print("\033[33m {}" .format(self.__yellow))
        else:
            print("\033[32m {}" .format(self.__green))


count = 0
a = TrafficLight()
while count < 10:
    count += 1
    a.running('Red')
    sleep(7)
    a.running('Yellow')
    sleep(2)
    a.running('Green')
    sleep(5)
    a.running('Yellow')
    sleep(2)
