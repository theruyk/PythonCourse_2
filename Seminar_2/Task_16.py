# Напишите программу, которая решает квадратные уравнения # даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

import math

#(b**2) - 4 * a * c this is diskriminant

def diskriminant (a,b,c) :
  return pow(b, 2) - 4 * a * c


a =float (input ("Ведите а:"))
b =float (input ("Ведите b:"))
c =float (input ("Ведите c:"))


# print(diskriminant (a, b, c))
print (pow(diskriminant (a,b, c) ,0.5))


dis = diskriminant(a,b, c)
kor_dis = pow(diskriminant (a,b, c) , 0.5)


if dis > 0: 
  print((-b+kor_dis)/(2*a))
  print((-b-kor_dis)/(2*a))
elif dis == 0: 
  print((-b-kor_dis)/(2*a))
else:
  print((-b+kor_dis)/(2*a))
  print((-b-kor_dis)/(2*a))