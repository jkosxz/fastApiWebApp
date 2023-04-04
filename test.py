from jsonPlaceHolderFetcher import jsonPlaceHolderFetcher
import json

var = jsonPlaceHolderFetcher()
print(var.end_point_status_code("/posts"))

print(type(var.fetch_json("/posts")))
a = json.loads(var.fetch_json("/posts"))

print(a[0])