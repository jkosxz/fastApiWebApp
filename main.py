from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jsonPlaceHolderFetcher import jsonPlaceHolderFetcher

app = FastAPI()
jsonFetcher = jsonPlaceHolderFetcher()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("layout.html", {"request": request})


@app.get("/users")
async def users(request: Request):
    return templates.TemplateResponse("users.html", {
        "request": request,
        "data_users": jsonFetcher.fetch_data("/users")})


@app.get("/posts")
async def posts(request: Request):
    return templates.TemplateResponse("posts.html", {
        "request": request,
        "data_posts": jsonFetcher.fetch_data("/posts"),

    })

@app.get("/mainpage")
async def mainpage(request: Request):
    return templates.TemplateResponse("mainpage.html", {
        "request": request,
        "data_posts": jsonFetcher.fetch_data("/posts")[0: 11],
        "data_comments": jsonFetcher.fetch_data("/comments"),
        "data_users": jsonFetcher.fetch_data("/users"),
        "posts_count": 10

    })
@app.get("/mainpage/{num}")
async def mainpage_p(request: Request, num: int):
    return templates.TemplateResponse("mainpage.html", {
        "request": request,
        "data_posts": jsonFetcher.fetch_data("/posts")[num*10: num*10+11],
        "data_comments": jsonFetcher.fetch_data("/comments"),
        "data_users": jsonFetcher.fetch_data("/users"),

    })

@app.get("/mainpage/post/{postid}")
async def mainpage_post(request: Request, postid: int):
    return templates.TemplateResponse("singlepost.html", {
        "request": request,
        "data_posts": jsonFetcher.fetch_data("/posts")[postid - 1],
        "data_comments": jsonFetcher.fetch_data("/comments"),
        "data_users": jsonFetcher.fetch_data("/users"),
        "postid": postid

    })