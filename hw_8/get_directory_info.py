"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import csv
import json
import pickle


def get_size(path):  # функция для определения размера каталога
    size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


def directory_walk(path: str = os.getcwd()):
    content = {}
    for root, dirs, files in os.walk(path):
        # Обходим папки
        for dir_ in dirs:
            parent_dir = ((os.path.join(root)).strip().split('\\')[-1])
            size = get_size(os.path.join(root, dir_))
            content[dir_] = [parent_dir, 'Directory', size]
        # Обходим файлы
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            parent_dir = root.strip().split('\\')[-1]
            content[file] = [parent_dir, 'File', size]
    return content


def json_save(data, json_file='data.json'):
    with open(json_file, 'w', encoding='utf-8') as jswr:
        json.dump(data, jswr, indent=4, ensure_ascii=False)


def csv_save(data, csv_file='data.csv'):
    with open(csv_file, 'w', encoding='utf-8') as csvwr:
        csv_writer = csv.writer(csvwr, dialect='excel', delimiter=' ', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(('Name of file/directory', 'Parent directory', 'Type', 'Size'))
        for key, value in data.items():
            csv_writer.writerow([key, *value])


def picle_save(data, pickle_file='data.picle'):
    with open(pickle_file, 'wb') as pickwr:
        pickle.dump(data, pickwr)


def pickle_load(path: str):  # Для проверки
    with open(path, 'rb') as pl:
        file = pickle.load(pl)
    return file


def run(path: str = os.getcwd()):
    data = directory_walk()
    json_save(data)
    csv_save(data)
    picle_save(data)


if __name__ == '__main__':
    run()
