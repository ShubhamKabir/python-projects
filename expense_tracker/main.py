import logging
import os

import config
import storage
import utils
from models import Expense

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def rebuild_data(raw_data):
    expenses = []
    for e in raw_data:
        expenses.append(
            Expense(e["title"], e["amount"], e["category"])
        )
    return expenses


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for i, e in enumerate(expenses):
        print(f"{i}. {e.title} - ₹{e.amount} ({e.category})")


def total_expense(expenses):
    return sum(e.amount for e in expenses)


def category_summary(expenses):
    summary = {}

    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount

    return summary


def run():
    raw_data = storage.load_data(config.DATA_FILE)
    expenses = rebuild_data(raw_data)

    logging.info("Expense Tracker started")

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")

        try:
            choice = utils.get_number("Choose option: ")

            if choice == 1:
                title = utils.get_input("Expense title: ")
                amount = utils.get_number("Amount: ")
                category = utils.get_input("Category: ")

                expenses.append(Expense(title, amount, category))
                logging.info(f"Expense added: {title}")

            elif choice == 2:
                display_expenses(expenses)

            elif choice == 3:
                print(f"Total: ₹{total_expense(expenses)}")

            elif choice == 4:
                summary = category_summary(expenses)
                for cat, amt in summary.items():
                    print(f"{cat}: ₹{amt}")

            elif choice == 5:
                storage.save_data(expenses, config.DATA_FILE)
                print("Saved. Goodbye!")
                break

        except ValueError as e:
            print(f"Error: {e}")
            logging.warning(str(e))

        except Exception as e:
            print("Unexpected error")
            logging.critical(str(e))


if __name__ == "__main__":
    run()