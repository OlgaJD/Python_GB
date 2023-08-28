"""
Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""
nums = [5, 9, 3, 1, 8, 55, 22, 1, 0, 11, 4, 50]
ind_1 = 3
ind_2 = 7


def sum_in_range(num_list, start, stop):
    start_stop = sorted([start, stop])
    return sum(num_list[start_stop[0]:start_stop[1]])


print(sum_in_range(nums, ind_1, ind_2))
