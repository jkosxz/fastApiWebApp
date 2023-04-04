import requests


class jsonPlaceHolderFetcher:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com"

    def end_point_status_code(self, endpoint):
        response = requests.get(self.url + endpoint)
        return response.status_code

    def fetch_json(self, endpoint):
        response = requests.get(self.url + f"{endpoint}")
        return response.content
