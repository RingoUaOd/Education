# ДЗ 20. Задача на множества 1
# Дан список чисел. Определите, сколько в нем встречается различных (уникальных) чисел.
#
#   - Примечание. Эту задачу на Питоне можно решить в одну строчку.
#
# (Задача решается с применением множеств)

from random import randint

# №1

line = input('Please enter digits: ')
print(set(line))

# №2

line = [randint(1, 10) for _ in range(10)]
print(line)
print(set(line))

# №3

print(set([randint(1, 10) for _ in range(10)]))

