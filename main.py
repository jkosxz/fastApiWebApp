import json
from unittest.mock import MagicMock, patch

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.testclient import TestClient

from jsonPlaceHolderFetcher import jsonPlaceHolderFetcher

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

#
var = jsonPlaceHolderFetcher()
users = json.loads(var.fetch_json("/users"))

data = []
for user in users:
    d = dict(user)
    data.append(list(d.values()))

print(data)
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request})

@app.get("/users")
async def users(request: Request):
    return templates.TemplateResponse("users.html", {
        "request": request,
        "users": users,
        "data": data})
