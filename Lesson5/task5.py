# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randrange
result_number = 0
data_list = []
try:
    with open('task5_text.txt', 'w+', encoding='utf-8') as file:
        for i in range(0, 11):
            file.write(str(randrange(-1000, 1000, 4))+' ')
        file.seek(0)
        content = file.read()
        print(f'Файл содержит числа: {content}')
except IOError:
    print("Error input in file task5_text!")

try:
    with open('task5_text.txt', encoding='utf-8') as file:
        content = file.read()
        data_numbers = content.split(" ")
        for el in data_numbers:
            if el.isdigit():
                result_number += int(el)
    print(f'Сумма чисел в файле равна: {result_number}')
except IOError:
    print("Error output in file task5_text!")
