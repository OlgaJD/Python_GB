"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

ATTEMPT_LIMIT = 10
target = int(randint(0, 100))
num = None
print(f'Подсказка, ответ: {target}')

for attemp in range(ATTEMPT_LIMIT) :
    num = int(input(f'Попытка № {attemp + 1} из {ATTEMPT_LIMIT}, введите число: '))
    if target > num:
        print('Загаданное число больше вашего')
    elif target < num:
        print('Загаданное число меньше вашего')
    else:
        print(f'Поздравляю, это {num} верный ответ!')
        break
else:
    print(f'Все попытки исчерпаны, было загадано число {target}')
    quit()
