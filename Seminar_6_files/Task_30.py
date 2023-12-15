import os

# Создать папку Seminar_7
directory = "Seminar_7"
if not os.path.exists(directory):
    os.makedirs(directory)

# В цикле создать файлы Task_1.py до Task_30.py в папке Seminar_7
for i in range(1, 31):
    filename = f"Task_{i}.py"
    filepath = os.path.join(directory, filename)
    
    # Создаем пустой файл (если файл уже существует, его содержимое не изменится)
    open(filepath, 'a').close()

print(f"Created 30 files in {directory}/")
