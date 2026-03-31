from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# Root
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

# Basic Routes
@app.get("/hello")
def hello():
    return {"message": "Hello Bondeth"}

@app.get("/about")
def about():
    return {"message": "About Page"}

@app.get("/users")
def findAllUsers():
    users = [{"id": 1, "name": "Bondeth"}, {"id": 2, "name": "John"}, {"id": 3, "name": "Jane"}]
    return users

# Parameter
@app.get("/user/{user_id}")
def findOneUser(user_id: int):
    return  {"user_id": user_id}

# Query Parameter
@app.get("/products")
def findAllProduct(limit: int = 5, page: int = 1):
    return {"limit": limit, "page": page}

@app.get("/user/{user_id}/posts")
def findUserPosts(user_id: int, limit: int = 10, page: int = 1, sort: str = "asc"):
    return {"user_id": user_id, "limit": limit, "page": page, "sort": sort}

# Optional Query Parameter
@app.get("/search")
def search(q: str = None):
    if q:
        return {"query": q}
    return {"message": "No query parameter provided"}

# Practice
@app.get("/product/{productId}")
def findOneProduct(productId: int):
    return { "title": "Product" ,"productId": productId}

@app.get("/keyword-search")
def search(keyword: Optional[str] = None):
   return { "keyword": keyword }