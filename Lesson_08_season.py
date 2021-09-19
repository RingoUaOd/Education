# ДЗ 22. Написать функцию season
#
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(m):
    if 3 <= m <= 5:
        return 'Spring'
    elif 6 <= m <= 8:
        return 'Summer'
    elif 9 <= m <= 11:
        return 'Autumn'
    elif 1 <= m <= 2 or m == 12:
        return 'Winter'
    else:
        return 'Wrong number'


month = int(input('Please enter month number: '))
month = season(month)
print(month)
