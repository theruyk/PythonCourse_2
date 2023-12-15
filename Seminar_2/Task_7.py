import sys
STEP = 2 ** 16
num = 1
for _ in range (30): # _ когда не нужна переменная в цикле
  print(sys.getsizeof(num), num) #функция для узнавания занимаемой объектом памяти
  num *= STEP