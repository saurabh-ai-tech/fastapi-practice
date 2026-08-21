# 1. Solution
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI(
#     title = "Request Body",
#     version= "1.0.0"
# )

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/user")
# def User_data(user: User):
#     return user


# 2. Solution
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI(
#     title = "Request Body",
#     version= "1.0.0"
# )

# class Products(BaseModel):
#     name: str
#     price: float
#     in_stock: bool

# @app.post("/products")
# def product_data(product: Products):
#     return product

# 3. Solution

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int | None = None
    city: str | None = None


@app.post("/users")
def create_user(user: User):
    return user








