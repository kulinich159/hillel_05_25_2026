import requests

BASE_URL = "http://127.0.0.1:8080"
image_file = 'mars_photo1.jpg'
UPLOAD_FILE_URL = f"{BASE_URL}/upload"
IMAGE_URL = f"{BASE_URL}/image/{image_file}"
DELETE_IMAGE_URL = f"{BASE_URL}/delete/{image_file}"
headers_text = {'Content-Type': 'text'}
headers_image = {'Content-Type': 'image'}

# Завантаження зображення
with open(image_file, 'rb') as file:
    files = {'image': file}

    response = requests.post(UPLOAD_FILE_URL, files=files)

    if response.status_code == 201:
        response_data = response.json()
        image_url = response_data["image_url"]
        print(f"Файл було завантажено, він доступний за посиланням: {image_url}")
    else:
        print('Помилка при завантаженні:', response.status_code)

# Отримання інформації про завантажене зображення
response = requests.get(f"{IMAGE_URL}", headers=headers_text)

if response.status_code == 200:
    data = response.json()
    image_url = data["image_url"]
    print(f"Файл було знайдено за посиланням: {image_url}")
else:
    print('Помилка при отриманні даних:', response.status_code)


# Скачування зображення
response = requests.get(f"{IMAGE_URL}", headers=headers_image)
if response.status_code == 200:
    with open("test.jpg", "wb") as file:
        file.write(response.content)
    print("Зображення було скачано")
else:
    print("Помилка при скачуванні:", response.status_code)


# Видалення зображення
response = requests.delete(DELETE_IMAGE_URL)

if response.status_code == 200:
    data = response.json()
    print(data["message"])
else:
    print('Помилка при видаленні даних:', response.status_code)