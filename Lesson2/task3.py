#  Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и через dict.

month = int(input('введите месяц в виде числа от 1 до 12: '))
list_season = ['зима', 'весна', 'лето', 'осень']
dict_season = {"1": 'зима', "2": 'весна', "3": 'лето', "4": 'осень'}
if 1 <= month <= 2 or month == 12:
    print(f"сейчас на дворе {list_season[0]}")
    print(f"сейчас на дворе {dict_season.get('1')}")
elif 3 <= month <= 5:
    print(f"сейчас на дворе {list_season[1]}")
    print(f"сейчас на дворе {dict_season.get('2')}")
elif 6 <= month <= 8:
    print(f"сейчас на дворе {list_season[2]}")
    print(f"сейчас на дворе {dict_season.get('3')}")
else:
    print(f"сейчас на дворе {list_season[3]}")
    print(f"сейчас на дворе {dict_season.get('4')}")

