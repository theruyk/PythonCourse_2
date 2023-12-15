from datetime import datetime

class Archive:
    my_list = []  # Классовый атрибут, общий для всех экземпляров

    def __new__(cls, *args):
        instance = super().__new__(cls)
        Archive.my_list.append(args)  # Добавляем аргументы как кортеж в классовый список
        return instance

    def __init__(self, number, text):
        self.number = number
        self.text = text
        self.creation_time = datetime.now()  # Пример добавления времени создания экземпляра

# Создание экземпляров класса Archive
example1 = Archive(2, 'two')
example2 = Archive(4, 'four')

# Вывод содержимого классового списка my_list
print(Archive.my_list)
