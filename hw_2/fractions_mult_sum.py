"""Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей.
Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction


def greatest_divisor(a, b):
    common_divisor = ''
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if (a % i == 0) and (b % i == 0):
            common_divisor = i
    return common_divisor


frac_1 = input('Введите первую дробь: ')
frac_2 = input('Введите вторую дробь: ')

numerator_1, denominator_1 = map(int, frac_1.split('/'))
numerator_2, denominator_2 = map(int, frac_2.split('/'))

mult_frac = [(numerator_1 * numerator_2), (denominator_1 * denominator_2)]
sum_frac = [(numerator_1 * denominator_2 + numerator_2 * denominator_1), (denominator_1 * denominator_2)]

m_dev = greatest_divisor(mult_frac[0], mult_frac[1])
s_dev = greatest_divisor(sum_frac[0], sum_frac[1])

print(f'{mult_frac[0] // m_dev}/{mult_frac[1] // m_dev}')
print(f'{sum_frac[0] // s_dev}/{sum_frac[1] // s_dev}')

f1 = Fraction(f'{numerator_1}/{denominator_1}')
f2 = Fraction(f'{numerator_2}/{denominator_2}')
print(f1 + f2, f1 * f2)

print(f1)
