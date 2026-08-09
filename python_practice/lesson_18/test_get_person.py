import unittest
import requests

from core.api.swapi.swapi_controller import SwapiController

swapi_controller = SwapiController()

class TestPerson(unittest.TestCase):

    def test_get_person(self):
        person_id = 1
        responce = swapi_controller.get_person(person_id)

        self.assertEqual(200, responce.status_code)

    def test_get_people(self):
        responce = swapi_controller.get_people()

        self.assertEqual(200, responce.status_code)