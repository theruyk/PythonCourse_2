# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для 
# диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. 
# Далее счётчик файлов и расширение

import os

def file_rename(new_name="", serial_number=2, extension="txt", new_extension="txt", name_range=(0, 8)):
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    counter = 1
    
    for file_name in files:
        if file_name.endswith(f".{extension}"):
            part_of_original_name = file_name[name_range[0]:name_range[1]]
            final_name = f"{part_of_original_name}{new_name}{str(counter).zfill(serial_number)}.{new_extension}"
            os.rename(file_name, final_name)
            counter += 1

file_rename(new_name="new_name", extension="csv", new_extension="txt", name_range=(3, 6))
