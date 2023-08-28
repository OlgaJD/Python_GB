"""
Пользователь вводит данные.
Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
✔Целое положительное число
✔Вещественное положительное или отрицательное число
✔Строку в верхнем регистре, если в строке есть хотя бы одна заглавная буква
✔Строку в нижнем регистре в остальных случаях
"""

text = input('Введите текст: ')

if text.isdigit():
    result = f'Вы ввели целое число {text}'
elif (text.startswith('-') and text.replace('-', '', 1).replace('.', '', 1).isdigit()) or \
        (text.replace('.', '', 1).isdigit()):
    result = f'Вы ввели вещественное число {float(text)}'
elif len([i for i in text if i.isupper()]) > 0:
    result = f'В тексте есть одна или более заглавных букв {text.upper()}'
else:
    result = f'В тексте нет заглавных букв {text}'

print(result)
