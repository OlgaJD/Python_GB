"""
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
"""

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')

# my_gen = (f'\n' if j == 11 else f' {i:2d} * {j:2d} = {i * j:2d}' for i in range(2, 10) for j in range(2, 12))
# print(*my_gen)

min_num = 2
max_num = 10
column = 4

[[print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='') if j == max_num and k == i + column - 1
  else print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='') if k == i + column - 1
else print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='') for k in range(i, i + column)]
 for i in range(min_num, max_num, column) for j in range(min_num, max_num + 1)]