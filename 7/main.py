import random
import Calculator

while True:

    nachalo = input('Выберите операцию, которую вы хотите произвести: +, -, /, *, ^, random, module, !, arccos: ')

    if nachalo == "+":
        calc = Calculator
        calc.Calculator.sum(nachalo)

    elif nachalo == "-":
        calc = Calculator
        calc.Calculator.sub(nachalo)

    elif nachalo == "/":
        calc = Calculator
        calc.Calculator.div(nachalo)

    elif nachalo == "*":
        calc = Calculator
        calc.Calculator.mul(nachalo)

    elif nachalo == "^":
        calc = Calculator
        calc.Calculator.exp(nachalo)

    elif nachalo == "random":
        c = (random.random())
        print("Ответ:")
        print(c)

    elif nachalo == "module":
        calc = Calculator
        calc.Calculator.mod(nachalo)

    elif nachalo == "!":
        calc = Calculator
        calc.Calculator.fact(nachalo)

    elif nachalo == "arccos":
        calc = Calculator
        calc.Calculator.arccos(nachalo)

    else:
        print("Ошибка. Попробуйте еще раз")
