# 1. Solution

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/search")
# def search(keyword: str):
#     return {
#         "keyword": keyword
#     }

# 2. Solution

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users")
# def search(keyword: str | None = None):
#     return {
#         "keyword": keyword
#     }


# 3. Solution

from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def get_products(limit: int = 10):
    return {
        "limit": limit
    }
