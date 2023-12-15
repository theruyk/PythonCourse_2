

def add_two_def(a, b):
  return a + b
add__two_lambda = lambda a, b: a + b # так писать нельзя!

print (add_two_def (42, 3.14))
print(add__two_lambda (42, 3.14))

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted (my_dict.items ())
s_value = sorted (my_dict.items(), key=lambda x: x[1]) # пример использования lambda
print (f' {s_key = }\n{s_value = }')
