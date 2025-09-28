import imaplib
import os
from dotenv import load_dotenv

load_dotenv()

IMAP_SERVER = os.getenv('SERVER')
EMAIL_ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')

# Устанавливаем соединение с почтовым сервером
mail = imaplib.IMAP4_SSL(IMAP_SERVER)

mail.login(EMAIL_ACCOUNT, PASSWORD)

mail.select('Trash') # Выбираем папку

# Получаем все письма в папке
status, response = mail.search(None, 'ALL') # Ищем все письма
if status == 'OK':
    email_ids = response[0].split() # Список ID всех писем
    
    print(f"Найдено писем: {len(email_ids)}")
    
    for email_id in email_ids:
        # Удаляем флаг \Seen (помечаем как непрочитанное)
        mail.store(email_id, '-FLAGS', '\\Seen')
        print(f"Письмо {email_id.decode()} помечено как непрочитанное.")
        

# Закрываем соединение
mail.logout()