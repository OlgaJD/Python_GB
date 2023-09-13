"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import json


def csv_to_json(csv_path: str = 'user.csv', json_path: str = 'user.json'):
    with (open(csv_path, 'r', encoding='utf-8') as csv_file,
          open(json_path, 'w', encoding='utf-8') as js_file):
        data = csv_file.readlines()
        user_data = {}
        for i in range(len(data)):
            if i and data[i] != '\n':
                user = data[i].strip().replace('"', '').split()
                user[1] = f'{user[1]:0>10}'
                u_hash = str(hash(user[0] + user[1]))
                user_data[u_hash] = user

        json.dump(user_data, js_file, indent=4, ensure_ascii=False)


csv_to_json()
