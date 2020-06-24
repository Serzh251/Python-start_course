# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json
content = ''
my_list = []
firm_list = []
dict_firms = dict()
dict_profit = dict()
average_profit = 0
data_list = []
try:
    with open('task7_text.txt', encoding='utf-8') as file:
        content = file.read()

except IOError:
    print("Error input in file task5_text!")
my_list = content.split('\n')
for el in my_list:
    firm_list = el.split(' ')
    firm_names = firm_list[1] + ' ' + firm_list[0]
    firms_profit = int(firm_list[2]) - int(firm_list[3])
    dict_firms.update({firm_names: firms_profit})
count = 0
summ_profit = 0
for i in dict_firms.values():
    if i > 0:
        count += 1
        summ_profit += i
average_profit = summ_profit/count
dict_profit.update({"average_profit": average_profit})
data_list.append(dict_firms)
data_list.append(dict_profit)
print(data_list)
with open("task7.json", "w", encoding='utf-8') as write_f:
    json.dump(data_list, write_f, ensure_ascii=False, indent=4)
