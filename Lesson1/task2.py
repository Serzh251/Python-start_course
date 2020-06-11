# Задача 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time = int(input('enter time in seconds: '))

hours = time // 3600
time = time % 3600
minutes = time // 60
seconds = time % 60

# old formatting strings
print("%02d" % hours, ':', "%02d" % minutes, ':', "%02d" % seconds)

# f formatting strings
# print('{: %H:%M:%S}'.format(hours, minutes, seconds)) - не смог разобраться как вывести время в новом формате f строк
