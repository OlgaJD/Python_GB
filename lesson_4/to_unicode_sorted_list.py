"""
Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
"""
# Вариант 1
def uni_sort(text):
    sorted_list = sorted(set(map(ord, text)), reverse=True)
    return sorted_list


# Вариант 2
def uni_sort_2():
    some_text = input('Input your text: ')
    some_text = [ord(i) for i in set(some_text)]
    return sorted(some_text, reverse=True)


print(uni_sort('some text'))
print(uni_sort_2())
