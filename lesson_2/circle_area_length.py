import decimal
from math import pi

"""
Задание №4
✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

"""

decimal.getcontext().prec = 42
diameter = -1
while diameter < 0 or diameter > 1000:
    diameter = decimal.Decimal(input('Введите диаметр не превышающий 1000: '))
print(diameter)

area_circle = decimal.Decimal(pi) * (diameter / 2) ** 2
length_circle = decimal.Decimal(pi) * diameter

print(area_circle, length_circle)
