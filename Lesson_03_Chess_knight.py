# ДЗ 4. Шахматный конь
# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
# или наоборот.
# Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
# Понадобится оператор if, and, or, возможно пригодится функция abs(), но не обязательно.


print('11 12 13 14 15 16 17 18\t\t1A 2A 3A 4A 5A 6A 7A 8A')
print('21 22 23 24 25 26 27 28\t\t1B 2B 3B 4B 5B 6B 7B 8B')
print('31 32 33 34 35 36 37 38\t\t1C 2C 3C 4C 5C 6C 7C 8C')
print('41 42 43 44 45 46 47 48\t\t1D 2D 3D 4D 5D 6D 7D 8D')
print('51 52 53 54 55 56 57 58\t\t1E 2E 3E 4E 5E 6E 7E 8E')
print('61 62 63 64 65 66 67 68\t\t1F 2F 3F 4F 5F 6F 7F 8F')
print('71 72 73 74 75 76 77 78\t\t1G 2G 3G 4G 5G 6G 7G 8G')
print('81 82 83 84 85 86 87 88\t\t1H 2H 3H 4H 5H 6H 7H 8H')

cell1 = int(input("Please enter first cell "))
cell2 = int(input("Please enter second cell "))
x1 = cell1 % 10
y1 = cell1 // 10
x2 = cell2 % 10
y2 = cell2 // 10
if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print('The chess knight hit cell ')
else:
    print('The chess knight missed ')
# ord ("string")