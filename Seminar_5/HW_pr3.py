# Напишите функцию, которая принимает целое число. Если число делится на 5 или на
#  7 (но не на оба одновременно), верните True. В противном случае верните False.

def func_(num):
    if (num % 5 == 0 and num % 7 != 0) or (num % 7 == 0 and num % 5 != 0):
        return True
    else:
        return False

print(func_(num = int(input('Input num: '))))
