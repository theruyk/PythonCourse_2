# Напишите функцию, которая принимает два булевых значения: is_weekend и 
# is_vacation. Если сейчас выходные или отпуск, будильник не должен звонить. 
# Если это рабочий день и не отпуск, будильник должен звонить. Верните True, если 
# будильник звонит, и False в противном случае.

def alarm(is_weekend, is_vacation):
    if is_weekend or is_vacation:
        return False
    else:
        return True

print("1: Выходной\n2: Отпуск\n3: Рабочий день")
day = int(input('Введите 1, 2 или 3: '))

is_weekend = False
is_vacation = False

if day == 1:
    is_weekend = True
elif day == 2:
    is_vacation = True

print(alarm(is_weekend, is_vacation))
