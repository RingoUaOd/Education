# ДЗ 3. Високосный год.
# Написать программу определяющую високосный год.
# Пользователь вводит номер года, программа должна ответить високосный это год или нет.

# №1 Gregorian calendar

year = int(input('Please write AD year: '))
if year % 4 != 0:
    print(year, '- is common year ')
else:
    if year % 100 != 0:
        print(year, '- is leap year ')
    else:
        if year % 400 == 0:
            print(year, '- is leap year ')
        else:
            print(year, '- is common year ')


# №2 Julian calendar + Gregorian calendar

year = int(input('Please write AD year: '))
if year >= 1583:
    if year % 4 != 0:
        print(year, '- is common year of the Gregorian Calendar ')
    else:
        if year % 100 != 0:
            print(year, '- is leap year of the Gregorian Calendar ')
        else:
            if year % 400 == 0:
                print(year, '- is leap year of the Gregorian Calendar ')
            else:
                print(year, '- is common year of the Gregorian Calendar ')
else:
    if year % 4 == 0:
        print(year, '- is leap year of the Julian Calendar ')
    else:
        print(year, '- is common year of the Julian Calendar ')



