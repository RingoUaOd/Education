# ДЗ 8. Найти наибольшую, целую степень двойки

# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

natural_number = int(input('Hello, please enter natural number: '))
power_of_two = 2
x = 1
while power_of_two <= natural_number:
    power_of_two = power_of_two * 2
    x += 1
print(natural_number, '\t',  x - 1, power_of_two // 2, '\t', 2, '**', x - 1, '=', power_of_two // 2)
