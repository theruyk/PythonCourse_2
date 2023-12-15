import subprocess

def checkout(cmd, text):
    # Выполнение команды в оболочке и захват стандартного вывода
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    
    # Печать результата команды в стандартный вывод
    print(result.stdout)
    
    # Проверка наличия заданного текста в выводе и успешного завершения команды (код возврата 0)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def checkout_negative(cmd, text):
    # Выполнение команды в оболочке и захват как стандартного вывода, так и стандартного потока ошибок
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    
    # Проверка наличия заданного текста в выводе или потоке ошибок и неуспешного завершения команды (код возврата не 0)
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False

def getout(cmd):
    # Выполнение команды и возвращение её вывода
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
