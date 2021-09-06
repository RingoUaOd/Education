# ДЗ 6. Математические классы

# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
# Использовать только арифметические операторы. (Подсказка: понадобятся // + и %) Оператор IF использовать нельзя.

# 1 Detailed for each class

first_grade = int(input('Please, enter number of students in the first grade: '))
second_grade = int(input('Please, enter number of students in the second grade: '))
third_grade = int(input('Please, enter number of students in the third grade: '))
desks_for_first_grade = first_grade // 2 + first_grade % 2
desks_for_second_grade = second_grade // 2 + second_grade % 2
desks_for_third_grade = third_grade // 2 + third_grade % 2
sum_of_desks = desks_for_first_grade + desks_for_second_grade + desks_for_third_grade
print('For first grade you need', desks_for_first_grade, 'desks')
print('For second grade you need', desks_for_second_grade, 'desks')
print('For third grade you need', desks_for_third_grade, 'desks')
print('For all grade you need', sum_of_desks, 'desks')

# 2 Simple way, but not correct in relation to each class separately

first_grade = int(input('Please, enter number of students in the first grade: '))
second_grade = int(input('Please, enter number of students in the second grade: '))
third_grade = int(input('Please, enter number of students in the third grade: '))
sum_students = first_grade + second_grade + third_grade
sum_school_desks = sum_students % 2 + sum_students // 2
print('You need', sum_school_desks, 'desks')
