data = [
    {"name": "Anna", "age": 25, "job": "engineer"},
    {"name": "Bob", "age": 30, "job": "data scientist"},
    {"name": "Charlie", "age": 29, "job": "manager"}
]


def func(data):
  new_list = []
  for i in data:
    if i["age"] >= 28 and i["job"] != "data scientist":
      new_list.append(i)
  return new_list

print(func(data))