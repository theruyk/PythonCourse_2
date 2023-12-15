from collections import Counter
import string

def analyze_text(cleaned_text: str) -> tuple:
    words = cleaned_text.split()
    word_counter = len(words)  # Подсчет слов
    unique_words = set(words)
    unique_word_counter = len(unique_words)  # Подсчет уникальных слов
    most_often_word = Counter(words).most_common(1)[0][0]  # Наиболее частое слово
    return word_counter, unique_word_counter, most_often_word

text = "Hello world! Hello everyone. Hello world, hello.".lower()
print(text)

# Создание таблицы переводов для удаления знаков препинания
translator = str.maketrans('', '', string.punctuation)

# Удаление знаков препинания из текста
cleaned_text = text.translate(translator)
print(cleaned_text)

# Теперь передаем очищенный текст в функцию
print(analyze_text(cleaned_text))
