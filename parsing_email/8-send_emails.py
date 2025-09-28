import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

# Данные для подключения
IMAP_SERVER = os.getenv('SERVER')
EMAIL_ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')

# Создаем объект сообщения
msg = MIMEMultipart()
msg['From'] = EMAIL_ACCOUNT
msg['To'] = 'balezino2017@gmail.com'
msg['Subject'] = 'Тестовое письмо'

# Текст письма
body = 'Это тестовое письмо отправленное с помощью smtplib.'
msg.attach(MIMEText(body, 'plain'))

# Подключаемся к серверу SMTP
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()   # Используем TLS для безопасного соединения
server.login(EMAIL_ACCOUNT, PASSWORD)

# Отправляем письмо
server.sendmail(EMAIL_ACCOUNT, 'balezino2017@gmail.com', msg.as_string())

# Закрываем соединение с сервером
server.quit()

print("Письмо отправлено успешно.")