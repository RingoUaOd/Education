# ДЗ 18. Задача на словари 1
#
# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,
# сколько раз оно встречалось в этом тексте.
#
# Задачу необходимо решить с использованием словаря.

# №1

dict_text = {}
for word in input('Please enter text: ').split():
    if word in dict_text:
        dict_text[word] = dict_text[word] + 1
    else:
        dict_text[word] = 1
print(dict_text)

# №2

text = "Harry Potter is an ordinary boy who lives in a cupboard under the stairs " \
         "at his Aunt Petunia and Uncle Vernon's house, " \
         "which he thinks is normal for someone like him who's parents have been killed in a 'car crash'."

dict_text = {}
for word in text.split():
    if word in dict_text:
        dict_text[word] = dict_text[word] + 1
    else:
        dict_text[word] = 1
print(dict_text)

