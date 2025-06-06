from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel

from controllers.task_controller import TaskController
from controllers.web_task_controller import WebTaskController
from models.task_model import TaskModel
from views.task_view import TaskView
from views.task_web_view import TaskWebView

app = FastAPI()

model = TaskModel()
view = TaskView()
controller = TaskController(model, view)
web_view = TaskWebView()
web_controller = WebTaskController(model)

class TaskCreate(BaseModel):
    description: str

@app.post("/tasks")
def add_task(task: TaskCreate):
    return controller.add(task.description)

@app.get("/tasks")
def list_tasks():
    return controller.list()

@app.put("/tasks/{index}/complete")
def complete_task(index: int):
    return controller.complete(index)

@app.delete("/tasks/{index}")
def delete_task(index: int):
    return controller.delete(index)


# Web interface routes

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    tasks = web_controller.list()
    return web_view.display_tasks(request, tasks)


@app.post("/add")
def add_task_form(description: str = Form(...)):
    web_controller.add(description)
    return RedirectResponse("/", status_code=303)


@app.post("/complete/{index}")
def complete_task_form(index: int):
    web_controller.complete(index)
    return RedirectResponse("/", status_code=303)


@app.post("/delete/{index}")
def delete_task_form(index: int):
    web_controller.delete(index)
    return RedirectResponse("/", status_code=303)
