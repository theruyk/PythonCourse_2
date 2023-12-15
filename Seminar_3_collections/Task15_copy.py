
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print (my_list, new_list, sep='\n')

my_list [2] = 555
print (my_list, new_list, sep='\n')

# при таком методе копирования изменения будут вноситься в оба списка, так как 
# один список будет просто ссылаться на другой поэтому нужно пользоваться функцией 
#copy:
print()

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print (my_list, new_list, sep='\n')

my_list [2] = 555
print (my_list, new_list, sep='\n')