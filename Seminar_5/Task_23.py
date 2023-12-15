# Используя map, преобразуйте все слова из списка ["apple", "banana", "cherry"] в верхний регистр.

list1 = ["apple", "banana", "cherry"]
new_list = map(lambda x: x.upper(), list1)
list2 = list(new_list)
print(list2)