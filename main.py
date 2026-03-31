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