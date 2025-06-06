class TaskController:
    """Controller that mediates between model and view."""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add(self, description):
        self.model.add_task(description)
        return self.view.display_message("Task added.")

    def list(self):
        tasks = self.model.list_tasks()
        return self.view.display_tasks(tasks)

    def complete(self, index):
        self.model.complete_task(index)
        return self.view.display_message("Task completed.")

    def delete(self, index):
        self.model.delete_task(index)
        return self.view.display_message("Task deleted.")
