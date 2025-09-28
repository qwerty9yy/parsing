import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8181/resta/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tab_content = soup.find('div', class_='tab-pane fade')
    food_items = tab_content.find_all('div', class_='info')
    
    for item in food_items:
        name = item.find('h3').text.strip()
        description = item.find('p').text.strip()
        price = item.find('span').text.strip()
        
        print(f'Блюдо: {name}')
        print(f'Описание: {description}')
        print(f'Цена:  {price}')
        print('-' * 40)
else:
    print('Ошибка', response.status_code)