"""
Посчитайте сумму чётных элементов от 1 до n исключая кратные e. Используйте while и if.
"""

e, n = int(input('Введите e: ')), int(input('Введите n: '))
i = 0
summ = 0
while i < n:
    if i % 2 == 0 and i % e != 0:
        summ += i
    i += 1
print(summ)
