import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

load_dotenv()

IMAP_SERVER = os.getenv('SERVER')
EMAIL_ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')

search_word = 'XML-файл со статистикой'.lower()

# Подключаемся к серверу IMAP
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ACCOUNT, PASSWORD)

# Выбираем папку "Входящие"
mail.select('inbox')

# Ищем все письма
status, messages = mail.search(None, 'ALL')
if status == 'OK':
    for num in messages[0].split():
        # Получаем письмо
        status, msg_data = mail.fetch(num, '(RFC822)')
        if status == 'OK':
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    # Извлекаем заголовки
                    date = msg.get('Date')
                    subject = msg.get('Subject')
                    sender = msg.get('From')
                    
                    # Декодируем тему письма
                    if subject:
                        subject_decoded, encoding = decode_header(subject)[0]
                        if isinstance(subject_decoded, bytes):
                            subject_decoded = subject_decoded.decode(encoding or 'utf-8')
                        
                        # Ищем ключевое слово в теме
                        if search_word in subject_decoded.lower():
                            print(f'Дата: {date}')
                            print(f'Отправитель: {sender}')
                            print(f'Тема: {subject_decoded}')
                            
                            # Проверяем вложения
                            for part in msg.walk():
                                if part.get_content_disposition() == 'attachment':
                                    filename = part.get_filename()
                                    if filename:
                                        # Сохраняем файл
                                        with open(filename, 'wb') as f:
                                            f.write(part.get_payload(decode=True))
                                        print(f'Вложение сохранено: {filename}')
                                        
mail.logout()                                        