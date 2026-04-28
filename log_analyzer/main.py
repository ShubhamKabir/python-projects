import logging
import os
import sys

from analyzer import LogAnalyzer
import utils
import config

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def write_report(report):
    with open(config.REPORT_FILE, "w") as f:
        f.write(report)


def run():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Usage: python main.py <logfile>")

        filename = utils.validate_file(sys.argv[1])

        lines = read_file(filename)

        analyzer = LogAnalyzer()
        analyzer.analyze(lines)

        report = analyzer.get_report()
        print("\n--- Report ---")
        print(report)

        write_report(report)

        logging.info(f"Analyzed file: {filename}")

    except FileNotFoundError:
        print("Error: File not found")
        logging.error("File not found")

    except ValueError as e:
        print(f"Error: {e}")
        logging.warning(str(e))

    except Exception as e:
        print("Unexpected error occurred")
        logging.critical(str(e))


if __name__ == "__main__":
    run()