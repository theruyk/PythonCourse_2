text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open ('new_data.txt', 'w', encoding='utf-8') as f:
  print (f.tell())
  for line in text:
    f.write(f'{line}\n')
    print (f.tell())
  print(f.tell())
  print (f .tell()) # ValueError: I/0 operation on closed file.