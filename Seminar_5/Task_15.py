votes = ["Alice", "Bob", "Alice", "Alice", "Bob", "Charlie", "Charlie", "Alice"]
dict1 = {}
for i in votes:
  count = 0
  for j in votes:
    if i == j:
      count +=1
  dict1[i] = count
print(dict1)

duplicated_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7]
to_set = set(duplicated_list)
to_new_list = list(to_set)
print(to_new_list)


personal_info = {"name": "John", "age": 25}
address_info = {"city": "New York", "postcode": "10001"}
for key, value in address_info.items():
  personal_info[key] = value
print(personal_info)

text = 'Сюжет картины основан на летописном сказании о сражении 992 года, \
 в котором древнерусское войско князя Владимира Святославича победило печенегов.\
Перед началом битвы надо было найти воина, который смог бы достойно сразиться \
с печенежским богатырём. Им оказался сын киевского кожемяки Ян Усмарь, который\
с честью выдержал предложенное ему испытание — руками остановил бегущего \
разъярённого быка, вырвав у него кусок кожи.'

dict2 = {}
for i in text:
  count = 0
  for j in text:
    if i == j:
      count +=1
  dict2[i] = count
print(dict2)


countries = {"France": "Paris", "Spain": "Madrid", "Germany": "Berlin"}
dict3 = {}

for key, value in countries.items():
  dict3[value] = key
print(dict3)