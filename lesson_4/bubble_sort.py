"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
"""
def bubble_sort(some_list):
    for i in range(len(some_list)):
        for j in range(0, len(some_list) - i - 1):
            if some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]


numbers = [5, 55, 8, 6, 1, 0, 7, 15, 9]
bubble_sort(numbers)
print(numbers)
