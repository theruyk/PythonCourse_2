import os
from pathlib import Path
print(os.getcwd()) #возвращает путь к текущей дериктории
print(Path.cwd())

os.chdir(' ../.. ') # смена директории
print (os.getcwd())
print (Path.cwd ())