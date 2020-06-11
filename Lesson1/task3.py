# task3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('enter number: '))
# first decision
print(number + int((str(number) + str(number))) + int((str(number) + str(number) + str(number))))

# second decision
if number <= 9:
    print(number + (number * 10 + number) + (number * 100 + number * 10 + number))
elif 10 <= number <= 99:
    print(number + (number * 100 + number) + (number * 10000 + number * 100 + number))
# ....
