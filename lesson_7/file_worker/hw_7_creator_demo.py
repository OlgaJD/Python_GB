# Заполняем каталог файлами директорию для дальнейшей сортировки по каталогам
import os
import string
from random import sample, randint


def create(extension, path='for_files_hw7', count_files=15, min_len=6, max_len=20):
    if not os.path.isdir(path):
        os.mkdir(path)
    for i in range(count_files):
        file_name = ''.join(sample(string.ascii_lowercase, randint(min_len, max_len)))
        new_file = open(f'{path}/{file_name}.{extension}', 'x')


def setting(ext_count_of_files, path='for_files_hw7'):
    for pair in ext_count_of_files:
        create(pair[0], path, count_files=pair[1])

