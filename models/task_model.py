class TaskModel:
    """Represents a collection of tasks stored in memory and persisted to a file."""

    def __init__(self, storage_path="tasks.json"):
        self.storage_path = storage_path
        self.tasks = []
        self.load()

    def load(self):
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                import json
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save(self):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            import json
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        self.save()

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()
