"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def to_hex_system(decimal_num):
    hex_digits = '0123456789ABCDEF'
    hex_num = ''
    sign = ''
    if decimal_num < 0:
        sign = '-'
    decimal_num = abs(decimal_num)
    while decimal_num > 0:
        hex_num = hex_num + hex_digits[decimal_num % 16]
        decimal_num //= 16
    return sign + hex_num[::-1]


example = int(input('Введите целое число в десятичной системе: '))
print(example)
print(to_hex_system(example))
print(hex(example))
