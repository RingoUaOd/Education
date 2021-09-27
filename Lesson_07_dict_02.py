# ДЗ 19. Задача на словари 2
#
# Дан текст состоящий из нескольких строк. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите последнее.
#
# Задачу необходимо решить с использованием словаря.

# №1

dict_text = {}
max_value = 0
max_key = 0
for word in input('Please enter text: ').split():
    if word in dict_text:
        dict_text[word] = dict_text[word] + 1
    else:
        dict_text[word] = 1
for key, value in dict_text.items():
    if max_value is None or value == max_value or value > max_value:
        max_value = value
        max_key = key

print(max_key)

# №2

text = "Harry Potter is an ordinary boy who lives in a cupboard under the stairs " \
       "at his Aunt Petunia and Uncle Vernon's house, " \
       "which he thinks is normal for someone like him who's parents have been killed in a 'car crash'."

dict_text = {}
max_value = 0
max_key = 0
for word in text.split():
    if word in dict_text:
        dict_text[word] = dict_text[word] + 1
    else:
        dict_text[word] = 1
for key, value in dict_text.items():
    if max_value is None or value == max_value or value > max_value:
        max_value = value
        max_key = key

print(max_key)
