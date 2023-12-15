person = { "first_name": 'Ivan', "last_name": 'Sokolov', "age": 29, "city": 'Almaty'}
print(f'Hello, my name is {person["first_name"]} {person["last_name"]}. I am {person["age"]} years old and I live in {person["city"]}.')

person["hobbies"] = ['Тестирование', 'программирование', 'теннис']

for i in person['hobbies']:
  print(f'One of my hobbies is: {i}')

person["city"] = 'St.Petersburg'
for key,value in person.items():
  print(f'{key} : {value}')