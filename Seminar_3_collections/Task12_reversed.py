# создает не список, а объект с реверсированными элементами, их можно поместить в список
my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)

rev_list = list(reversed(my_list))
print(rev_list)

# for item in reversed (my_list): # запустит цикл с конца к началу
#print (item)