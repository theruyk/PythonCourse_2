# Урок 11. ООП. Особенности Python
# Задача 1
# from datetime import datetime
import math
# class MyStr(str):
#     def __new__(cls, value, author):
#         # Создаем экземпляр класса MyStr, передавая value в качестве строкового значения
#         instance = super(MyStr, cls).__new__(cls, value)
#         # Установка дополнительных атрибутов
#         instance.value = value
#         instance.author = author
#         instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
#         return instance

#     def __str__(self):
#         # Формирование строкового представления события
#         return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"

#     def __repr__(self):
#         # Формирование строки, которая может быть использована для повторного создания этого объекта
#         return f"MyStr('{self.value}', '{self.author}')"

# # Пример использования
# event = MyStr("Завершилось тестирование", "John")
# print(event)

# my_string = MyStr("Пример текста", "Иван")
# print(my_string)

# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))


# Задача 2

class InvalidTextError(Exception):
    """Исключение выбрасывается, когда предоставленный текст не является строкой или пустой."""
    pass

class InvalidNumberError(Exception):
    """Исключение выбрасывается, когда предоставленное число не является положительным целым числом или числом с плавающей запятой ."""

class Archive:
    _instance = None  # Статическая переменная для хранения единственного экземпляра класса
    archive_text = []  # Статический список для хранения текстовых записей
    archive_number = []  # Статический список для хранения числовых записей

    def __new__(cls, text, number):
            if not isinstance(text, str) or not text:
                raise InvalidTextError("Текст должен быть непустой строкой")
            if not isinstance(number, (int,float)):
                raise InvalidNumberError("Число не является целым числом или числом с плавающей запятой ")
            if number < 0:
                raise InvalidNumberError("Число должно быть положительным")
            if cls._instance is None:
                cls._instance = super(Archive, cls).__new__(cls)
            cls.archive_text.append(text)
            cls.archive_number.append(number)
            return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self):
        return (f"Text is {self.text} and number is {self.number}. "
                f"Also {self.archive_text} and {self.archive_number}")

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"

# Пример использования
try:
    archive1 = Archive("Запись 1", 42)
    print(archive1)  # Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]

    archive2 = Archive("Запись 2", 3.14)
    print(archive2)  # Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]
except InvalidTextError as e:
    print(f"Ошибка: {e}")




# Задача 3

# class Rectangle:
#     def __init__(self, width, height=None):
#         self.width = width
#         self.height = height if height is not None else width

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def area(self):
#         return self.width * self.height

#     def __add__(self, other):
#         new_width = self.width + other.width
#         new_height = self.height + other.height
#         return Rectangle(new_width, new_height)

#     def __sub__(self, other):
#         new_width = max(self.width - other.width, 0)
#         new_height = max(self.height - other.height, 0)
#         return Rectangle(new_width, new_height)

#     def __lt__(self, other):
#         return self.area() < other.area()

#     def __eq__(self, other):
#         return self.area() == other.area()

#     def __le__(self, other):
#         return self.area() <= other.area()

#     def __str__(self):
#         return f"Прямоугольник со сторонами {self.width} и {self.height}"

#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"

# # Пример использования
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)

# print(f"Периметр rect1: {rect1.perimeter()}")  # Периметр rect1: 30
# print(f"Площадь rect2: {rect2.area()}")        # Площадь rect2: 21
# print(f"rect1 < rect2: {rect1 < rect2}")       # rect1 < rect2: False
# print(f"rect1 == rect2: {rect1 == rect2}")     # rect1 == rect2: False
# print(f"rect1 <= rect2: {rect1 <= rect2}")     # rect1 <= rect2: False

# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")  # Периметр rect3: 50
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")          # Ширина rect4: 2

# # # Часть Урока 13. Исключения 

# class NegativeValueError(Exception):
#     """Исключение, выбрасываемое при попытке задать отрицательное значение ширине или высоте прямоугольника."""
#     pass

# class Rectangle:
#     def __init__(self, width: float, height: float = None):
#         self.width = width
#         self.height = height if height is not None else width

#     @property
#     def width(self) -> float:
#         return self._width

#     @width.setter
#     def width(self, value: float) -> None:
#         if value < 0:
#             raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
#         self._width = value

#     @property
#     def height(self) -> float:
#         return self._height

#     @height.setter
#     def height(self, value: float) -> None:
#         if value < 0:
#             raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
#         self._height = value

#     def perimeter(self) -> float:
#         return 2 * (self.width + self.height)

#     def area(self) -> float:
#         return self.width * self.height

#     def __add__(self, other: 'Rectangle') -> 'Rectangle':
#         new_width = self.width + other.width
#         new_height = self.height + other.height
#         return Rectangle(new_width, new_height)

#     def __sub__(self, other: 'Rectangle') -> 'Rectangle':
#         new_width = max(self.width - other.width, 0)
#         new_height = max(self.height - other.height, 0)
#         return Rectangle(new_width, new_height)

#     def __lt__(self, other: 'Rectangle') -> bool:
#         return self.area() < other.area()

#     def __eq__(self, other: 'Rectangle') -> bool:
#         return self.area() == other.area()

#     def __le__(self, other: 'Rectangle') -> bool:
#         return self.area() <= other.area()

#     def __str__(self) -> str:
#         return f"Прямоугольник со сторонами {self.width} и {self.height}"

#     def __repr__(self) -> str:
#         return f"Rectangle({self.width}, {self.height})"

# # Пример использования
# try:
#     rect1 = Rectangle(5, 10)
#     rect2 = Rectangle(-3, 7)  # Здесь будет выброшено исключение NegativeValueError
# except NegativeValueError as e:
#     print(e)


# Задача 4


# class Matrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0 for _ in range(cols)] for _ in range(rows)]

#     def __str__(self):
#         return '\n'.join([' '.join(map(str, row)) for row in self.data])

#     def __repr__(self):
#         return f'Matrix({self.rows}, {self.cols})'

#     def __eq__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             return False
#         return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))

#     def __add__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for addition")
#         result = Matrix(self.rows, self.cols)
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 result.data[i][j] = self.data[i][j] + other.data[i][j]
#         return result

#     def __mul__(self, other):
#         if self.cols != other.rows:
#             raise ValueError("The number of columns of the first matrix must be equal to the number of rows of the second matrix")
#         result = Matrix(self.rows, other.cols)
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
#         return result

# matrix1 = Matrix(2, 3)
# matrix1.data = [[1, 2, 3], [4, 5, 6]]

# matrix2 = Matrix(2, 3)
# matrix2.data = [[7, 8, 9], [10, 11, 12]]

# print(matrix1)
# print(matrix2)
# print(matrix1 == matrix2)

# matrix_sum = matrix1 + matrix2
# print(matrix_sum)

# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]

# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]

# result = matrix3 * matrix4
# print(result)
