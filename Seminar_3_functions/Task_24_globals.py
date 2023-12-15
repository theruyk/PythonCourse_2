"""globals)"""

SIZE = 10

def func (a, b, c) :
  x = a + b
  print (globals())
  z = x + c
  return z

print (globals())
print (f'{func(1, 2, 3) = }')

# изменяем словарь globals
x = 42
glob_dict = globals ()
glob_dict['x'] = 73
print (f'{x = }')