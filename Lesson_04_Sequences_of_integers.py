# ДЗ 7. Последовательности целых чисел

# Программа запрашивает ввод, с клавиатуры, целых чисел, пока не будет введён 0.
# Как только пользователь введёт 0 (ноль),
# программа должна посчитать и вывести на экран следующие результаты (без учёта последнего 0):

# количество введённых чисел
# их сумму
# среднее арифметическое всех введённых чисел
# максимальное и минимальное значение
# количество чётных и не чётных значений

number_of_entered = 0
sum_numbers = 0
even_numbers = 0
odd_numbers = 0
average = 0
number = int(input('Hello, please enter number or 0 if you need finish entering numbers: '))
max_numbers = number
min_numbers = number
while number != 0:
    number_of_entered += 1
    sum_numbers = sum_numbers + number
    average = sum_numbers / number_of_entered
    if number > max_numbers:
        max_numbers = number
    if number < min_numbers:
        min_numbers = number
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    number = int(input('Please enter next number or 0 if you need finish entering numbers: '))
print('Number of entered digits:', number_of_entered,
      'Total sum of digits:', sum_numbers,
      'Average:', average,
      'Maximum value:', max_numbers,
      'Minimum value:', min_numbers,
      'Number of even:', even_numbers,
      'Number of odd:', odd_numbers, sep='\n')
