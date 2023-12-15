# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
#  Каждая группа включает файлы с несколькими расширениями.
#  В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil

def sort_files(directory):
    categories = {
        'videos': ['.mp4', '.avi', '.mkv'],
        'images': ['.jpg', '.jpeg', '.png'],
        'texts': ['.txt', '.doc', '.pdf']
    }
    
    for filename in os.listdir(directory):
        path1 = os.path.join(directory, filename)
        
        if not os.path.isfile(path1):
            continue
        
        for category, extension in categories.items():
            if filename.endswith(tuple(extension)):
                end_folder = os.path.join(directory, category)
                if not os.path.exists(end_folder):
                    os.mkdir(end_folder)
                shutil.move(path1, os.path.join(end_folder, filename))



sort_files(os.getcwd())
