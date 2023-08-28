"""
✔Пользователь вводит строку текста.
✔Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
✔Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
✔Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""
text = input('Введите текст: ')
# вариант 1 без count
my_dict_1 = {}
for i in text:
    if i in my_dict_1:
        my_dict_1[i] += 1
    else:
        my_dict_1[i] = 1
print(my_dict_1)

# вариант 2
my_dict_2 = {}
for i in text:
    if i not in my_dict_2:
        my_dict_2[i] = text.count(i)
print(my_dict_2)

# вариант 3
my_dict_3 = {}
for i in set(text):
    my_dict_3[i] = text.count(i)
print(my_dict_3)
