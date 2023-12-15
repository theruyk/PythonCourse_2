num = 2 + 2 * 2
digit = 36 / 6
print (num, digit) # в первом случае целое число, во втором - вещественное
print (num == digit) # значения чисел равны  между собой получаем True
print (num is digit) # типы у чисел разные, обьекты лежат в разных
# ячейках в оперативной памяти поэтому получаем False
print(type(num), type(digit))
print(id(num), id(digit))