class WebTaskController:
    """Controller used by the HTML interface."""

    def __init__(self, model):
        self.model = model

    def add(self, description):
        self.model.add_task(description)

    def list(self):
        return self.model.list_tasks()

    def complete(self, index):
        self.model.complete_task(index)

    def delete(self, index):
        self.model.delete_task(index)
