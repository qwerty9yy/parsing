# import requests
# from bs4 import BeautifulSoup

# # 1. Отправляем запрос на сайт
# url = 'http://localhost:8181/aznews/blog.html'
# response = requests.get(url)

# # 2. Проверяем статус ответа
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # 3. Ищем только нужные элементы
#     date_section = soup.find('a', class_='blog_item_date')
#     details_section = soup.find('div', class_='blog_details')
    
#     # 4. Извлекаем данные
#     if date_section and details_section:
#         # Дата
#         date_day = date_section.find('h3').text.strip()
#         date_month = date_section.find('p').text.strip()
#         date = f'({date_day} {date_month})'
        
#         # Заголовок
#         title = details_section.find('h2').text.strip()
        
#         # Текст новости
#         content = details_section.find('p').text.strip()
        
#         # Выводим результат
#         print(f"Дата: {date}")
#         print(f"Заголовок: {title}")
#         print(f"Текст новости: {content}")
#     else:
#         print("Не удалось найти элементы на странице.")
# else:
#     print("Ошибка! Код ответа:", response.status_code)