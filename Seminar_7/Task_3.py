# Напишите функцию, которая открывает на чтение созданные 
# # в прошлых задачах файлы с числами и именами.
# Деремножьте пары чисел. В новый файл сохраните 
# # имя и произведение:
# если результат умножения отрицательный, сохраните имя 
# # записанное строчными буквами и произведение по модулю 
# # если результат умножения положительный, сохраните имя 
# # прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, 
# # сколько в более длинном файле.
# При достижении конца более короткого файла, # возвращайтесь в его начало.
def func(path_numbers: str, path_name: str, path_result: str):
    with open(path_numbers, 'r', encoding='utf-8') as data_numbers, \
         open(path_name, 'r', encoding='utf-8') as data_name, \
         open(path_result, 'w', encoding='utf-8') as data_result:

        # Получаем списки из строк
        list_numbers = data_numbers.readlines()
        list_name = data_name.readlines()

        # Делаем зацикливание файлов
        i = 0
        while i < max(len(list_numbers), len(list_name)):
            num = proc(list_numbers[i % len(list_numbers)])
            name = proc(list_name[i % len(list_name)])

            num_i, num_f = map(float, num.split('|'))
            mult = int(num_i) * num_f
            if mult < 0:
                data_result.write(f'{name.lower()} {-mult}\n')
            else:
                data_result.write(f'{name.upper()} {mult:.0f}\n')
            i += 1


def proc(line: str) -> str:
    return line.strip()


func('text.txt', 'text_name.txt', 'text_result.txt')
