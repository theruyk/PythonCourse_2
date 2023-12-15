# Выведите в консоль таблицу умножения от 2×2 до 9×10
for elem in range(2, 10): 
  for i in range(2, 11):
    print (f' {elem} x {i} = {elem * i}')
  print() 