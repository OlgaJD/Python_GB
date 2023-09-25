# ✔Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.
import string
from random import randint, sample

SIZE = (4, 7)
NUM_OF_NAMES = randint(3, 10)
vowels = 'аеiouy'


def write_name_to_file(file_name='../task_2.txt'):
    names = []
    while len(names) < NUM_OF_NAMES:
        res = ''.join(sample(string.ascii_lowercase, randint(4, 7))).title()
        if len(set(res) & set(vowels)) > 0:
            names.append(res)
    with open(file_name, 'a', encoding='utf-8') as f:
        f.writelines('\n'.join(names))


if __name__ == '__main__':
    write_name_to_file()
