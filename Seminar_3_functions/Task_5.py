# def func(*args): - принимает любое число позиционных аргументов
# def func (**kwargs) : - принимает любое число ключевых аргументов
# def func(*args, **kwargs) : - принимает любое число позиционных и ключевых аргументов

def mean (args) :
  return sum(args) / len(args)

print (mean ([1, 2, 3]))
# print (mean (1, 2, 5)) # TypeError: mean() takes 1 positional argument but 3 were given

def mean (*args) :
  return sum (args) / len (args)
print (mean(*[1, 2, 3])) # распакует кортеж и возмет каждое число как отдельный аргумент
print (mean (1, 2, 3))