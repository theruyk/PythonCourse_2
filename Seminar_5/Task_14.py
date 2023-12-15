car = { "brand" : 'Toyota', "model" : 'Corolla', "year" : 2020}
car["Color"] = 'blue'
car["year"] = 2021
for key,value in car.items():
  print(f'{key} : {value}')

students = {'John': {'math': 5, 'history': 4}, 'Anna': {'math': 4, 'history': 5}}
students['Anya'] = {'math' : 2, 'history' : 2}
for key,value in students.items():
  print(f"{key} по математике имеет {value['math']} баллов")

zoo = {'lions': ['Simba', 'Nala'], 'elephants': ['Dumbo']}
zoo['monkeys'] = ['pupa', 'lupa']
zoo['lions'].append('Duda')
print(f'Имена львов : {zoo["lions"]}')