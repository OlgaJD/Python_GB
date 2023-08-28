"""
✔Создайте вручную список с повторяющимися элементами.
✔Удалите из него все элементы, которые встречаются дважды.
"""
import random

some_list = [random.randint(0, 10) for _ in range(5)]
print(*some_list)
my_set = set(some_list)
print(*my_set)
for i in my_set:
    if some_list.count(i) == 2:
        some_list.remove(i)
        some_list.remove(i)
print(some_list)
