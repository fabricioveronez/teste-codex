class TaskView:
    """Handles displaying information to the user."""

    def display_tasks(self, tasks):
        if not tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(tasks):
            status = "[x]" if task.get("completed") else "[ ]"
            print(f"{i + 1}. {status} {task.get('description')}")

    def display_message(self, message):
        print(message)
