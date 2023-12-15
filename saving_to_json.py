import json

class JsonContextManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def __enter__(self):
        # Возвращаем себя, чтобы можно было добавлять данные
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # При выходе из контекста сохраняем данные в JSON
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"Данные сохранены в файле {self.filename}")

    def add_data(self, key, value):
        # Метод для добавления данных, которые будем сохранять
        self.data[key] = value

# Использование класса JsonContextManager с оператором with
with JsonContextManager('my_data.json') as json_manager:
    json_manager.add_data('name', 'John Doe')
    json_manager.add_data('age', 30)
    json_manager.add_data('city', 'New York')

# После выхода из блока with данные будут автоматически сохранены в 'my_data.json'
