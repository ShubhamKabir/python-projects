import json
import logging

def save_tasks(tasks, filename):
    try:
        data = [t.__dict__ for t in tasks]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Saved {len(tasks)} tasks.")
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")


def load_tasks(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("No existing task file found.")
        return []