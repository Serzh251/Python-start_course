# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
numb_str = 0
data_list = []
str_count = 0
try:
    with open("task1_file.txt", encoding='utf-8') as my_file:
        data_list = my_file.readlines()
    print(f'File include {len(data_list)} lines')

except IOError:
    print("Error input/output!")
for el in data_list:  # enumerate здесь не удалось применить, видимо потому что символы \n добавлены
    str_count += 1
    if el.count(", ") != 0:  # не самый лучший индикатор нового слова, но если так в файле, то норм
        numb_str = el.count(", ")+1
        print(f'В строке {str_count} содержится {numb_str} слов')
    elif len(el) != 0:
        print(f'В строке {str_count} одно слово')
    else:
        print(f'В строке {str_count} нет слов')
