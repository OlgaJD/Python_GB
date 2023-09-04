"""
✔ Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ['Margo', 'Robin', 'Tom']
salary = [150, 25, 444]
bonus = ['10.25%', '35%', '51%']


def payments(names_, salary_, bonus_):
    return {names[i]: salary[i] * float(bonus[i][:-1]) / 100 for i in range(len(names))}


print(payments(names, salary, bonus))

## Задача уже была решена. https://github.com/OlgaJD/Python_GB/blob/main/lesson_4/salary_calc.py