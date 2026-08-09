import requests

from core.api.swapi.swapi_controller import SwapiController

responce = requests.get(url= f"{SwapiController().url}people/1")

status_code = responce.status_code
text = responce.text
headers = dict(responce.headers)

responce_json = responce.json()

print("status_code:", status_code)
print("text:", text)
print("headers:", headers)
print("responce_json:", responce_json)

print(responce_json.get("name"))
