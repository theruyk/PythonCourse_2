# расширение списка через extend, последовательно добавляет элементы в конец
# списка. Не может добавить один элемент. Может добавить элементы из списка 1 в 
# список 1.(удвоит список)
a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend (a) # TypeError: 'int' object is not iterable
print (my_list)
my_list.extend(b)
print (my_list)
my_list.extend(c)
print (my_list)
my_list.extend (my_list)
print (my_list)