from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#register a get endpoint

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI", "status": "success"}

@app.get("/about")
def about():
    return {
        "frameWork": "Fastapi",
        "purpose": "building REST api's"
    }

#dynamic endpoint (or) dynamic route (or) dynamic parameter
#/users/23 -> 23 is the user id (or) user number

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {
        "user_id" : user_id,
        "message": f"fetching user with id {user_id}"
    }

#greet/sukku

@app.get("/greet/{name}")
def greet(name:str):
    return {
        "name": name,
        "message" : f"Hello {name}, welcome to FastAPI"
    }

#query parameters -> pass the additional parameters
# #filtering, search

#/products?category=laptop
#/products 

##/products -> path parameters
##/products?category=laptop -> query parameters


#http://127.0.0.1:8000/products?category=laptop

@app.get("/products")
def get_products(category:str = "all"):
    return {
        "category": category,
        "message": f"fetching products in category {category}"
    }

#/search
#http://127.0.0.1:8000/search?keyword=python&limit=500 

@app.get("/search")
def search_product(keyword:str, limit: int = 10):
    return {
        "keyword": keyword,
        "limit": limit,
        "message": f"searching for '{keyword}' and limit is {limit}"
    }


#pyic -> data validation(python library)
# task REST apis

class Task(BaseModel):
    title : str
    completed : bool = False

tasks = []
#status_code -> 201,
#200 -> normally created, 200 -> created successfully,
#400 -> validation error, 404 -> not found, 500 -> internal server error

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    tasks.append(task)

    return {
        "message" : "Task created successfully",
        "task" : task
    }

@app.get("/tasks")
def get_tasks():

    return {
        "tasks": tasks
    }

@app.get("/tasks/{task_index}")
def get_single_task(task_index:int):
    return {
        "task":tasks[task_index]
    }

#put -> update the existing resource 
### update 
@app.put("/tasks/{task_index}")
def update_task(task_index:int, task:Task):
    tasks[task_index] = task
    return {
        "message": "Task updated successfully",
        "task": task
    }

#delete -> delete the existing resource
## delete

@app.delete("/tasks/{task_index}")
def delete_single_task(task_index:int):

    deleted_task = tasks.pop(task_index)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }