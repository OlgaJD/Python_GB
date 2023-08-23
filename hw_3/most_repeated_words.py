""" ✔ В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
"""
import re

COUNT_WORLDS = 10

text = 'Python is an easy to learn, powerful programming language. It has efficient high-level data structures ' \
       'and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic ' \
       'typing, together with its interpreted nature, make it an ideal language for scripting and rapid application ' \
       'development in many areas on most platforms. The Python interpreter and the extensive standard library are ' \
       'freely available in source or binary form for all major platforms from the Python web site, ' \
       'https://www.python.org/, and may be freely distributed. The same site also contains distributions of and ' \
       'pointers to many free third party Python modules, programs and tools, and additional documentation. The ' \
       'Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other ' \
       'languages callable from C). Python is also suitable as an extension language for customizable applications.'

result_str = (re.sub("[^A-Za-z А-Яа-яЁё]", "", text.lower())).split()

dict_words = {}
for word in result_str:
    dict_words[word] = result_str.count(word)

print(f'Всего слов в тексте: {len(result_str)}')
print(f'Из них уникальных: {len(dict_words)}')

print('Самые частые слова:')
counter = 0
sorted_words = sorted(dict_words, key=dict_words.get, reverse=True)
for i in sorted_words:
    if counter < COUNT_WORLDS:
        print(f'{counter + 1}. "{i}" = {dict_words[i]}')
        counter += 1
