import json
import logging

def save_data(clients, filename):
    try:
        data = []
        for c in clients:
            client_data = {
                "name": c.name,
                "projects": [
                    {
                        "title": p.title,
                        "price": p.price,
                        "completed": p.completed
                    }
                    for p in c.projects
                ]
            }
            data.append(client_data)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Data saved successfully")

    except Exception as e:
        logging.error(f"Error saving data: {e}")


def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("No existing data file found")
        return []