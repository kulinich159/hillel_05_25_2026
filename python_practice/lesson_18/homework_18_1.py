import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"


response = requests.get(search_url, params=search_params)
response_data = response.json()
items = response_data["collection"]["items"]

nasa_ids = []
for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)
    if len(nasa_ids) == 2:
        break

pictures_urls = []
for nasa_id in nasa_ids:
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    response = requests.get(asset_url)
    asset_data = response.json()

    for file_url in asset_data["collection"]["items"]:
        url = file_url["href"]
        if url.endswith("orig.jpg"):
            pictures_urls.append(url)
            break
        elif url.endswith(".jpg"):
            pictures_urls.append(url)
            break

counter = 1
for picture_url in pictures_urls:

    response = requests.get(picture_url)
    with open(f"mars_photo{counter}.jpg", "wb") as file:
        file.write(response.content)
    counter +=1

    print(f"Зображення за посиланням {picture_url} було збережено")