# ДЗ 17. Инвертирование словаря.
#
# Дан словарь ключами которого являются английские слова, а значения - списки латинских слов.
# Необходимо развернуть словарь. Другими словами, необходимо,
# на основании заданого словаря, создать новый словарь,
# у которого в качестве ключей будут взяты латинские слова,
# из первого словаря, а значениями будут, соответствующие им, английские слова.
#
# Исходный словарь:
#
# d = {
#    'apple': ['malum', 'pomum', 'popula'],
#    'fruit': ['baca', 'bacca', 'popum'],
#    'punishment': ['malum', 'multa']
# }

text = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

new_dict = {}
for key, values in text.items():
    for new_key in values:
        if new_key not in new_dict:
            new_dict[new_key] = [key]
        else:
            new_dict[new_key].append(key)
print(new_dict)
