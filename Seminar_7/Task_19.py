import warnings
import os
import json
import csv
import pickle

warnings.filterwarnings('ignore')

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