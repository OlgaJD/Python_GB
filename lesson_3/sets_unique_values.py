"""
✔ Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
"""
#  вариант 1
list_1 = [1, 2, 2, 5, 25, 11, 1, 25]
list_2 = set(list_1)
print(list_2)

#  вариант 2
list_3 = []
for i in list_1:
    if i not in list_3:
        list_3.append(i)
print(list_3)