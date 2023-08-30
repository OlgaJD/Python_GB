"""✔ Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""
def kwarg_to_arg(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:  # если ключ не хэшируется(объект изменяемый) надо представить его как строку
            value = str(value)
        new_dict[value] = key
    return new_dict


print(kwarg_to_arg(name='Olga', num=1, some_list=['Hello!', 'lesson_4'], some_set=(1, 5, 10, 99)))
