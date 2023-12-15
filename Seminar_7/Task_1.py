# Напишите функцию, которая заполняет файл (добавляет в конец)
# # случайными парами чисел. Первое число int,
# # второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции

from random import randint, uniform

NUM_MAX = 1000
NUM_MIN = - 1000


def add_text(count: int, file: str):
    with open(file, 'a', encoding='utf-8') as data:
        for i in range(count):
            data.write(
                F'{randint (NUM_MIN, NUM_MAX)} | {uniform (NUM_MIN, NUM_MAX)} \n')


if __name__ == '__main__':
    add_text(5, 'text.txt')
