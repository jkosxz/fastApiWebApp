import json
import requests


class jsonPlaceHolderFetcher:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com"

    def end_point_status_code(self, endpoint):
        response = requests.get(self.url + endpoint)
        return response.status_code

    def __fetch_json(self, endpoint):
        response = requests.get(self.url + f"{endpoint}")
        return response.content

    def fetch_data(self, endpoint):
        data = []
        for item in json.loads(self.__fetch_json(f"{endpoint}")):
            dict_items = dict(item)
            data.append(list(dict_items.values()))
        return data


