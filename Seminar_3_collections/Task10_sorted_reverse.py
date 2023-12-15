# Принимает на вход списоки возвращает НОВЫЙ список с отсортированными данными
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted (my_list)
print (my_list, sort_list, sep='\n')
rev_list = sorted (my_list, reverse=True) # создает новый список в реверсивном порядке
print (my_list, rev_list, sep='\n')

# СОЗДАЮТСЯ НОВЫЕ СПИСКИ, СТАРЫЕ НЕ ИЗМЕНЯЮТСЯ