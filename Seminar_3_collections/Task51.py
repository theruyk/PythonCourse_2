# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте # если возможно в один из вариантов ниже:
#целое положительное число 
# вещественное положительное или отрицательное число 
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква 
# строку в верхнем регистре в остальных случаях

text = input ("Введите текст: ")
if text.isnumeric():
  print(int (text))
elif text.replace('.','',1).isnumeric():
  print(float (text))
elif text [0] == '-' and text.replace('.','',1).replace('.','',1).isnumeric():
  print(float (text))
elif not text.islower ():
  print(text.lower())
else:
  print(text.upper())
