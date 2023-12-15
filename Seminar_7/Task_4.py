# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случано сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_lowercase, digits
from random import randint, choices
import os

print(ascii_lowercase)
print(digits)


def my_funk(
    ext: str = "txt",
    min_name: int = 6,
    max_name: int = 30,
    min_size: int = 256,
    max_size: int = 4096,
    count: int = 42
):
    for _ in range(count):
        my_data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        name_of_file = ''.join(choices(ascii_lowercase + digits, k=randint(min_name, max_name)))
        if os.path.exists(f"{name_of_file}.{ext}"):
            continue
        with open(f"{name_of_file}.{ext}", 'wb') as data:
            data.write(my_data)


def new_func(direct, **kwargs):
    if not os.path.exists(direct):
        os.mkdir(direct)
    os.chdir(direct)
    for ext, count in kwargs.items():
        my_funk(ext, count=count)


new_func(r'/Users/the_ryuk/Desktop/PythonCurse_2', txt=2, bin=3)
