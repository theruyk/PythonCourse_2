"""iter (object[, sentinel])"""

a = 42
#iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print (list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print (*list_iter)
print(*list_iter)

# итератор проходит по объекту один раз поэтому последние 2 принта не выводятся
# нужно создавать новый объект