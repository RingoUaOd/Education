# ДЗ 16. Ромб 2
# При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
# Пользователь вводит, с клавиатуры, высоту фигуры в символах.
#
#   D         *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *         *         *
#     *       *       *
#       *     *     *
#         *   *   *
#           * * *
#             *

cols = int(input('Please enter a height for a rhombus odd number: '))
if cols % 2 == 0:
    print('Please try again and use odd number')
    exit()
rows = cols
a = 0
b = 2
c = rows // 2
for i in range(cols):
    if i <= cols//2:
        for j in range(rows):
            if c - a <= j <= c + a:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        a = a + 1
        print()
    else:
        for j in range(rows):
            if j == b - 1 or j == (rows - b) or j == c:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        b = b + 1
        print()
