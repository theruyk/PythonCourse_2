#аннотация типов нужна для облегчения читаемости кода, при этом сам пайтон это не учитывает

def my_func (data: list[int, float]) -> float: #функция ожидает массив с типами int, float и отдаст float
  res = sum (data) / len (data)
  return res
print (my_func([2, 5.5, 15, 8.0, 13.74]))