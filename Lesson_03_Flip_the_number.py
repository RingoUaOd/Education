# ДЗ 5. Перевернуть число
# Дано целое, положительное, ТРЁХЗНАЧНОЕ число. Например: 123, 867, 374. Необходимо его перевернуть.
# Например, если ввели число 123, то должно получиться на выходе ЧИСЛО 321.
# ВАЖНО! Работать только с числами. Строки, оператор IF и циклы использовать НЕЛЬЗЯ!
# На выходе ОБЯЗАТЕЛЬНО должно быть ЧИСЛО!!!

# №1

num = int(input('Please input 3 digit number: '))
num1 = num % 10
num2 = num // 100
num3 = num // 10 % 10
print('Your number - ', num, 'After the flip of the digit - ', num1 * 100 + num3 * 10 + num2)

# №2
num = int(input('Please input 3 digit number: '))
num_reverse = num % 10 * 100 + num // 10 % 10 * 10 + num // 100
print('Your number - ', num, 'After the flip of the digit - ', num_reverse)



