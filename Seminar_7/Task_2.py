# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
# # среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

import random

def name_gan(file: str, count:int):
  glas = 'eyuioa'
  sagl ='gwrtpsdfghjklzxcvbnm'
  

  with open('text.txt', 'a', encoding='utf-8') as data:
    for j in range (count):
      answer = []
      num_it = random. randint (4, 7)
      for i in range(random.randint(4, 7)):
        answer.extend([random.choice(glas),random.choice(sagl)]) 
      print(''.join(answer).title()[:num_it],file = data)

if __name__=='__main__':
  name_gan('text.txt',5)