import sys

"""
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""
print('Задание 1')
a = 1
b = 0.5
c = "Hello"
d = True
e = [1, 5, 10, "hi"]

print(type(a))
print(type(b))
print(isinstance(c, str))
print(type(d))
print(type(e))

"""
Задание №2
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""
print('Задание 2')
data = [1, 2.5, "three", True, 100, 0.5, 1]
for i in range(len(data)):
    print(i+1)
    print(data[i])
    print(id(data[i]))
    print(sys.getsizeof(data[i]))
    print(hash(data[i]))
    if isinstance(data[i], int):
        print(isinstance(data[i], int))
    if isinstance(data[i], str):
        print(isinstance(data[i], str))
    print('--------------------------')
