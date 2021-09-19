# ДЗ 23. Написать функцию is_year_leap
# Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True,
# если год високосный, и False иначе.
# Описание условий посмотрите здесь, раздел: Григорианский календарь.

# №1

def is_year_leap(a):
    if a % 4 != 0:
        return False
    else:
        if a % 100 != 0:
            return True
        else:
            if a % 400 == 0:
                return True
            else:
                return False


year = int(input('Please write AD year: '))
year = is_year_leap(year)
print(year)

# №2

def is_year_leap(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return True
    else:
        return False


year = int(input('Please write AD year: '))
year = is_year_leap(year)
print(year)
