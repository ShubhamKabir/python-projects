import logging
import os

import config
import storage
import utils
from models import Client, Project

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def rebuild_data(raw_data):
    clients = []

    for c in raw_data:
        client = Client(c["name"])

        for p in c["projects"]:
            proj = Project(p["title"], p["price"])
            proj.completed = p.get("completed", False)
            client.projects.append(proj)

        clients.append(client)

    return clients


def display_clients(clients):
    for i, c in enumerate(clients):
        print(f"{i}. {c.name}")


def display_projects(client):
    for i, p in enumerate(client.projects):
        status = "✔" if p.completed else "✘"
        print(f"{i}. {p.title} - ₹{p.price} [{status}]")


def total_earnings(clients):
    total = 0
    for c in clients:
        for p in c.projects:
            if p.completed:
                total += p.price
    return total


def run():
    raw_data = storage.load_data(config.DATA_FILE)
    clients = rebuild_data(raw_data)

    logging.info("Freelance Manager started")

    while True:
        print("\n--- Freelance Manager ---")
        print("1. Add Client")
        print("2. Add Project")
        print("3. View Clients")
        print("4. View Projects")
        print("5. Complete Project")
        print("6. Total Earnings")
        print("7. Exit")

        try:
            choice = utils.get_number("Choose option: ")

            if choice == 1:
                name = utils.get_input("Client name: ")
                clients.append(Client(name))
                logging.info(f"Client added: {name}")

            elif choice == 2:
                display_clients(clients)
                idx = utils.get_number("Select client: ")
                title = utils.get_input("Project title: ")
                price = utils.get_number("Project price: ")

                clients[idx].add_project(Project(title, price))
                logging.info(f"Project added: {title}")

            elif choice == 3:
                display_clients(clients)

            elif choice == 4:
                display_clients(clients)
                idx = utils.get_number("Select client: ")
                display_projects(clients[idx])

            elif choice == 5:
                display_clients(clients)
                c_idx = utils.get_number("Select client: ")
                display_projects(clients[c_idx])
                p_idx = utils.get_number("Select project: ")

                clients[c_idx].projects[p_idx].complete()
                logging.info("Project marked complete")

            elif choice == 6:
                total = total_earnings(clients)
                print(f"Total Earnings: ₹{total}")

            elif choice == 7:
                storage.save_data(clients, config.DATA_FILE)
                print("Data saved. Goodbye!")
                break

        except ValueError as e:
            print(f"Error: {e}")
            logging.warning(str(e))

        except IndexError:
            print("Invalid selection")
            logging.error("Index error")

        except Exception as e:
            print("Unexpected error")
            logging.critical(str(e))


if __name__ == "__main__":
    run()