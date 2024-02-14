import paramiko

def ssh_checkout(host: str, user: str, passwd: str, cmd: str, text: str, port: int = 22) -> bool:
    """
    Выполняет команду на удаленном сервере, проверяет наличие заданного текста в выводе
    и возвращает True, если текст найден и команда завершилась с кодом 0 (успешно).

    :param host: IP-адрес или хостнейм удаленного сервера.
    :param user: Имя пользователя для подключения по SSH.
    :param passwd: Пароль для подключения по SSH.
    :param cmd: Команда для выполнения на удаленном сервере.
    :param text: Текст, который ожидается найти в выводе команды.
    :param port: Порт SSH для подключения, по умолчанию 22.
    :return: True, если указанный текст найден в выводе и команда завершилась успешно, иначе False.
    """
    # Создание нового SSH клиента
    client = paramiko.SSHClient()
    
    # Автоматически добавляет отсутствующий ключ хоста без предварительной проверки
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Устанавливает соединение с SSH сервером
    client.connect(hostname=host, username=user, password=passwd, port=port)
    
    # Выполнение команды на удаленном сервере и получение трех потоков ввода/вывода
    stdin, stdout, stderr = client.exec_command(cmd)
    
    # Получение кода завершения выполненной команды
    exit_code = stdout.channel.recv_exit_status()
    
    # Чтение стандартного вывода и стандартного вывода ошибок, декодирование в UTF-8
    out = (stdout.read() + stderr.read()).decode("utf-8")
    
    # Закрытие клиента SSH
    client.close()
    
    # Возвращает True, если текст присутствует в выводе и команда завершилась с кодом 0
    return text in out and exit_code == 0


def upload_files(host: str, user: str, passwd: str, local_path: str, 
    remote_path: str, port: int = 22) -> None:
    """Загружает файл с локальной машины на удаленный сервер."""
    # Вывод информационного сообщения о начале загрузки файла
    print(f"Загружаем файл {local_path} в каталог {remote_path}")

    # Создание объекта Transport для установления соединения с сервером
    transport = paramiko.Transport((host, port))

    # Установление соединения, используя предоставленные учетные данные пользователя
    transport.connect(None, username=user, password=passwd)

    # Создание клиента SFTP через установленное транспортное соединение
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Загрузка файла из локального пути в удаленный путь на сервере
    sftp.put(local_path, remote_path)

    # Закрытие клиента SFTP, если он был успешно создан
    if sftp:
        sftp.close()

    # Закрытие транспортного соединения, если оно было установлено
    if transport:
        transport.close()


def download_files(
        host: str, user: str, passwd: str, remote_path: str, local_path: str,
        port: int = 22) -> None:
    """Скачивает файл с удаленного сервера по SFTP.

    :param host: IP-адрес или хостнейм удаленного сервера
    :param user: Имя пользователя для подключения
    :param passwd: Пароль пользователя
    :param remote_path: Путь к файлу на удаленном сервере
    :param local_path: Путь для сохранения файла локально
    :param port: Порт SSH для подключения
    """
    print(f"Скачиваем файл {remote_path} в каталог {local_path}")

    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remote_path, local_path)
    
    sftp.close()
    transport.close()


def ssh_checkout_negative(
        host: str, user: str, passwd: str, cmd: str, text: str, port: int = 22) -> bool:
    """Выполняет команду на удаленном сервере и проверяет наличие текста в выводе.

    :param host: IP-адрес или хостнейм удаленного сервера
    :param user: Имя пользователя для подключения
    :param passwd: Пароль пользователя
    :param cmd: Команда для выполнения
    :param text: Текст для поиска в выводе команды
    :param port: Порт SSH для подключения
    :return: True, если текст найден и код завершения команды не 0
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=passwd, port=port)

    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    output = (stdout.read() + stderr.read()).decode('utf-8')

    client.close()
    return text in output and exit_code != 0


def ssh_getout(host: str, user: str, passwd: str, cmd: str, port: int = 22) -> str:
    """
    Выполняет команду на удаленном сервере и возвращает ее вывод.

    :param host: IP-адрес или хостнейм удаленного сервера.
    :param user: Имя пользователя для подключения по SSH.
    :param passwd: Пароль для подключения по SSH.
    :param cmd: Команда для выполнения на удаленном сервере.
    :param port: Порт SSH для подключения, по умолчанию 22.
    :return: Вывод выполнения команды на удаленном сервере.
    """
    # Создание клиента SSH
    client = paramiko.SSHClient()
    # Автоматическое добавление ключа хоста, если он отсутствует в known_hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение к удаленному серверу
    client.connect(hostname=host, username=user, password=passwd, port=port)
    # Выполнение команды и получение потоков ввода/вывода
    stdin, stdout, stderr = client.exec_command(cmd)
    # Чтение и декодирование вывода команды
    output = (stdout.read() + stderr.read()).decode('utf-8')
    # Закрытие клиента SSH
    client.close()
    # Возврат вывода команды
    return output
