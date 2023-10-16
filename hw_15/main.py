"""Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
Также реализуйте возможность запуска из командной строки с передачей параметров.
"""

import logging
from collections import namedtuple
import os
import argparse

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:7} - {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='logger.log', filemode='w', level=logging.NOTSET,
                    encoding='utf-8')


def get_size(path):  # функция для определения размера каталога
    size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


def directory_walk(path: str = os.getcwd()):
    if not os.path.exists(path):
        logger.error(f'Указанного каталога не существует')
    content = []
    for root, dirs, files in os.walk(path):
        # Обходим папки
        Element = namedtuple("Element", ['name', 'extension', 'parent_dir', 'size'])
        for dir_ in dirs:
            parent_dir = ((os.path.join(root)).strip().split('\\')[-1])
            size = get_size(os.path.join(root, dir_))
            content.append(Element(dir_, 'Directory', parent_dir, size))
            logger.info(f'{dir_}, {"Directory", parent_dir, size}')
        # Обходим файлы
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            parent_dir = root.strip().split('\\')[-1]
            if '.' in file:
                name, ext = file.rsplit('.', 1)
            else:
                name, ext = file, 'No file extension'
            content.append(Element(name, ext, parent_dir, size))
            logger.info(f'{name}, {ext, parent_dir, size}')
    return content


def term_parser():
    parser = argparse.ArgumentParser(description='Walker')
    parser.add_argument('files', metavar='Обход каталога', type=str, nargs='*', help='Введите путь каталога')
    args = parser.parse_args()
    return directory_walk(args.files[0])


if __name__ == '__main__':
    data = term_parser()
    print(data)
