"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV."""
import csv
import json


def json_to_csv(json_path, res_csv_path='res_csv.csv'):
    with (open(json_path, 'r', encoding='utf-8') as jr,
          open(res_csv_path, 'w', encoding='utf-8') as cr):
        js_data: dict[str, list[list[str, int]]] = json.load(jr)
        users_list = []
        for u_level, users in js_data.items():
            for user in users:
                users_list.append((user[0], user[1], u_level))
        csv_writer = csv.writer(cr, dialect='excel', delimiter=' ', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(('Имя', 'ID', 'Уровень'))
        csv_writer.writerows(users_list)


json_to_csv('user.json', 'user.csv')
