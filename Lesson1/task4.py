#  Task4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.
number = abs(int(input('enter number : ')))

while number > 0:
    a = number % 10
    number = number // 10
    if a == 9:
        print(a)
        break
    elif a == 8:
        print(a)
        break
    elif a == 7:
        print(a)
        break
    elif a == 6:
        print(a)
        break
    elif a == 5:
        print(a)
        break
    elif a == 4:
        print(a)
        break
    elif a == 3:
        print(a)
        break
    elif a == 2:
        print(a)
        break
    elif a == 1:
        print(a)
        break
    else:
        print(a)
