# while True - это бесконечный цикл который прерывается командой break при исполнении
# условий блока if

min_limit = 0
max_limit = 10

while True:
    print(f'Введи число между {min_limit} и {max_limit}: ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break

print(f'Было введено число {num}')
