# задача №1 Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

first_name = input('enter your first name: ')
last_name = input('enter your last name: ')
age = int(input('enter your age: '))
profession = input('enter your profession: ')
experience = int(input('enter the number of years of experience in this profession:'))
print(first_name, last_name, ',', 'age ', age, 'years, ', 'working like', profession, experience, 'years')

a = 26.6  # type float
b = True  # type bool
# print types vars
print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(profession, type(profession))
print(experience, type(experience))
print(a, type(a))
print(b, type(b))
