# Распаковка

a, b, c = input ("Три символа: ")
print (f' {a=} {b=} {c=}')

a, b, с = {"один", "два", "три", "четыре", "Пять"} # значений должно быть столько же сколько и переменных 
print(f' {a=} {b=} {c=}') # ValueError: too many values to unpack (expected 3)