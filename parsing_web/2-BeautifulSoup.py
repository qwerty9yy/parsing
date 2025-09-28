# библиотека для HTTP-запросов (GET/POST и т.д.). Нужна, чтобы скачать HTML страницы.
import requests 
# парсер HTML. Он превращает строку HTML в структуру, по которой удобно искать теги.
from bs4 import BeautifulSoup

# ! адрес страницы, которую ты парсишь.
url = 'http://localhost:8181/resta/'

try:
    # ! некоторые сайты блокируют «пустой» User-Agent; 
    # ! поэтому мы имитируем обычный браузер. Это повышает вероятность корректного ответа.
    response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
    
    # ! Если ответ имеет код ошибки (4xx или 5xx), 
    # ! метод выбрасывает исключение requests.HTTPError. 
    # ! Это удобно — мы не продолжаем парсить страницу, если сервер вернул ошибку.
    response.raise_for_status()
    
    # базовый класс для всех исключений requests, в него входят Timeout, ConnectionError, HTTPError и т.д.
except requests.exceptions.RequestException as e:
    print('Ошибка при запросе:', e)
else:
    # дальше — только если ошибок не было
    
    # response.text — HTML-страница в виде строки.
    soup = BeautifulSoup(response.text, 'lxml')
    
    # Это CSS-селектор: ищет <div> элемент, 
    # у которого одновременно есть классы tab-pane и fade 
    # (то есть class="tab-pane fade" или class="fade tab-pane").
    tab_content = soup.select_one('div.tab-pane.fade')
    if not tab_content:
        print('Не найден контейнер tab-pane fade')
    else:
        food_items = tab_content.find_all('div', class_='info')
        for item in food_items:
            h3 = item.select_one('h3')
            name = h3.get_text(strip=True) if h3 else '-'
            
            p = item.select_one('p')
            description = p.get_text(strip=True) if p else '-'
            
            span = item.select_one('span')
            raw_price = span.get_text(strip=True) if span else '-'
            
            print(f'Блюдо: {name}')
            print(f'Описание: {description}')
            print(f'Цена (raw): {raw_price}')
            print('-' * 40)