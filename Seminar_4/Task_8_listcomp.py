my_listcomp = [chr (i) for i in range (97, 123)]
print (my_listcomp)
for char in my_listcomp:
  print(char)

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
  if item % 2 == 0:
    res.append (item)
print(f'{res = }')

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print (f'{res = }')