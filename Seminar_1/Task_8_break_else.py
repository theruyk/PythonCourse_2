# Если цикл выходит самостоятельно то срабатывает else, если внутри цикла срабатывает 
# команда break то else относящийся к циклу не срабатывает.

min_limit = 0
max_limit = 10
count = 3

while count > 0:
    print('Попытка', count)
    count -= 1
    print('Введи число между', min_limit, 'и', max_limit, "? ")
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()

print(f'Было введено число {num}')
