import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import subprocess

# Указываем путь к файлу тестов
test_file_path = '/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_crossbrowser/test_1.py'

# Запускаем pytest с указанным файлом и сохраняем отчет в report.xml: python send_report.py
subprocess.run(['pytest', test_file_path, '--junitxml=report.xml'])

# Установите ваш реальный адрес электронной почты и пароль
fromaddr = "vano95-cokol@mail.ru"
toaddr = "vano95-cokol@mail.ru"
mypassword = "BH1xJr1ynSvDEhgbsZd0" 

# Указываете имя файла отчета
reportname = "report.xml"

# Создание объекта сообщения
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Отчет о тестировании"

# Текст сообщения
body = "В приложении находится отчет о последних тестах."
msg.attach(MIMEText(body, 'plain'))

# Добавление файла в виде вложения
with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
msg.attach(part)

# Настройка сервера
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypassword)

# Отправка сообщения
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
