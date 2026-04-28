import json
import logging

def save_data(expenses, filename):
    try:
        data = [e.__dict__ for e in expenses]

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Expenses saved")

    except Exception as e:
        logging.error(f"Save error: {e}")


def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("No data file found")
        return []