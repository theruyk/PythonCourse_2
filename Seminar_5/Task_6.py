# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:
file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

def get_file_info(file_path):
    tuple_1 = tuple(file_path.split('/'))
    joined_string = '/'.join(tuple_1[:-1]) +'/' if '/' in file_path else ''

    last_el = tuple_1[-1].rsplit('.', 1)
    name = last_el[0]
    format_of_file ='.' + last_el[1] if len(last_el) > 1 else ""
    new_tuple = (joined_string,name,format_of_file,)

    return new_tuple

#print(get_file_info(file_path))
#print(get_file_info(file_path = 'file_in_current_directory.txt'))
print(get_file_info(file_path = '/home/user/data/file'))