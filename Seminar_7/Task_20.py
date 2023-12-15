Общая статистика
Всего тестов: 5. Пройдено: 0. Не пройдено: 5.

Подробную информацию по каждому тесту смотрите ниже.

Тест 1
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

import warnings
import os
import json
import csv
import pickle


def get_size(path):
    try:
        total = 0
        if os.path.isfile(path):
            return os.path.getsize(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
        return total
    except Exception as e:
        print(f"Error calculating size for {path}: {e}")
        return 0

def traverse_directory(directory):
    results = []
    try:
        for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
            # Эта строка нужна для того, чтобы исключить рекурсивный обход вложенных директорий
            # Это позволит функции get_size правильно рассчитать размер родительской директории
            dirnames[:] = []

            # Для директорий
            for d in dirnames:
                dir_full_path = os.path.join(dirpath, d)
                results.append({
                    "Path": dir_full_path,
                    "Type": "Directory",
                    "Size": get_size(dir_full_path),
                    "Parent Directory": dirpath
                })

            # Для файлов
            for f in filenames:
                file_full_path = os.path.join(dirpath, f)
                results.append({
                    "Path": file_full_path,
                    "Type": "File",
                    "Size": os.path.getsize(file_full_path),
                    "Parent Directory": dirpath
                })
    except Exception as e:
        print(f"Error traversing {directory}: {e}")
    return results

def save_results_to_json(data, filename="results.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def save_results_to_csv(data, filename="results.csv"):
    try:
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_results_to_pickle(data, filename="results.pickle"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"Error saving to Pickle: {e}") 

 


directory = 'geekbrains'
results = traverse_directory(directory)
print(results)


Ожидаемый ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]

Ваш ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85, 'Parent Directory': 'geekbrains'}]
Тест 2
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

import warnings
import os
import json
import csv
import pickle


