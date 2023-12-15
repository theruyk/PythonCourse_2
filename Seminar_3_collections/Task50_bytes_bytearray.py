x = bytes (b'\xd0\x9f\xd1\x80\xd0\xb8') # неизменяемая последовательность
y = bytearray (b'\xd0\x9f\xd1\x80\xd0\xb8')# изменяемый массив байт
print (f'{x = }\n{y = }')