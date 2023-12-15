# Создайте вручную слисок с повторяюшимися элементами.
# Удалите из него все элементы, которые встречаются дважды.
my_list = [2, 5, 3, 3, 3, 2, 5, 10, 11, 12]
for i in my_list:
  if my_list.count (i) == 2: 
    for j in range (2):
      my_list.remove (i)
print (my_list)