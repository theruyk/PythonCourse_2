# Урок 12. ООП. Финал

import csv
import os

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not value.istitle() or not value.replace(" ", "").isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects_file = subjects_file
        self.subjects = {}
        self.load_subjects()

    def __str__(self):
        subjects_with_data = [subject for subject, data in self.subjects.items() 
                              if data['grades'] or data['test_scores']]
        subjects_list = ', '.join(subjects_with_data)
        return f"Студент: {self.name}\nПредметы: {subjects_list}"


    def load_subjects(self):
        with open(self.subjects_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for subject in row:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not 0 <= test_score <= 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject in self.subjects and self.subjects[subject]['test_scores']:
            return sum(self.subjects[subject]['test_scores']) / len(self.subjects[subject]['test_scores'])
        return None

    def get_average_grade(self):
        all_grades = [grade for subject in self.subjects.values() for grade in subject['grades']]
        return sum(all_grades) / len(all_grades) if all_grades else None


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
