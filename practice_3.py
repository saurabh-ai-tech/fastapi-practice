# 1. Solution 

# from fastapi import FastAPI

# app = FastAPI(
#     title = "practice api",
#     description = "this is for practicing purposes",
#     version = "1.0.0",
#     )

# @app.get("/")
# def display_msg():
#     return {"message": "Hello, FastAPI"}



# 2. Solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "user",
#     version = "1.0.0"
# )

# @app.get("/users")
# def users():
#     return {"message":"getting all users"}


# 3. Solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "user",
#     version = "1.0.0"
# )

# @app.post("/users")
# def users():
#     return {"message":"users created successfully"}

# 4. Solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "user",
#     version = "1.0.0"
# )

# @app.put("/users")
# def users():
#     return {"message":"users updated successfully"}


# 5. Solution

# from fastapi import FastAPI
# app = FastAPI(
#     title = "user",
#     version = "1.0.0"
# )

# @app.delete("/users")
# def users():
#     return {"message":"users deleted successfully"}

# 6 Solution 

# from fastapi import FastAPI
# app = FastAPI(
#     title = "user",
#     version = "1.0.0"
# )

# @app.patch("/users")
# def users():
#     return {"message":"users partially updated"}

# # 7 solution

# from fastapi import FastAPI

# app = FastAPI(
#     title = "practice get post",
#     version = "1.0.0"
# )

# @app.get("/users")
# def users():
#     return {"message": "This is getting all the users"}

# @app.post("/users")
# def users():
#     return {"message": "This is creating the users"}


# 8. Solution
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/1")
def get_user():
    return {"message": "Getting user 1"}


@app.put("/users/1")
def update_user():
    return {"message": "Completely updating user 1"}


@app.patch("/users/1")
def partial_update_user():
    return {"message": "Partially updating user 1"}


@app.delete("/users/1")
def delete_user():
    return {"message": "Deleting user 1"}