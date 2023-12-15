# Студент может сдать экзамен, если его рейтинг по курсу выше 50% и он не 
# пропустил более трёх лекций. Напишите функцию, которая принимает процент 
# успеваемости студента и количество пропущенных лекций, и возвращает True,
#  если студент может сдать экзамен, и False в противном случае.

def func_(percent, lecturies):
  return percent > 50 and lecturies < 3

percent = int(input('Input percent: '))
lecturies = int(input('Input num of lecturies: '))
print(func_(percent, lecturies))