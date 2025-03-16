import os
from cryptography.fernet import Fernet


def generate_or_load_key():
    """
    Generates a new key if needed or loads the existing one.
    """
    key_file = "key.key"

    # Check if the file exists
    if not os.path.exists(key_file):
        print("No encryption key file found. Generating a new one...")
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
        print(f"Encryption key file '{key_file}' has been created.")
    else:
        print(f"Encryption key file '{key_file}' already exists. Using the existing key.")

    # Load the key
    with open(key_file, "rb") as file:
        return file.read()
