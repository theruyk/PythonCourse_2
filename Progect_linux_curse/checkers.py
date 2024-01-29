import subprocess
import string

def checkout(cmd: str, text: str, find_words_mode: bool = False) -> bool:
    """
    Выполняет команду в оболочке и проверяет, содержится ли заданный текст в её выводе.
    
    :param cmd: Команда для выполнения в виде строки.
    :param text: Текст для поиска в выводе команды.
    :return: True если текст найден и команда завершилась успешно, иначе False.
    :find_words_mode: Ищет слово и удаляет пунктуацию
    """
    # Выполнение команды в оболочке и захват стандартного вывода
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    
    # Печать результата команды в стандартный вывод
    print(result.stdout)
    
    # Проверка наличия заданного текста в выводе и успешного завершения команды (код возврата 0)
    # if text in result.stdout and result.returncode == 0:
    #     return True
    # else:
    #     return False

    if find_words_mode:
        translation_table = str.maketrans('', '', string.punctuation)
        output_without_punctuation = result.stdout.translate(translation_table).split()
        return text in output_without_punctuation and result.returncode == 0
    else:
        # Стандартная проверка наличия заданного текста в выводе
        return text in result.stdout and result.returncode == 0


