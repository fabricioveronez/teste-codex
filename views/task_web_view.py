from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory="templates")

class TaskWebView:
    """Render tasks to HTML pages."""

    def display_tasks(self, request: Request, tasks):
        return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})
