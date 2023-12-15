# создает пересечение множеств: формирует новое множества с элементами которые
# есть и в первом множестве и во втором

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set # замена функции intersection символом &
print (f'{my_set = }\n{other_set = }\n{new_set = }')