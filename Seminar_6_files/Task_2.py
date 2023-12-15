f = open ('data.txt','wb')
f.write('Привет, '.encode('utf-8') + 'мир!' .encode ('cp1251')) 
f.close ()

# f = open ('data.txt','p' , encoding= 'utf-8')
# print(list (f))# UnicodeDecodeError: 'utf-8' codec can't decode byte Oxec in position 14: invalid
# f.close ()

f = open ('data.txt','r', encoding= 'utf-8', errors= 'replace')
print(list(f))
f.close ()