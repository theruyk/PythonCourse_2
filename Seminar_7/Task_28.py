# ) Создайте класс Person с атрибутами name и age. Добавьте метод 
# introduce_yourself, который будет выводить информацию в формате 
# "Привет, меня зовут [имя], мне [возраст] лет".

# b) Создайте класс Student, который наследует класс Person. 
# Добавьте новый атрибут grade (оценка). Добавьте метод tell_grade,
#  который будет выводить оценку студента.

# c) Создайте экземпляры обоих классов и вызовите их методы.

# Эти задания позволят вам практиковаться в основных аспектах работы 
# со списками, словарями и классами в Python. Удачи!

class Person:
  def __init__(self, name,age) -> None:
    self.name = name
    self.age = age

  def introduce_yourself(self):
    return print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
    

class Student(Person,grade):
  def __init__(self:super, name,age):
    self.grade = grade

  def tell_grade(self):
    return grade


olga = Person(name = 'Olga',age = 32)
olga2 = Student(name = 'Olga',age = 32, grade = 5)
olga.introduce_yourself()
olga2.tell_grade()