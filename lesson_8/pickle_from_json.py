"""Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов."""
import json
import os
import pickle


def json_to_pickle(path: str = os.getcwd()):
    file_list = []
    for files in os.walk(path):
        for file in files[2]:
            if file.endswith('.json'):
                file_list.append(os.path.join(files[0], file))
    for file in file_list:
        with (open(file.rsplit('.', 1)[0] + '.pickle', 'wb') as data,
              open(file, 'r', encoding='utf-8') as json_file):
            users_file = json.load(json_file)
            pickle.dump(users_file, data)


def pickle_load(path: str):
    with open(path, 'rb') as data:
        file = pickle.load(data)
        print(file)
    return file


def picle_save(path: str, obj: object):
    with open(path, 'wb') as data:
        pickle.dump(obj, data)
