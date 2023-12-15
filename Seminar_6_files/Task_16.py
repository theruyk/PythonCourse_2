text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open ('new_data. txt', 'a', encoding='utf-8') as f:
  for line in text:
    res = f.write (f'{line}\n')
    print (f'{res = }\n{len(text) = }')