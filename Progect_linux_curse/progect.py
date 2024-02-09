from checkers import checkout, getout
import yaml
import pytest
from checkers_ssh import ssh_checkout,upload_files, ssh_getout
import datetime
import subprocess

@pytest.mark.usefixtures('make_folders','make_files','make_subfolder','clear_folders')#'stats_collector'
class TestSevenZ:

  def save_log(self, data, time_now, file_name):
      # Команда для получения логов с удаленного сервера
      command = f"journalctl --since '{time_now}'"
      
      # Получаем вывод команды с удаленного сервера с помощью функции ssh_getout
      log_output = ssh_getout(data['ip'], data['username'], data['password'], command, data['port'])
      
      # Записываем полученный вывод в файл
      with open(file_name, "w") as f:
          f.write(log_output)



  def test_step0(self, time_now, data):
    # Получение данных из конфигурации
    remote_ip = data['ip']
    username = data['username']
    password = data['password']
    install_path = data['install_path']
    local_path = data['local_path']
    port = data['port']

    # Загружает файл на удаленный сервер и выполняет команды по установке пакета.
    res = []
    upload_files(remote_ip, username, password, local_path, install_path + "p7zip-full.deb", port=port)
    command_install = f"echo '{password}' | sudo -S dpkg -i {install_path}p7zip-full.deb"
    command_check = f"echo '{password}' | sudo -S dpkg -s p7zip-full"
    install_message = "Setting up"
    check_message = "Status: install ok installed"
    res.append(ssh_checkout(remote_ip, username, password, command_install, install_message))
    res.append(ssh_checkout(remote_ip, username, password, command_check, check_message))
    self.save_log(data,time_now, 'step0.txt')
    assert all(res)

  def test_step1(self, data,time_now):
    # Тест 1: Создание архива из содержимого папки folder_in.
    archive_type = data['archive_type']
    folder_in = data['folder_in']
    folder_out = data['folder_out']
    host = data['ip']
    user = data['username']
    passwd = data['password']
    port = data['port']
    archive_type = data.get('archive_type')  # Получаем тип архива из конфигурации
    command_create_archive = f"cd {folder_in}; 7z a {archive_type} {folder_out}/arx2 *"
    command_check_archive = f"ls {folder_out}"
    res1 = ssh_checkout(host, user, passwd, command_create_archive, "Everything is Ok", port)
    res2 = ssh_checkout(host, user, passwd, command_check_archive, "arx2.7z", port)
    self.save_log(data,time_now, 'step1')
    assert res1 and res2, "test1 FAIL"

  def test_step2(self, make_files, data, time_now):
      # Тест 2: Проверка наличия файлов внутри архива arx2.7z на удаленном сервере.
      res = []
      archive_command = f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx2 *"
      archive_result = ssh_checkout(data['ip'], data['username'], data['password'], archive_command, "Everything is Ok", data['port'])
      res.append(archive_result)

      extract_command = f"cd {data['folder_out']}; 7z e arx2.7z -o{data['folder_ext']} -y"
      extract_result = ssh_checkout(data['ip'], data['username'], data['password'], extract_command, "Everything is Ok", data['port'])
      res.append(extract_result)
      
      # Проверка наличия каждого файла в распакованной директории
      for item in make_files:
          check_file_command = f"ls {data['folder_ext']}"
          res.append(ssh_checkout(data['ip'], data['username'], data['password'], check_file_command, item, data['port']))
      
      self.save_log(data,time_now, 'step2')
      assert all(res), "test2 FAIL"


  def test_step3(self, data, time_now):
    # Тест 3: Проверка целостности архива на удаленном сервере.
    check_archive_command = f"cd {data['folder_out']}; 7z t arx2.7z"
    res = ssh_checkout(data['ip'], data['username'], data['password'], check_archive_command, "Everything is Ok", data['port'])
    
    self.save_log(data,time_now, 'step3')
    assert res, "test3 FAIL"

  def test_step4(self, data, time_now):
    # Тест 4: Проверка обновления содержимого архива на удаленном сервере.
    update_command = f"cd {data['folder_in']}; 7z u {data['folder_out']}/arx2.7z"
    res = ssh_checkout(data['ip'], data['username'], data['password'], update_command, "Everything is Ok", data['port'])

    self.save_log(data,time_now, 'step4')
    assert res, "test4 FAIL"

  def test_step5(self, make_files, data, time_now):
      # Тест 5: Проверка создания архива и его содержимого на удаленном сервере.
      res = []
      archive_command = f"cd {data['folder_in']}; 7z a {data['archive_type']} {data['folder_out']}/arx2 *"
      res.append(ssh_checkout(data['ip'], data['username'], data['password'], archive_command, "Everything is Ok", data['port']))

      # Получение списка файлов в архиве
      list_command = f"cd {data['folder_out']}; 7z l arx2.7z"
      list_output = ssh_getout(data['ip'], data['username'], data['password'], list_command, data['port'])
      for item in make_files:
          if item in list_output:
              res.append(True)
          else:
              res.append(False)

      self.save_log(data,time_now, 'step5')
      assert all(res), "test5 FAIL"




  def test_step6(self, make_files, data, time_now):
    # Тест 6: Проверка содержимого архива и извлечения файлов на удаленном сервере.
    res = []
    create_archive_command = f"cd {data['folder_in']}; 7z a {data['archive_type']} {data['folder_out']}/arx *"
    extract_command = f"cd {data['folder_out']}; 7z x arx.7z -o{data['folder_ext2']} -y"
    
    # Выполнение команд на удаленном сервере
    res.append(ssh_checkout(data['ip'], data['username'], data['password'], create_archive_command, "Everything is Ok", data['port']))
    res.append(ssh_checkout(data['ip'], data['username'], data['password'], extract_command, "Everything is Ok", data['port']))

    # Получение списка файлов в извлеченной папке
    list_files_command = f"ls {data['folder_ext2']}"
    list_files_output = ssh_getout(data['ip'], data['username'], data['password'], list_files_command, data['port'])
    extracted_files = list_files_output.split()

    # Проверка наличия каждого файла из списка make_files в извлеченной папке
    for expected_file in make_files:
        if expected_file in extracted_files:
            res.append(True)
        else:
            res.append(False)

    self.save_log(data,time_now, 'step6')
    assert all(res), "test6 FAIL"


  def test_step7(self, data, time_now):
    # Тест 7: Проверка удаления содержимого архива на удаленном сервере.
    remove_command = f"cd {data['folder_out']}; 7z d arx.7z"
    res = ssh_checkout(data['ip'], data['username'], data['password'], remove_command, "Everything is Ok", data['port'])

    self.save_log(data,time_now, 'step7')
    assert res, "test7 FAIL"


  def test_step8(self, make_files, data, time_now):
      # Тест 8: Проверка расчета хеша файлов и сравнение с выводом команды crc32
      res = []
      for item in make_files:
          # Выполнение команды для расчета хеша файла с помощью 7z
          hash_command = f"cd {data['folder_in']}; 7z h {item}"
          hash_command_output = ssh_getout(data['ip'], data['username'], data['password'], hash_command, data['port'])
          
          # Получение хеша командой crc32 и преобразование его в верхний регистр
          crc32_command = f"crc32 {data['folder_in']}/{item}"
          crc32_hash = ssh_getout(data['ip'], data['username'], data['password'], crc32_command, data['port']).strip().upper()

          # Сравнение хеша из 7z и crc32
          if crc32_hash in hash_command_output:
              res.append(True)
          else:
              res.append(False)

      self.save_log(data,time_now, 'step8')
      assert all(res), "test8 FAIL"


  def test_step9(self, time_now, data):
      # Удаляет файл с удаленного сервера и выполняет команды по удалению пакета.
      res = []
      # Получение данных из конфигурации
      remote_ip = data['ip']
      username = data['username']
      password = data['password']
      remote_path = data['install_path']
      local_path = data['local_path']
      port = data['port']

      upload_files(remote_ip, username, password, local_path, f"{remote_path}/p7zip-full.deb", port=port)
      remove_command = f"echo '{password}' | sudo -S dpkg -r p7zip-full"
      command_check = f"echo '{password}' | sudo -S dpkg -s p7zip-full"
      remove_message = "Removing"
      check_message = "Status: deinstall ok"
      res.append(ssh_checkout(remote_ip, username, password, remove_command, remove_message))
      res.append(ssh_checkout(remote_ip, username, password, command_check, check_message))
      self.save_log(data,time_now, 'step9')
      assert all(res)



# if __name__ == '__main__':
#  pytest.main['-vv']

#pytest -vv /Users/the_ryuk/Desktop/PythonCurse_2/Progect_linux_curse/progect.py

#pytest --alluredir=/Users/the_ryuk/Desktop/PythonCurse_2/results2 /Users/the_ryuk/Desktop/PythonCurse_2/Progect_linux_curse/progect.py
#allure serve /Users/the_ryuk/Desktop/PythonCurse_2/results2
