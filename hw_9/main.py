"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""
import json
import math
import os
from typing import Callable
from functools import wraps
from random import randint
import csv


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def csv_reader(func: Callable):
    def wrapper(file: str = 'numbers.csv'):
        result = []
        with open(file, 'r') as csv_r:
            data = csv.reader(csv_r)
            for i in data:
                a, b, c = map(float, i)
                result.append(func(a, b, c))
            return result

    return wrapper


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv(file: str = 'numbers.csv'):
    with open(file, 'w', newline='') as csv_wr:
        writer = csv.writer(csv_wr)
        for _ in range(randint(100, 1001)):
            writer.writerow([randint(1, 101) for _ in range(3)])


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def json_save(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # atr = ','.join(list(map(str, args))) + '|' + ','.join(list(map(str, kwargs.items())))   # Тоже самое что и 46стр, без подписей 'args, kwargs' в файле
        atr = 'args: ' + ','.join(list(map(str, args))) + ' | kwargs: ' + ','.join(list(map(str, kwargs.items())))
        if not os.path.exists('result.json'):
            with open('result.json', 'w', encoding='utf-8') as js_wr:
                json.dump({atr: result}, js_wr, indent=4, ensure_ascii=False)
        else:
            with open('result.json', 'r', encoding='utf-8') as js_r:
                data = json.load(js_r)
            with open('result.json', 'w', encoding='utf-8') as js_w:
                data[atr] = result
                json.dump(data, js_w, indent=4, ensure_ascii=False)

        return result

    return wrapper

# Функция Нахождение корней квадратного уравнения
@csv_reader
@json_save
def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = round((-b + math.sqrt(discriminant)) / (2 * a), 5)
        x2 = round((-b - math.sqrt(discriminant)) / (2 * a), 5)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return round(x, 5)
    else:
        return 'Корней нет'


generate_csv()
quadratic()
