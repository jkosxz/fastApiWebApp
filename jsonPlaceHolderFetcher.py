import json

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

    def fetch_posts(self):
        data_users = []
        for user in json.loads(self.fetch_json("/posts")):
            dict_users = dict(user)
            data_users.append(list(dict_users.values()))
        return data_users

    def fetch_users(self):
        data_posts = []
        for user in json.loads(self.fetch_json("/users")):
            dict_users = dict(user)
            data_posts.append(list(dict_users.values()))
        return data_posts
