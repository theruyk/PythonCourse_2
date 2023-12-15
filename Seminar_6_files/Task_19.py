text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
'Consequatur debitis explicabo Laboriosam sint suscipit temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit guia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
  for line in text:
   print(line, file=f)