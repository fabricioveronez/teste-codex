from controllers.task_controller import TaskController
from models.task_model import TaskModel
from views.task_view import TaskView


def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        command = input("Enter command (add/list/complete/delete/quit): ").strip()
        if command == "add":
            description = input("Task description: ")
            controller.add(description)
        elif command == "list":
            controller.list()
        elif command == "complete":
            try:
                index = int(input("Task number to complete: ")) - 1
                controller.complete(index)
            except ValueError:
                view.display_message("Invalid number.")
        elif command == "delete":
            try:
                index = int(input("Task number to delete: ")) - 1
                controller.delete(index)
            except ValueError:
                view.display_message("Invalid number.")
        elif command == "quit":
            break
        else:
            view.display_message("Unknown command.")


if __name__ == "__main__":
    main()
