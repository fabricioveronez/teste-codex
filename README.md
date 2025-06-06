# To-Do List Application

This is a simple web-based to-do list application implemented in Python using FastAPI and the MVC architecture.

## Usage

Run the application with:

```bash
uvicorn main:app --reload
```

Open your browser at `http://localhost:8000/` to use the web interface.

The API exposes the following endpoints:

- `POST /tasks` – Add a new task
- `GET /tasks` – List all tasks
- `PUT /tasks/{index}/complete` – Mark a task as completed
- `DELETE /tasks/{index}` – Delete a task
