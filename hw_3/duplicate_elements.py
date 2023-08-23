"""✔ Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""

some_list = [1, 3, 25, 1, 0, 8, 50, 50, 5, 1, 5, 20, 5, 5]
result_list = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in result_list:
            result_list.append(i)
print(some_list)
print(result_list)
