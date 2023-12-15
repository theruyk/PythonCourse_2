
with open('text_data.txt','r+', encoding='utf-8') as f: # with также гарантирует безопасное закрытие фаайла
  print (list (f))
print(f.write('Пока')) # ValueError: I/0 operation on closed file.