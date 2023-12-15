input_string = "aaabbbcde"

count = 0
dict1 ={}
for i in input_string:
  for j in input_string:
    if i == j:
      count +=1
      dict1[i] = count
  count = 0

max_value = 0
list1 = []
for key,value in dict1.items():
  if value >= max_value:
    max_value = value
    list1.append(key)

print(list1)