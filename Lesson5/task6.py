# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
content = ''
my_dict = dict()
key_flag_process = False
value_flag_process = False
key = ''
value = ''
sum_value = 0
try:
    with open('task6_text.txt', encoding='utf-8') as file:
        content = file.read()
except IOError:
    print("Error input in file task5_text!")
for el in content:
    if (65 <= ord(el) <= 90) or (97 <= ord(el) <= 122):
        key_flag_process = True
    elif el == ':':
        key_flag_process = False
    elif el == '\n':
        if key == 'Fizra':
            my_dict.update({key: sum_value})
        elif key == 'Math':
            my_dict.update({key: sum_value})
        elif key == 'History':
            my_dict.update({key: sum_value})
        elif key == 'Physics':
            my_dict.update({key: sum_value})
        elif key == 'Informatics':
            my_dict.update({key: sum_value})
        elif key == 'Literature':
            my_dict.update({key: sum_value})
        elif key == 'Russian':
            my_dict.update({key: sum_value})
        key = ''
        sum_value = 0
    if el.isdigit():
        value_flag_process = True
    else:
        value_flag_process = False
    if key_flag_process:
        key += el
    if value_flag_process:
        value += el
    else:
        if el == '(':
            sum_value += int(value)
            value = ''
print(f'Общее количество занятий по предметам - {my_dict}')
