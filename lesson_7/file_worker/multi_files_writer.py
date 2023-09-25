# ✔Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔При достижении конца более короткого файла, возвращайтесь в его начало.

def multi_writer(file_1, file_2, res_file='../result.txt'):
    name, number = None, None
    with (
        open(file_1, 'r', encoding='utf-8') as f1,
        open(file_2, 'r', encoding='utf-8') as f2
    ):
        number = f1.readlines()
        name = f2.readlines()
        number = list(map(lambda x: int(x.strip().split(' | ')[0]) * float(x.strip().split(' | ')[1]), number))
        name = list(map(lambda x: x.strip(), name))
        list_to_write = list(zip(name, number))
        with open(res_file, 'a', encoding='utf-8') as f3:
            for st in list_to_write:
                if st[1] > 0:
                    f3.write(f'{st[0].upper()} -> {round(st[1])} \n')
                else:
                    f3.write(f'{st[0].upper()} -> {abs(st[1])} \n')


if __name__ == '__main__':
    multi_writer('../task_1.txt', '../task_2.txt')
