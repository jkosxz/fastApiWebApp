from fastapi import FastAPI
import requests
from starlette.responses import FileResponse
import json

import post

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse('templates/index.html')

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/test/")
async def test():
    return testpost.test_func()

response = requests.get("https://jsonplaceholder.typicode.com/posts")
res = json.loads(response.content)


temp = dict(res[1])
testpost = post.Post(temp["userId"], temp["id"], temp["title"], temp["body"])

