"""✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*(fib_generator(int(input('Введите число - количество элементов для создания генератора: ')))))
