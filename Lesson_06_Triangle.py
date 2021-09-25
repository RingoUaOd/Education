# ДЗ 13. Треугольник 1

# При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
# Пользователь вводит, с клавиатуры, высоту фигуры в символах.

#   A         *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *


height = int(input('Please enter altitude for a triangle: '))
width = height * 2 - 1

for y in range(height):
    for x in range(width):
        if y == height - 1 or x == height - y - 1 or y == x - height + 1:
            print(' *', end='')
        else:
            print('  ', end='')
    print()

print()

