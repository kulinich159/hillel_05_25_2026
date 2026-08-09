import requests


class SwapiController:
    def __init__(self, url = "https://swapi.info/api/"):
        self.url = url

    def get_person(self, person_id):
        url = f"{self.url}people/{person_id}"

        return requests.get(url=url)

    def get_people(self):
        url = f"{self.url}people"

        return requests.get(url=url)