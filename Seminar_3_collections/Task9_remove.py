# Метод проходит по списку и ищет элемент с таким значением и удаляет его, все 
# элементы сдвигаются соответственно
my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove (6) # удалит только первый встречный элемент с таким значением
print (my_list)
# my_list.remove (3) # ValueError: list.remove (x): × not in list print (my_list)