import logging
import os

from tasks import Task
import storage
import utils
import config

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Setup logging
logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def rebuild_tasks(raw_data):
    tasks = []
    for t in raw_data:
        task = Task(t['title'])
        task.completed = t.get('completed', False)
        tasks.append(task)
    return tasks


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t.completed else "✘"
        print(f"{i}. {t.title} [{status}]")


def run_app():
    raw_data = storage.load_tasks(config.FILENAME)
    tasks = rebuild_tasks(raw_data)

    logging.info("Application started")

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = utils.get_choice()

            if choice == 1:
                title = utils.get_non_empty_input("Enter task title: ")
                tasks.append(Task(title))
                logging.info(f"Task added: {title}")

            elif choice == 2:
                display_tasks(tasks)

            elif choice == 3:
                display_tasks(tasks)
                idx = int(input("Enter task number: "))
                tasks[idx].complete()
                logging.info(f"Task completed: {tasks[idx].title}")

            elif choice == 4:
                display_tasks(tasks)
                idx = int(input("Enter task number to delete: "))
                removed = tasks.pop(idx)
                logging.info(f"Task deleted: {removed.title}")

            elif choice == 5:
                storage.save_tasks(tasks, config.FILENAME)
                print("Tasks saved. Goodbye!")
                logging.info("Application exited")
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print(f"Error: {e}")
            logging.warning(f"ValueError: {e}")

        except IndexError:
            print("Error: Invalid task number.")
            logging.error("IndexError: Invalid task index")

        except Exception as e:
            print("Unexpected error occurred.")
            logging.critical(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_app()