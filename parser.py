import requests
import json

# Отправляем GET-запрос на веб-сайт
url = 'https://m.mashina.kg/'
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Извлекаем JSON из ответа
    json_data = response.json()

    # Извлекаем нужную информацию из JSON
    name = json_data['name']
    brand = json_data['brand']
    color = json_data['color']
    image = json_data['image']
    description = json_data['description']
    production_date = json_data['productionDate']
    price = json_data['offers']['price']
    price_currency = json_data['offers']['priceCurrency']

    # Выводим извлеченные данные
    print("Name:", name)
    print("Brand:", brand)
    print("Color:", color)
    print("Image URL:", image)
    print("Description:", description)
    print("Production Date:", production_date)
    print("Price:", price, price_currency)
else:
    print("Ошибка при получении данных:", response.status_code)
