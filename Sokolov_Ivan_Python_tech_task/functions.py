def func_for_num(value, data):
    """Выводит 'Привет', если value больше числа 'Number' в файле data.yaml """
    if value > data["Number"]:
        print('Привет')
    else:
        print(f'Для приветствия нужно ввести число больше {data["Number"]}')


def func_for_str(value, data):
    """Выводит 'Привет value', если value соответствует 'Name_match' в файле data.yaml """
    if value == data["Name_match"]:
        print(f"Привет, {value}")
    else:
        print("Нет такого имени")


def func_for_list(value, data):
    """Выводит элементы числового массива кратные 'Divisor' в файле data.yaml"""
    for i in range(len(value)):
        if value[i] % data["Divisor"] == 0:
            print(f"{value[i]} ", end='')
    print()
