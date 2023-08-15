"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
"""

for j in range(2, 11):
    for i in range(2, 6):
        print(f'{i:^3} X {j:^3} = {j * i:^3}', end='\t\t\t')
    print()
print()

for j in range(2, 11):
    for i in range(6, 10):
        print(f'{i:^3} X {j:^3} = {j * i:^3}', end='\t\t\t')
    print()
