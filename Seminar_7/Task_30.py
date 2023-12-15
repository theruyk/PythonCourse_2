# Исходное предложение
text = "Привет, как дела?"

# Разделяем предложение на слова
words = text.split()

# Инвертируем каждое слово в списке
inverted_words = [word[::-1] for word in words]

# Собираем слова обратно в строку
inverted_text = ' '.join(inverted_words)

print(inverted_text)
