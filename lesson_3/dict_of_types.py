"""
✔Создайте вручную кортеж содержащий элементы разных типов.
✔Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.
"""

some_tuple = (2, 5, 5.6, 'Hello', [10, 2], '!!!')
types_dict = {}
for i in some_tuple:
    if type(i) not in types_dict:
        types_dict[type(i)] = [i]
    else:
        types_dict[type(i)].append(i)
print(types_dict)
