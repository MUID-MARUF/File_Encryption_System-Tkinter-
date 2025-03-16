from cryptography.fernet import Fernet
from key_manager import generate_or_load_key


def encrypt_file(file_path):
    """
    Encrypts the contents of a file and saves it as a new file with `.enc` extension.

    :param file_path: Path of the file to encrypt.
    :return: Path of the encrypted file.
    """
    key = generate_or_load_key()  # Load or generate the encryption key
    cipher = Fernet(key)

    # Read the original file data
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Encrypt the file data
    encrypted_data = cipher.encrypt(file_data)

    # Write the encrypted data to a new file
    encrypted_file_path = f"{file_path}.enc"
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)

    return encrypted_file_path


def decrypt_file(file_path):
    """
    Decrypts the contents of a `.enc` file and saves it as its original name.

    :param file_path: Path of the encrypted file.
    :return: Path of the decrypted file.
    """
    key = generate_or_load_key()  # Load or generate the encryption key
    cipher = Fernet(key)

    # Read the encrypted file data
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the file data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Derive the original file name (remove `.enc`)
    decrypted_file_path = file_path.replace(".enc", "")
    with open(decrypted_file_path, "wb") as file:
        file.write(decrypted_data)

    return decrypted_file_path
