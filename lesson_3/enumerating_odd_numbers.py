"""
✔Создайте вручную список с повторяющимися целыми числами.
✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
✔Нумерация начинается с единицы.
"""
import random

some_list = [random.randint(0, 10) for _ in range(10)]
print(*some_list)
res = []
for i in range(len(some_list)):
    if some_list[i] % 2 == 1:
        res.append(i+1)
print(res)