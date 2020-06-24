# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
temp_packet = ''
my_dict = dict()
list_workers = []
sum_salary = 0
try:
    with open("task3_file.txt", encoding='utf-8') as my_file:
        data_str = my_file.read()
except IOError:
    print("Error input/output!")
for el in data_str:
    temp_packet += el
    if el == ' ':
        value = temp_packet[:-1]
        temp_packet = ''
    elif el == '\n':
        key = temp_packet[:-1]
        my_dict.update({key: value})
        key = ''
        value = ''
        temp_packet = ''
for el in my_dict:
    if float(el) < 20000:
        list_workers.append(my_dict.get(el))
    sum_salary += float(el)

print(f'Сотрудники {list_workers} имеют зарплату ниже 20 000р.')
print(f'Средняя зарплата сотрудников составляет {sum_salary/len(my_dict.keys())}р.')