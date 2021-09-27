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

height = int(input('Please enter altitude for a triangle: '))
for y in range(height):
    for x in range(height - y - 1):
        print(end='  ')
    for j in range(2 * y + 1):
        print('* ', end='')
    print()



