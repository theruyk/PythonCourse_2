import pytest
import yaml
from checkers import checkout, getout
import string
import random
import os
from datetime import datetime
import psutil
import time
from checkers_ssh import ssh_checkout,upload_files, ssh_getout

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
    # Использует функцию ssh_checkout для выполнения команды mkdir на удаленном сервере и создания папок
    folder_in = data['folder_in']
    folder_out = data['folder_out']
    folder_ext = data['folder_ext']
    folder_ext2 = data['folder_ext2']

    mkdir_command = f"mkdir -p {folder_in} {folder_out} {folder_ext} {folder_ext2}"
    
    # Проверка успешности создания папок
    ssh_result = ssh_checkout(data['ip'], data['username'], data['password'], mkdir_command, "created", data['port'])
    
    return ssh_result

# Фикстура pytest для создания тестовых файлов
@pytest.fixture(scope='class')
def make_files(data):
    list_of_files = []
    # Генерируем 5 случайных имен файлов и создаем их с помощью команды dd на удаленном сервере
    for i in range(5):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        dd_command = f"dd if=/dev/urandom of={data.get('folder_in')}/{filename} bs=1M count=1 iflag=fullblock"
        if ssh_checkout(data['ip'], data['username'], data['password'], dd_command, "bytes copied", data['port']):
            list_of_files.append(filename)
    return list_of_files

# Фикстура pytest для создания подпапок
@pytest.fixture(scope='class')
def make_subfolder(data):
    # Генерируем случайное имя для тестового файла и подпапки
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    # Создаем подпапку на удаленном сервере
    mkdir_command = f"mkdir -p {data.get('folder_in')}/{subfoldername}"
    if not ssh_checkout(data['ip'], data['username'], data['password'], mkdir_command, "created", data['port']):
        return None, None
    # Создаем тестовый файл на удаленном сервере
    dd_command = f"dd if=/dev/urandom of={data.get('folder_in')}/{subfoldername}/{testfilename} bs=1M count=1 iflag=fullblock"
    if not ssh_checkout(data['ip'], data['username'], data['password'], dd_command, "1+0 records in", data['port']):
        return subfoldername, None
    return subfoldername, testfilename
        
# Фикстура для очистки папок перед тестом
@pytest.fixture(scope='class')
def clear_folders(data):
    # Очистка папок перед началом теста
    yield  # Это позволяет сначала выполнить тесты, а затем очистить папки после их завершения

    # Команда для удаления содержимого папок на удаленном сервере
    clear_command = f"rm -rf {data.get('folder_in')}/* {data.get('folder_out')}/* {data.get('folder_ext')}/* {data.get('folder_ext2')}/*"
    
    # Выполнение команды удаления
    return ssh_checkout(data['ip'], data['username'], data['password'], clear_command, "", data['port'])



# @pytest.fixture(autouse=True)
# def stats_collector(request, data):
#     def finalizer():
#         time_now =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         file_count = len(os.listdir(data['folder_in']))
#         file_sizes = sum(os.path.getsize(os.path.join(data['folder_in'], f)) for f in os.listdir(data['folder_in']))
        
#         # Первый вызов для инициализации измерения
#         psutil.cpu_percent(interval=None)
#         time.sleep(1)  # Небольшая задержка
#         cpu_load = psutil.cpu_percent(interval=None)  # Второй вызов для получения актуального значения загрузки ЦПУ

#         with open('stat.txt', 'a') as stat_file:
#             stat_file.write(f"{time_now}, {file_count}, {file_sizes}, {cpu_load}\n")

#     request.addfinalizer(finalizer)

@pytest.fixture()
def time_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")