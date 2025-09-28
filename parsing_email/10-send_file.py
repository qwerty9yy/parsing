import smtplib # библиотека для отправки писем через SMTP.
# модули для работы с письмами (текст, вложения, кодировка).
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()

# Данные для отправки
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
TO_EMAIL = os.getenv('ACCOUNT')

# Создаем сообщение
msg = MIMEMultipart() # объект письма, куда можно прикрепить и текст, и файлы.
# ! В заголовки добавляем отправителя, получателя и тему.
msg['From'] = EMAIL_ACCOUNT
msg['To'] = TO_EMAIL
msg['Subject'] = "XML-файл со статистикой"

# Текст письма
body = "Во вложении находится XML-файл со статистикой."
msg.attach(MIMEText(body, 'plain'))

# Прикрепляем файл
filename = 'statistics.xml'

with open(filename, 'rb') as attachment: # открывает файл в бинарном режиме (rb = read binary).
    part = MIMEBase('application', 'octet-stream') # объект для файловых вложений.
    part.set_payload(attachment.read()) # загружаем содержимое файла.
    encoders.encode_base64(part) # кодируем файл в base64 (чтобы корректно пересылался).
    # указываем имя файла во вложении.
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}'
    )
    msg.attach(part) # прикрепляем его к письму.
    
# Отправка письма
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) # подключаемся к серверу.
server.starttls() # включаем защищенное соединение.
server.login(EMAIL_ACCOUNT, PASSWORD)
server.send_message(msg)    # отправляем письмо.
server.quit()

print("Письмо с XML-файлом отправлено.")