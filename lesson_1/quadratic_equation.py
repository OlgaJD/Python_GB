"""
Решите квадратное уравнение 5x2-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2.
"""

a, b, c = 5, -10, -400
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / 2 / a
    x2 = (-b - discriminant ** 0.5) / 2 / a
    print(x1, x2)
elif discriminant == 0:
    x = -b / 2 / a
    print(x)
else:
    print('Вещественных корней нет')