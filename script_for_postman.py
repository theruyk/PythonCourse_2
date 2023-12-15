import subprocess

# Путь к файлу коллекции Postman и файлу среды выполнения
collection_path = '/Users/the_ryuk/Desktop/PythonCurse_2/Postman Requests/Test_reqres.postman_collection.json'
#environment_path = 'path/to/your/environment.json'

def run_newman_tests():
  # Запуск Newman с помощью Python
  result = subprocess.run(['newman', 'run', collection_path,'--color', 'on'], capture_output=True, text=True)
  print(result.stdout)

# subprocess.run(
#     ['newman', 'run', collection_path, '-e', environment_path, '--color', 'on'],
#     stdout=sys.stdout,
#     stderr=sys.stderr
# )

    # Проверяем, были ли ошибки и выводим их
  if result.stderr:
    print(result.stderr)

# Вызываем функцию запуска тестов
run_newman_tests()