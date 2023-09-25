"""✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os


def path_parse(abs_path):
    tuple_path = (abs_path[0: abs_path.rfind('\\') + 1:],
                  abs_path[abs_path.rfind('\\') + 1: abs_path.rfind('.'):],
                  abs_path[1 + abs_path.rfind('.'):])
    return tuple_path

    # Расшифровки для однострочного решения:
    # file_path = (abs_path[0: abs_path.rfind('\\') + 1:])
    # file_name = abs_path[abs_path.rfind('\\') + 1: abs_path.rfind('.'):]
    # file_extension = abs_path[1 + abs_path.rfind('.'):]
    # tuple_path = (file_path, file_name, file_extension)
    # return tuple_path


def split_path(abs_path: str) -> tuple[str]:
    return os.path.split(abs_path)[0], *os.path.split(abs_path)[-1].split('.')


# print(path_parse(r'C:\Users\Admin\Desktop\Education\GB\Python\lesson5.py'))
print(split_path('C:\Users\Admin\Desktop\Education\GB\Python\lesson5.py'))
