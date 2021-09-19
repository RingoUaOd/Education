# ДЗ 21. Написать функцию arithmetic
#
# Написать функцию arithmetic, принимающую 3 аргумента:
# первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Функция должна вернуть результат вычислений зависящий от третьего аргумент:
# +, сложить их; если -, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        return 'Unknown operation'


x = int(input('Please enter first digit: '))
y = int(input('Please enter second digit: '))
n = input('Please enter arithmetic operator +, -, *, / : ')
m = arithmetic(x, y, n)
print(m)
