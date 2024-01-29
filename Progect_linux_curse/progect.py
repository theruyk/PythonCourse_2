from checkers import checkout, getout
import yaml
import pytest




@pytest.mark.usefixtures('make_folders','make_files','make_subfolder','clear_folders','stats_collector')
class TestSevenZ:

  def test_step1(self,data):
      # Тест 1: Создание архива из содержимого папки folder_in.
      res1 = checkout("cd {}; 7z a {}/arx2 *".format(data.get('folder_in'), data.get('folder_out')), "Everything is Ok")
      res2 = checkout("ls {}".format(data.get('folder_out')), "arx2.7z")
      assert res1 and res2, "test1 FAIL"

  def test_step2(self,make_files,data):
      # Тест 2: Проверка наличия файлов внутри архива arx2.7z.
      res = []
      res.append(checkout("cd {}; 7z a {}/arx2".format(data.get('folder_in'), data.get('folder_out')), "Everything is Ok"))
      res.append(checkout("cd {}; 7z e arx2.7z -o{} -y".format(data.get('folder_out'), data.get('folder_ext')), "Everything is Ok"))
      for item in make_files:
          res.append(checkout("ls {}".format(data.get('folder_ext')), item))
      assert all(res), "test2 FAIL"

  def test_step3(self,data):
      # Тест 3: Проверка целостности архива
      assert checkout(f"cd {data.get('folder_out')}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"

  def test_step4(self,data):
      # Тест 4: Проверка обновления содержимого архива
      assert checkout(f"cd {data.get('folder_in')}; 7z u arx2.7z", "Everything is Ok"), "test4 FAIL"

  def test_step5(self,make_files,data):
      # Тест 5: Проверка создания архива и его содержимого
      res = []
      # Создает архив и проверяет, было ли это успешно
      res.append(checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}/arx2", "Everything is Ok"))
      # Проверяет наличие каждого файла из списка make_files в архиве arx2.7z
      for item in make_files:
          res.append(checkout(f"cd {data.get('folder_out')}; 7z l arx2.7z", item))
      # Проверяет, что все предыдущие действия прошли успешно
      assert all(res), "test5 FAIL"

  def test_step6(self,make_files,data):
      # Тест 6: Проверка содержимого архива и извлечения файлов
      res = []
      # Создает архив и проверяет, было ли это успешно
      res.append(checkout(f"cd {data.get('folder_in')}; 7z a {data.get('folder_out')}/arx", "Everything is Ok"))
      # Извлекает содержимое архива и проверяет, было ли это успешно
      res.append(checkout(f"cd {data.get('folder_out')}; 7z x arx.7z -o{data.get('folder_ext2')} -y", "Everything is Ok"))
      # Проверяет наличие каждого файла из списка make_files в извлеченной папке folder_ext2
      for item in make_files:
          res.append(checkout(f"ls {data.get('folder_ext2')}", item))
      # Проверяет, что все предыдущие действия прошли успешно
      assert all(res), "test6 FAIL"

  def test_step7(self,data):
      # Тест 7: Проверка удаления содержимого архива
      assert checkout(f"cd {data.get('folder_out')}; 7z d arx.7z", "Everything is Ok"), "test7 FAIL"

  def test_step8(self,make_files,data):
      # Тест 8: Проверка расчета хеша файлов и сравнение с выводом команды crc32
      res = []
      for item in make_files:
          # Выполняет команду для расчета хеша файла с помощью 7z и добавляет результат в список res
          res.append(checkout(f"cd {data.get('folder_in')}; 7z h {item}", "Everything is Ok"))
          # Вызывает команду crc32 для расчета хеша и преобразует вывод в верхний регистр
          hash = getout(f"cd {data.get('folder_in')}; crc32 {item}").upper()
          # Выполняет команду для проверки хеша файла с помощью 7z и добавляет результат в список res
          res.append(checkout(f"cd {data.get('folder_in')}; 7z h {item}", hash))
      # Проверяет, все ли результаты в res истинны (True)
      assert all(res), "test8 FAIL"

# if __name__ == '__main__':
#  pytest.main['-vv']

#pytest -vv /Users/the_ryuk/Desktop/PythonCurse_2/Progect_linux_curse/progect.py

#pytest --alluredir=/Users/the_ryuk/Desktop/PythonCurse_2/results2 /Users/the_ryuk/Desktop/PythonCurse_2/Progect_linux_curse/progect.py
#allure serve /Users/the_ryuk/Desktop/PythonCurse_2/results2
