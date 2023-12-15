# создание нового списка внутри функции чтобы каждый раз создавался новый список,
# а не дополнялся старый

def from_one_to_n(n, data=None):
  if data is None: # is рекомендуется вместо == так как читается и работает быстрее 
    data = []
  for i in range (1, n + 1):
    data.append (i)
  return data

new_list = from_one_to_n(5)
print (f'{new_list = }')
other_list = from_one_to_n(7)
print (f'{other_list = }')