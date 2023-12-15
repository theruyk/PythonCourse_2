# Позиционные и ключевые аргументы 

def combined_example (pos_only, /, standard, *, kwd_only) :
  """Пример функции со всеми вариантами параметров"""
  print (pos_only, standard, kwd_only) # Принтим для примера,
#combined_example (1, 2, 3) # TypeError: combined_example() tak combined_example (1, 2, kwd_only=3) 
combined_example(1, standard=2, kwd_only=3)
#combined_example (pos_only=1, standard=2, kwd_only=3) 