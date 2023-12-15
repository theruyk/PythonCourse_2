# Метод pop без индекса элемента (строка 4), берет последний элемент и удаляет 
# его из списка. 

my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop() # сохранение удаленного элемента в переменную
print (spam, my_list)
eggs = my_list.pop (1)
print (eggs, my_list)
# err = my_list.pop (10) # IndexError: pop index out of range