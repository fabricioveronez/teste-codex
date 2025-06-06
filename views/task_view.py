class TaskView:
    """Handles formatting of responses."""

    def display_tasks(self, tasks):
        """Return the list of tasks to the client."""
        return tasks

    def display_message(self, message):
        """Return a simple message to the client."""
        return {"message": message}
