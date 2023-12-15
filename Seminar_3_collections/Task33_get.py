# Получение значения по ключу методом get
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print (my_dict.get('five'))
print (my_dict.get('five', 5)) # 5 - значение по умолчанию и так как такого 
#ключа нет в словаре то вернет его
print(my_dict.get ('ten', 5))