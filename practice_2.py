# 1. Solution
# from fastapi import FastAPI
# app = FastAPI()

# 2. Solution 
# from fastapi import FastAPI
# app  = FastAPI(
#     title = "My First API",
# )

# 3. Solution
# from fastapi import FastAPI
# app = FastAPI(
#     title = "Student API",
#     version= 1.0.0
# )

# 4. Solution
# from fastapi import FastAPI
# app = FastAPI(
#     title = "Book A.P.I",
#     version="1.0.0"
#     description= "This API manages books."
# )

# 5. Solution 

# from fastapi import FastAPI

# app = FastAPI(
#     title="User API",
#     version="1.0.0",
#     description="API for managing users."
# )

# @app.get("/")
# def display_users():
#     return "this is any api for managing users"


# 6 Solution
# from fastapi import FastAPI

# app = FastAPI(
#     title = "my api",
#     docs_url= "/api/docs"
# )


# 7 Solution

from fastapi import FastAPI

app = FastAPI(
    title="E-Commerce API",
    version="2.0.0",
    description="API for managing products and orders.",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

