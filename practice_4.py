# 1. Solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "path Operation",
#     version = "1.0.1"
# )

# @app.get("/users/{user_id}")
# def user_id(user_id):
#     return {"message": f"The userid is : {user_id}"}


# 2. Solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "path Operation",
#     version = "1.0.1"
# )

# @app.get("/users/{product_id}")
# def user_id(product_id:int):
#     return {"message": f"The userid is : {product_id}"}


# 3. Solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "path Operation",
#     version = "1.0.1"
# )

# @app.get("/users/{product_id}")
# def user_id(product_id:int):
#     return {"message": f"The userid is : {product_id}"}

# 4. Solution


# from fastapi import FastAPI

# app = FastAPI(
#     title = "path Operation",
#     version = "1.0.1"
# )

# @app.get("/users/{user_id}/posts/{post_id}")
# def user_id(user_id:int, post_id: int):
#     return {"message": f"The product_id is : {user_id} and this is post_id: {post_id} "}


# 5. Solution

from fastapi import FastAPI
from uuid import UUID

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: UUID):
    return {"user_id": user_id}