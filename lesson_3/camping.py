"""
✔Три друга взяли вещи в поход.
Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔Какие вещи взяли все три друга
✔Какие вещи уникальны, есть только у одного друга
✔Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

friends = {'Коля': ('палатка', 'еда', 'вода', 'мяч'),
           'Игорь': ('палатка', 'топор', 'вода', 'бадминтон'),
           'Миша': ('палатка', 'топор', 'еда', 'водка')}

all_things = set()
for friend in friends.values():
    all_things = all_things.union(set(friend))

all_have = all_things.copy()
for friend in friends.values():
    all_have = all_have.intersection(set(friend))

uniq_dict = {}
for name, things in friends.items():
    all_except_one = all_things.copy()
    for other_name, other_things in friends.items():
        if name != other_name:
            all_except_one = all_except_one.difference(other_things)
    uniq_dict[name] = tuple(all_except_one)

except_dict = {}
for name, things in friends.items():
    all_except_one = all_things.copy()
    for other_name, other_things in friends.items():
        if name != other_name:
            all_except_one = all_except_one.intersection(other_things)
    except_dict[name] = tuple(all_except_one.difference(things))

print(f'Все вещи ребят: {all_things}')
print()
print(f'Вещи которые есть у всех ребят: {all_have}')
print()
print('Вещи, которые есть только у одного из ребят: ')
for name, thing in uniq_dict.items():
    print(f'{name}: {" ".join([i for i in thing])}')
print()
print('Вещи, которые есть у всех, кроме одного из ребят: ')
for name, thing in except_dict.items():
    print(f'{name}: {" ".join([i for i in thing])}')
