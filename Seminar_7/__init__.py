import os
import json
import pickle
import csv

def get_dir_size(path):
    """Возвращает размер директории в байтах."""
    total = 0
    if os.path.isfile(path):
        total += os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
    return total

def save_results_to_json(results, filename="results.json"):
    """Сохраняет результаты в файл JSON."""
    with open(filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)

def save_results_to_csv(results, filename="results.csv"):
    """Сохраняет результаты в файл CSV."""
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ["Path", "Type", "Size"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

def save_results_to_pickle(results, filename="results.pkl"):
    """Сохраняет результаты в файл pickle."""
    with open(filename, 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

def traverse_directory(directory):
    """Просматривает директорию и возвращает список файлов и директорий с их размерами."""
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            results.append({
                "Path": filepath,
                "Type": "File",
                "Size": os.path.getsize(filepath)
            })
        for name in dirs:
            dirpath = os.path.join(root, name)
            results.append({
                "Path": dirpath,
                "Type": "Directory",
                "Size": get_dir_size(dirpath)
            })
    return results
