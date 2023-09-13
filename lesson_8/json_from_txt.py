import json
"""
Сформирован текстовый файл с псевдо именами и произведением чисел (lesson 7).
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки
"""


def txt_to_json(file_txt, result_file_json='res_js.json'):
    dict_js = {}
    with open(file_txt, 'r', encoding='utf-8') as fr:
        data = fr.readlines()
        for item in data:
            item = item.strip().split('-> ')
            dict_js[item[0]] = float(item[1])
        print(dict_js)

    with open(result_file_json, 'a', encoding='utf-8') as fp:
        json.dump(dict_js, fp, indent=4, ensure_ascii=False)


txt_to_json('result.txt')



