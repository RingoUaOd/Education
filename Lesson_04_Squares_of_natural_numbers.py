# ДЗ 9. Квадраты натуральных чисел
# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

integer = int(input('Hello, please enter integer digit: '))
x = 1
while x ** 2 <= integer:
    print(x ** 2, end=' ')
    x += 1
