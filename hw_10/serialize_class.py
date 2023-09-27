"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.
"""
import os
import csv
import json
import pickle


class SerializeData:

    def __init__(self, data):
        self.data = data

    def json_save(self, json_file='data.json'):
        with open(json_file, 'w', encoding='utf-8') as jswr:
            json.dump(self.data, jswr, indent=4, ensure_ascii=False)

    def csv_save(self, csv_file='data.csv'):
        with open(csv_file, 'w', encoding='utf-8') as csvwr:
            csv_writer = csv.writer(csvwr, dialect='excel', delimiter=' ', quoting=csv.QUOTE_ALL)
            csv_writer.writerow(('Name of file/directory', 'Parent directory', 'Type', 'Size'))
            for key, value in self.data.items():
                csv_writer.writerow([key, *value])

    def picle_save(self, pickle_file='data.picle'):
        with open(pickle_file, 'wb') as pickwr:
            pickle.dump(self.data, pickwr)


class GetData:

    def __init__(self, path: str = os.getcwd()):
        self.path = path

    def get_size(self):  # функция для определения размера каталога
        size = 0
        for root, dirs, files in os.walk(self.path):
            for file in files:
                size += os.path.getsize(os.path.join(root, file))
        return size

    def directory_walk(self):
        content = {}
        for root, dirs, files in os.walk(self.path):
            # Обходим папки
            for dir_ in dirs:
                parent_dir = ((os.path.join(root)).strip().split('\\')[-1])
                size = self.get_size()
                # size = get_size(os.path.join(root, dir_))
                content[dir_] = [parent_dir, 'Directory', size]
            # Обходим файлы
            for file in files:
                size = os.path.getsize(os.path.join(root, file))
                parent_dir = root.strip().split('\\')[-1]
                content[file] = [parent_dir, 'File', size]
        return content


if __name__ == '__main__':
    data_getter = GetData()
    some_data = data_getter.directory_walk()

    processor = SerializeData(some_data)
    processor.json_save()
    processor.csv_save()
    processor.picle_save()