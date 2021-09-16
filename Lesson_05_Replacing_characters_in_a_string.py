# ДЗ 10. Замена символов в строке
# Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
# Понадобятся: срезы и функции replace(), rfind(), find().

line = input('Please enter a line with \'H\' and \'h\': ')
h = 'h'
x = line.replace('h', 'H')
y = x.replace('H', 'h', 1)
h2 = y.rfind('H')
i = (y[0:h2] + h + y[h2+1:])
print(line, i, sep='\n')  # sep for comparison with original text
