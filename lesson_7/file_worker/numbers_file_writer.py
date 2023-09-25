# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
from random import randint, uniform

MIN_SIZE = -1000
MAX_SIZE = 1001


# Вариант 1
def write_numbers_to_file(num_of_str, file_name):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        f.writelines(
            '\n'.join([f'{randint(MIN_SIZE, MAX_SIZE)} | {uniform(MIN_SIZE, MAX_SIZE)}' for i in range(num_of_str)]))


# Вариант 2
def number_writer(file, coun_l):
    with open(file, 'w', encoding='utf-8') as f:
        for i in range(coun_l):
            int_num = randint(-1000, 1001)
            float_num = uniform(-1000, 1001)
            f.write(f'{int_num:>10} | {float_num} \n')


if __name__ == '__main__':
    write_numbers_to_file(12, '../task_1')
    # number_writer('../task_1_1.txt', 5)
