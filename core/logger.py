import datetime
import os

HISTORY_FILE = "data/action_history.log"


def log_action(action, websites):
    os.makedirs("data", exist_ok=True)

    with open(HISTORY_FILE, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {action}:\n")
        for site in websites:
            file.write(f"  - {site}\n")
        file.write("\n")
