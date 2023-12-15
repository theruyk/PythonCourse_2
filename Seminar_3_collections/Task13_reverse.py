# reverse реверсирует текущий список, не создавая новый
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print (my_list)

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[:: -1] # сделать срез от начала до конца списка в обратном 
# порядке, тот же разворот списка
print (my_list, new_list, sep='\n')