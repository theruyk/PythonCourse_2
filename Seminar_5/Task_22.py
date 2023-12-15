# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
#  выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая
# расстановка ферзей на шахматной доске, в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом, что они не находятся на одной 
# вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать
# его не надо.
# Пример использования На входе:
# print(generate_boards())
# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]

import random
def is_valid(board, row, col):
    for prev_row in range(row):
        if board[prev_row] == col or \
            board[prev_row] - prev_row == col - row or \
            board[prev_row] + prev_row == col + row:
            return False
    return True

def generate_board():
    board = [-1] * 8
    row = 0
    while row < 8:
        valid_cols = [i for i in range(8) if is_valid(board, row, i)]
        if not valid_cols:  
            board = [-1] * 8
            row = 0
            continue
        col = random.choice(valid_cols)
        board[row] = col
        row += 1
    return [(i + 1, board[i] + 1) for i in range(8)]

def generate_boards():
    return [generate_board() for _ in range(4)]

board_list = generate_boards()
if len(board_list) != 4:
    print("Вы собрали не то количество комбинаций")
else:
    print("Отлично!")

print(generate_boards())