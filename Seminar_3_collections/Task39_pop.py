# pop удаляет пару ключ-значение по ключу

my_dict = {'one': 1, 'two': 2,'three': 3, 'four': 4,'ten': 10}
spam = my_dict.pop ('two')
print (f' {spam = }\t{my_dict=}')
#err = my_dict.pop('six') # KeyError: 'six'
#err = my_dict.pop () # TypeError: pop expected at least 1 argument, got o