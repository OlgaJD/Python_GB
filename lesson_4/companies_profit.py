"""
Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""
companies = {'first': [555, 40, -99999],
             'second': [1000, 0, 6],
             'third': [-500, 555, 1000]}


def profit(companies_):
    profit_dict = list(map(lambda x: sum(companies_[x]), companies_))
    is_profit = all(list(map(lambda x: x > 0, profit_dict)))
    return is_profit


print(profit(companies))
