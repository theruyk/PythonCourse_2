import pytest
import yaml
from checkers import checkout, getout
import string
import random
import os
import datetime
import psutil
import time

@pytest.fixture(scope="session")
def data():
    with open('config.yaml', encoding='utf-8') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            pytest.fail(f"YAML loading error: {exc}")

# Фикстура pytest для создания папок перед выполнением тестов
@pytest.fixture(scope='class')
def make_folders(data):
    # Использует функцию checkout для выполнения команды mkdir и создания папок
    return checkout(f"mkdir -p {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_ext')} {data.get('folder_ext2')}", "")

# Фикстура pytest для создания тестовых файлов
@pytest.fixture(scope='class')
def make_files(data):
    list_of_files = []
    # Генерируем 5 случайных имен файлов и создаем их с помощью команды dd
    for i in range(5):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout(f"cd {data.get('folder_in')}; dd if=/dev/urandom of={filename} bs=1M count=1 iflag=fullblock", ""):
            list_of_files.append(filename)
    return list_of_files

# Фикстура pytest для создания подпапок
@pytest.fixture(scope='class')
def make_subfolder(data):
    # Генерируем случайное имя для тестового файла и подпапки
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    # Создаем подпапку
    if not checkout(f"cd {data.get('folder_in')}; mkdir {subfoldername}", ""):
        return None, None
    # Создаем тестовый файл
    if not checkout(f"cd {data.get('folder_in')}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs=1M count=1 iflag=fullblock", ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename
        
# Фикстура для очистки папок перед тестом
@pytest.fixture(scope='class')
def clear_folders(data):
    # Используется функция checkout для удаления содержимого папок
    yield
    return checkout(f"rm -rf folder_in/* folder_out/* folder_ext/* folder_ext2/*", "")

@pytest.fixture(autouse=True)
def stats_collector(request, data):
    def finalizer():
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_count = len(os.listdir(data['folder_in']))
        file_sizes = sum(os.path.getsize(os.path.join(data['folder_in'], f)) for f in os.listdir(data['folder_in']))
        
        # Первый вызов для инициализации измерения
        psutil.cpu_percent(interval=None)
        time.sleep(1)  # Небольшая задержка
        cpu_load = psutil.cpu_percent(interval=None)  # Второй вызов для получения актуального значения загрузки ЦПУ

        with open('stat.txt', 'a') as stat_file:
            stat_file.write(f"{time_now}, {file_count}, {file_sizes}, {cpu_load}\n")

    request.addfinalizer(finalizer)

