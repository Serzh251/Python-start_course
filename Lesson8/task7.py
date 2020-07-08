# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, x, sign, y):
        self.x = x
        self.sign = sign
        if sign == '-':
            self.y = -y
        else:
            self.y = y

    def __add__(self, other):
        left_numb = (self.x + other.x)
        right_numb = (self.y + other.y)
        if right_numb < 0:
            self.sign = ''
        else:
            self.sign = '+'
        return f'результат сложения чисел: {left_numb}{self.sign}{right_numb}j'

    def __mul__(self, other):
        left_numb = (self.x * other.x - self.y * other.y)
        right_numb = (self.x * other.y + other.x * self.y)
        if right_numb < 0:
            self.sign = ''
        else:
            self.sign = '+'
        return f'результат умножения чисел: {left_numb}{self.sign}{right_numb}j'


numb1 = ComplexNumber(5, '-', 6)
numb2 = ComplexNumber(7, '+', 8)

print(numb1 + numb2)
print(numb1 * numb2)
