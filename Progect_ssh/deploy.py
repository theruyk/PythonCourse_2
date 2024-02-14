from checkers_ssh import ssh_checkout, upload_files

def deploy() -> bool:
    """
    Загружает файл на удаленный сервер и выполняет команды по установке пакета.
    Возвращает True, если все операции успешны, иначе False.
    """
    res = []

    # Вызов функции upload_files для загрузки файла на удаленный сервер через SFTP
    upload_files("89.104.68.41", "root", "TeimQvN9VxSOhb2g", "/Users/the_ryuk/Desktop/PythonCurse_2/Progect_linux_curse/p7zip-full.deb", "root@89.104.68.41:/Installer", port=22)
    #"0.0.0.0": IP-адрес удаленного сервера. 
    # "user2": Имя пользователя для аутентификации на удаленном сервере.
    # "11": Пароль для пользователя, используемого для аутентификации. 
    # "tests/p7zip-full.deb": Локальный путь к файлу, который вы хотите загрузить на сервер. 
    # "/home/user2/p7zip-full.deb": Путь на удаленном сервере, куда должен быть загружен файл. 
    # port=22: Порт, используемый для подключения к SFTP серверу.
    
    command_install = "echo '11' | sudo -S dpkg -i /home/user2/p7zip-full.deb"
    command_check = "echo '11' | sudo -S dpkg -s p7zip-full"
    install_message = "Настройка пакета"
    check_message = "Status: install ok installed"

    # Вызов функции ssh_checkout для выполнения команды установки пакета 
    # на удаленном сервере и добавление результата в список res
    res.append(ssh_checkout("0.0.0.0", "user2", "11", command_install, install_message))
    # Вызов функции ssh_checkout для проверки статуса установки и добавление результата в список res
    res.append(ssh_checkout("0.0.0.0", "user2", "11", command_check, check_message))

    return all(res)

if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
