# ДЗ 14. Треугольник 2
# При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
# Пользователь вводит, с клавиатуры, высоту фигуры в символах.
#
#   B         *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *

cols = int(input('Please enter altitude for a triangle: '))
for i in range(cols):
    for j in range(cols - i - 1):
        print(end='  ')
    for _ in range(2 * i + 1):
        print('* ', end='')
    print()


