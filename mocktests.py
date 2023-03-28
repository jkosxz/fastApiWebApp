import unittest
from unittest.mock import patch, MagicMock, Mock
import requests
from starlette.testclient import TestClient

import main


class jsonPlaceHolderFetcher:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com"

    def connectToEndpoint(self, endpoint):
        response = requests.get(self.url + endpoint)
        return response.status_code

    def fetch_json(self, endpoint):
        response = requests.get(self.url + f"{endpoint}")
        return response.json()

    def test(self, endpoint):
        response = requests.get("https://jsonplaceholder.typicode.com" + endpoint)
        return response.status_code


def test_api_call():
    real = jsonPlaceHolderFetcher()
    real.connectToEndpoint = MagicMock(name="connectToEndpoint")
    real.connectToEndpoint.return_value.status_code = 200

    with patch("requests.get", real):
        data = real.connectToEndpoint("/").status_code

    assert data == 200
