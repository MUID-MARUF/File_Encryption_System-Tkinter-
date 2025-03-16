import os
from datetime import datetime


def initialize_log_file():
    """
    Initializes the log file if it doesn't already exist.
    """
    log_file = "logs.txt"
    if not os.path.exists(log_file):
        with open(log_file, "w") as file:
            header = f"Log File Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            header += "-" * 50 + "\n"
            file.write(header)


def log_action(action, file_name, status):
    """
    Logs an action performed (e.g., encryption/decryption) into the log file.

    :param action: The action being performed (e.g., "File Encryption").
    :param file_name: The file being acted on.
    :param status: The status of the action (e.g., "Success" or "Failed").
    """
    initialize_log_file()  # Ensure the log file exists
    log_file = "logs.txt"

    with open(log_file, "a") as file:
        # Write the log entry with a timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] Action: {action}, File: {file_name}, Status: {status}\n"
        file.write(log_entry)
