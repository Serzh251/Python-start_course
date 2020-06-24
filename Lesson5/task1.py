# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
    data_file = open("task1_file.txt", 'w', encoding='utf-8')
    while True:
        my_str = input('введите строку для записи в файл. Или для окончания записи нажмите "enter": ')
        if len(my_str) == 0:
            break
        data_file.write(my_str + '\n')
except IOError:
    print("Ошибка в работе с файлом")
finally:
    data_file.close()
