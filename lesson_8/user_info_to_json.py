"""Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json
import os

MIN_LVL = 1
MAX_LVL = 8


def create_json(path: str = 'user.json'):
    user_data = {}
    id_list = []
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                user_data = json.load(file)
        if user_data:
            for users in user_data.values():
                for user in users:
                    id_list.append(user[1])
            # id_list = [user[1] for users in user_data.values() for user in users]
        u_name = input('Введите имя: ')
        if not u_name:
            break
        while True:
            u_id = input('Введите личный идентификатор ID: ')
            if u_id.isdigit():
                if int(u_id) not in id_list:
                    u_id = int(u_id)
                    break
                else:
                    print(f'ID {u_id} Уже занят, введите другой ID')
            else:
                print(f'ID должен быть целым числом')
        while True:
            u_level = input('Введите уровень доступа (от 1 до 7): ')
            if u_level.isdigit() and MIN_LVL < int(u_level) < MAX_LVL:
                break
            else:
                print('Уровень доступа должен быть от 1 до 7')
        if u_level in user_data:
            user_data[u_level].append((u_name, u_id))
        else:
            user_data[u_level] = [(u_name, u_id)]
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(user_data, file, indent=4, ensure_ascii=False)


create_json()
