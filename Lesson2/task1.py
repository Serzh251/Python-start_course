# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_int = 23
my_float = 54.72
my_string = "The best"
my_list = [23, 45, 32.67, True, [4, 5], None, "Hello"]
my_set = {45, 65, True, None, 45, 'Hi', 71.56}
my_touple = (23, 45, 32.67, True, [4, 5], None, "Hello")
my_dict = {'key_1': 432, '45': None, 'True': 52.12, '23.56': "Hello"}
my_bool = True
my_complex = complex(2, 9)

result_list = [my_int, my_float, my_string, my_list, my_set, my_touple, my_dict, my_bool, my_complex]

for i in result_list:
    print(f"переменная- '{i}' является типом {type (i)}")