def get_size(path):
    try:
        total = 0
        if os.path.isfile(path):
            return os.path.getsize(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
        return total
    except Exception as e:
        print(f"Error calculating size for {path}: {e}")
        return 0

def traverse_directory(directory):
    results = []
    try:
        for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
            # Эта строка нужна для того, чтобы исключить рекурсивный обход вложенных директорий
            # Это позволит функции get_size правильно рассчитать размер родительской директории
            dirnames[:] = []

            # Для директорий
            for d in dirnames:
                dir_full_path = os.path.join(dirpath, d)
                results.append({
                    "Path": dir_full_path,
                    "Type": "Directory",
                    "Size": get_size(dir_full_path),
                    "Parent Directory": dirpath
                })

            # Для файлов
            for f in filenames:
                file_full_path = os.path.join(dirpath, f)
                results.append({
                    "Path": file_full_path,
                    "Type": "File",
                    "Size": os.path.getsize(file_full_path),
                    "Parent Directory": dirpath
                })
    except Exception as e:
        print(f"Error traversing {directory}: {e}")
    return results

def save_results_to_json(data, filename="results.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def save_results_to_csv(data, filename="results.csv"):
    try:
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_results_to_pickle(data, filename="results.pickle"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"Error saving to Pickle: {e}") 

 


directory = 'geekbrains/my_ds_projects'
results = traverse_directory(directory)
print(results)


Ожидаемый ответ:

[{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]

Ваш ответ:

[]
Тест 3
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

import warnings
import os
import json
import csv
import pickle


def get_size(path):
    try:
        total = 0
        if os.path.isfile(path):
            return os.path.getsize(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
        return total
    except Exception as e:
        print(f"Error calculating size for {path}: {e}")
        return 0

def traverse_directory(directory):
    results = []
    try:
        for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
            # Эта строка нужна для того, чтобы исключить рекурсивный обход вложенных директорий
            # Это позволит функции get_size правильно рассчитать размер родительской директории
            dirnames[:] = []

            # Для директорий
            for d in dirnames:
                dir_full_path = os.path.join(dirpath, d)
                results.append({
                    "Path": dir_full_path,
                    "Type": "Directory",
                    "Size": get_size(dir_full_path),
                    "Parent Directory": dirpath
                })

            # Для файлов
            for f in filenames:
                file_full_path = os.path.join(dirpath, f)
                results.append({
                    "Path": file_full_path,
                    "Type": "File",
                    "Size": os.path.getsize(file_full_path),
                    "Parent Directory": dirpath
                })
    except Exception as e:
        print(f"Error traversing {directory}: {e}")
    return results

def save_results_to_json(data, filename="results.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def save_results_to_csv(data, filename="results.csv"):
    try:
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_results_to_pickle(data, filename="results.pickle"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"Error saving to Pickle: {e}") 

 


directory = 'geekbrains'
results = traverse_directory(directory)
save_results_to_json(results, 'results.json')

with open('results.json', 'r') as f:
    data = json.load(f)

print(data)


Ожидаемый ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]

Ваш ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85, 'Parent Directory': 'geekbrains'}]
Тест 4
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

import warnings
import os
import json
import csv
import pickle


def get_size(path):
    try:
        total = 0
        if os.path.isfile(path):
            return os.path.getsize(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
        return total
    except Exception as e:
        print(f"Error calculating size for {path}: {e}")
        return 0

def traverse_directory(directory):
    results = []
    try:
        for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
            # Эта строка нужна для того, чтобы исключить рекурсивный обход вложенных директорий
            # Это позволит функции get_size правильно рассчитать размер родительской директории
            dirnames[:] = []

            # Для директорий
            for d in dirnames:
                dir_full_path = os.path.join(dirpath, d)
                results.append({
                    "Path": dir_full_path,
                    "Type": "Directory",
                    "Size": get_size(dir_full_path),
                    "Parent Directory": dirpath
                })

            # Для файлов
            for f in filenames:
                file_full_path = os.path.join(dirpath, f)
                results.append({
                    "Path": file_full_path,
                    "Type": "File",
                    "Size": os.path.getsize(file_full_path),
                    "Parent Directory": dirpath
                })
    except Exception as e:
        print(f"Error traversing {directory}: {e}")
    return results

def save_results_to_json(data, filename="results.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def save_results_to_csv(data, filename="results.csv"):
    try:
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_results_to_pickle(data, filename="results.pickle"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"Error saving to Pickle: {e}") 

 


directory = 'geekbrains'
results = traverse_directory(directory)
save_results_to_csv(results, 'results.csv')

with open('results.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

print(data)


Ожидаемый ответ:

[['Path', 'Type', 'Size'], ['geekbrains/california_housing_train.csv', 'File', '1457'], ['geekbrains/student_performance.txt', 'File', '21'], ['geekbrains/covid.json', 'File', '35228079'], ['geekbrains/input2.txt', 'File', '9'], ['geekbrains/avg_list.txt', 'File', '21'], ['geekbrains/age_report.csv', 'File', '85'], ['geekbrains/my_ds_projects', 'Directory', '684'], ['geekbrains/my_ds_projects/My-code', 'Directory', '342'], ['geekbrains/my_ds_projects/My-code/GB_data', 'Directory', '171'], ['geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'File', '101'], ['geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'File', '70']]

Ваш ответ:

[['Path', 'Type', 'Size', 'Parent Directory'], ['geekbrains/california_housing_train.csv', 'File', '1457', 'geekbrains'], ['geekbrains/student_performance.txt', 'File', '21', 'geekbrains'], ['geekbrains/covid.json', 'File', '35228079', 'geekbrains'], ['geekbrains/input2.txt', 'File', '9', 'geekbrains'], ['geekbrains/avg_list.txt', 'File', '21', 'geekbrains'], ['geekbrains/age_report.csv', 'File', '85', 'geekbrains']]
Тест 5
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

import warnings
import os
import json
import csv
import pickle


def get_size(path):
    try:
        total = 0
        if os.path.isfile(path):
            return os.path.getsize(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total += os.path.getsize(fp)
        return total
    except Exception as e:
        print(f"Error calculating size for {path}: {e}")
        return 0

def traverse_directory(directory):
    results = []
    try:
        for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
            # Эта строка нужна для того, чтобы исключить рекурсивный обход вложенных директорий
            # Это позволит функции get_size правильно рассчитать размер родительской директории
            dirnames[:] = []

            # Для директорий
            for d in dirnames:
                dir_full_path = os.path.join(dirpath, d)
                results.append({
                    "Path": dir_full_path,
                    "Type": "Directory",
                    "Size": get_size(dir_full_path),
                    "Parent Directory": dirpath
                })

            # Для файлов
            for f in filenames:
                file_full_path = os.path.join(dirpath, f)
                results.append({
                    "Path": file_full_path,
                    "Type": "File",
                    "Size": os.path.getsize(file_full_path),
                    "Parent Directory": dirpath
                })
    except Exception as e:
        print(f"Error traversing {directory}: {e}")
    return results

def save_results_to_json(data, filename="results.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def save_results_to_csv(data, filename="results.csv"):
    try:
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_results_to_pickle(data, filename="results.pickle"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"Error saving to Pickle: {e}") 

 


directory = 'geekbrains'
results = traverse_directory(directory)
save_results_to_pickle(results, 'results.pkl')

with open('results.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)


Ожидаемый ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85}, {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684}, {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101}, {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}]

Ваш ответ:

[{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21, 'Parent Directory': 'geekbrains'}, {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85, 'Parent Directory': 'geekbrains'}]