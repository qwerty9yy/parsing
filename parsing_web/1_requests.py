import requests

# url = 'https://jsonplaceholder.typicode.com/posts/1' # Удаляем пост с ID=1
# response = requests.delete(url)

# print("Статус-код:", response.status_code) # Должно быть 200 или 204 (успех)

# url = 'https://jsonplaceholder.typicode.com/posts/1' # Обновляем пост с ID=1
# data = {
#     'id': 1, 
#     'title': 'Обновленный заголовок',
#     'body': 'Новый текст поста',
#     'userId': 1
# }
# response = requests.put(url, json=data)
# print('Статус-код:', response.status_code) # Должно быть 200
# print('Ответ сервера:', response.json())  # Выведет обновленный объект

# url = 'https://reqres.in/api/users'
# data = {
#     'name': 'morpheus',
#     'job': 'leader'
# }

# response = requests.post(url, json=data)
# print('Статус-код:', response.status_code)
# print('Ответ сервера:', response.json())

# url = 'https://api.genderize.io'
# params = {
#     'name': 'Саша'
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print(f"Имя {data['name']} вероятнее всего принадлежит {'мужчине' if data['gender'] == 'male' else 'женщине'} с вероятностью {data['probability']*100}%")
# else:
#     print('Ошибка:', response.status_code)
    

# url = 'https://catfact.ninja/fact'
# response = requests.get(url)

# if response.status_code == 200:
#     fact = response.json()
#     print("Факт о кошках:", fact['fact'])
# else:
#     print("Ошибка:", response.status_code)


# url = 'http://localhost:8181/anipat/about.html'
# data ={
#     'username': 'Иван',
#     'email': 'ivan@example.com',
#     'message': 'Привет! Это тестовое сообщение.'
# }

# response = requests.post(url, data=data)
# # Проверяем, как сервер ответил
# print('Статус-код:', response.status_code)
# print('Ответ сервера:', response.text[:500]) # Выведем первые 500 символов ответа


# response = requests.options('http://localhost:8181/anipat/about.html')
# print(response.headers.get('Allow'))

# response = requests.get('http://localhost:8181/anipat/about.html')

#print('Заголовки ответа:')
#for key, value in response.headers.items():
    #print(f'{key}: {value}')

# print('Статус-код:', response.status_code) # 200 - OK
# print("Тело ответа:", response.text) # Полный текст ответа
# print(response.status_code) # HTTP-код ответа (200 = успех)