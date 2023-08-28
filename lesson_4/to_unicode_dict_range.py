"""
Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""
def uni_dict(s):
    pair_num = sorted(list(map(int, s.split())))
    sorted_dict = {chr(i): i for i in range(pair_num[0], pair_num[1] + 1)}
    return sorted_dict


some_str = input('Input your text: ')
print(uni_dict(some_str))
