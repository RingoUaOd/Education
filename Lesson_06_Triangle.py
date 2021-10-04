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


cols = int(input('Please enter cols: '))
rows = cols * 2 - 1

for i in range(cols):
    print(i, end='\t')
    for j in range(rows):
        if i == cols - 1 or i == j - cols + 1 or j == cols - i - 1:
            print(' *', end='')
        else:
            print('  ', end='')
    print()

