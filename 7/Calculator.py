import math

class Calculator:
    @classmethod
    def sum(cls, self):
        def sum1(x, y):
            res = x + y
            return res

        a = float(input('Введите число a: '))
        b = float(input('Введите число b: '))
        c = sum1(a, b)
        print("Ответ:")
        print(c)

    @classmethod
    def sub(cls, self):
        def sub1(x, y):
            res = x - y
            return res

        a = float(input('Введите число a: '))
        b = float(input('Введите число b: '))
        c = sub1(a, b)
        print("Ответ:")
        print(c)

    @classmethod
    def div(cls, self):
        def div1(x, y):
            res = x / y
            return res

        a = float(input('Введите число a: '))
        b = float(input('Введите число b: '))
        c = div1(a, b)
        print("Ответ:")
        print(c)

    @classmethod
    def mul(cls, self):
        def mul1(x, y):
            res = x * y
            return res

        a = float(input('Введите число a: '))
        b = float(input('Введите число b: '))
        c = mul1(a, b)
        print("Ответ:")
        print(c)

    @classmethod
    def exp(cls, self):
        def exp1(x, y):
            res = math.pow(x, y)
            return res

        a = float(input('Введите число a: '))
        b = float(input('Введите число b: '))
        c = exp1(a, b)
        print("Ответ:")
        print(c)

    @classmethod
    def mod(cls, self):
        def mod1(x):
            res = abs(x)
            return res

        a = float(input('Введите число a: '))
        c = mod1(a)
        print("Ответ:")
        print(c)

    @classmethod
    def fact(cls, self):
        def fact1(x):
            res = math.factorial(x)
            return res

        a = int(input('Введите натуральное число a: '))
        ans = fact1(a)
        print("Ответ:")
        print(ans)

    @classmethod
    def arccos(cls, self):
        def arccos1(x):
            res = math.acos(a)
            return res

        a = float(input('Введите число a в промежутке [-1;1]: '))
        c = arccos1(a)
        print("Ответ:")
        print(c)
