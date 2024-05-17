from typing import Union, List
from functions import func_for_num, func_for_str, func_for_list
import yaml


def get_data():
    with open('Sokolov_Ivan_Python_tech_task/data.yaml', 'r') as file:
        return yaml.safe_load(file)


def logic(value: Union[str, int, float, List[Union[int, float]]]):
    """Вызывает функцию в соответствии с определенным типом данных"""
    data = get_data()
    if isinstance(value, int):
        func_for_num(value, data)
    elif isinstance(value, float):
        func_for_num(value, data)
    elif isinstance(value, str):
        func_for_str(value, data)
    elif isinstance(value, list) and all(isinstance(x, (int, float)) for x in value):
        func_for_list(value, data)
    else:
        raise ValueError("Неверный тип данных")


def main():
    """Принимает ввод и определяет тип данных"""
    data = get_data()
    while True:
        user_input = input(
            f"Введите число больше {data['Number']}, имя или числовой массив (например, [1, 2, 3]), или введите 'quit' для выхода: ")
        if user_input.lower() == 'quit':
            break
        try:
            evaluated_input = eval(user_input)
            if isinstance(evaluated_input, list) and all(isinstance(x, (int, float)) for x in evaluated_input):
                logic(evaluated_input)
            elif isinstance(evaluated_input, int) or isinstance(evaluated_input, float):
                logic(evaluated_input)
            else:
                print("Ввод не соответствует ожидаемым типам данных.")
        except (SyntaxError, NameError):
            logic(user_input)
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
