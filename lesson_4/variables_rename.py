"""Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
names = 'Name'
ages = [1, 18, 99]
line = 6
s = "SOME"
word = 'WWW'


def rename_s_end():
    temp_dict = {}
    temp_dict.update(globals())
    for key, item in temp_dict.items():
        if not key.startswith('__') and key.endswith('s') and len(key) > 1:
            globals()[key] = None
            globals()[key[:-1]] = item


def print_var(some_dict):
    for key, item in some_dict.items():
        if not key.startswith('__') and not type(item) == type(print_var):
            print(f'{key} = {some_dict[key]}')


print_var(globals())
print()
rename_s_end()
print_var(globals())
