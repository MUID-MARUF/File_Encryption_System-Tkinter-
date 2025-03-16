import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_module import encrypt_file, decrypt_file
from logger import log_action


# File selection for encryption
def browse_file_encrypt():
    """
    Opens a file dialog for selecting a file to encrypt.
    """
    return filedialog.askopenfilename(filetypes=[("Text and RTF files", "*.txt *.rtf")])


# File selection for decryption
def browse_file_decrypt():
    """
    Opens a file dialog for selecting a file to decrypt.
    """
    return filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])


# Encrypt File button action
def on_encrypt():
    """
    Handles the "Encrypt File" button click event.
    """
    try:
        file_path = browse_file_encrypt()
        if file_path:
            encrypted_file = encrypt_file(file_path)
            log_action("File Encryption", file_path, "Success")
            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {encrypted_file}")
    except Exception as e:
        log_action("File Encryption", file_path, f"Failed: {str(e)}")
        messagebox.showerror("Error", f"Failed to encrypt file: {str(e)}")


# Decrypt File button action
def on_decrypt():
    """
    Handles the "Decrypt File" button click event.
    """
    try:
        file_path = browse_file_decrypt()
        if file_path:
            decrypted_file = decrypt_file(file_path)
            log_action("File Decryption", file_path, "Success")
            messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {decrypted_file}")
    except Exception as e:
        log_action("File Decryption", file_path, f"Failed: {str(e)}")
        messagebox.showerror("Error", f"Failed to decrypt file: {str(e)}")


# Main GUI creation
def create_gui():
    """
    Creates the main graphical interface for the encryption/decryption system.
    """
    # Create the main window
    window = tk.Tk()
    window.title("File Encryption and Decryption System")
    window.configure(bg="darkblue")  # Set background color for the window
    window.geometry("500x400")  # Set the window size

    # Add GUI title
    title_label = tk.Label(window, text="File Encryption & Decryption", font=("Arial", 16, "bold"), bg="darkblue",
                           fg="white")
    title_label.pack(pady=20)

    # Add Encrypt File button
    encrypt_button = tk.Button(
        window,
        text="Encrypt File",
        command=on_encrypt,
        bg="white",
        fg="black",
        font=("Arial", 12),
        width=20,
        height=2
    )
    encrypt_button.pack(pady=20)

    # Add Decrypt File button
    decrypt_button = tk.Button(
        window,
        text="Decrypt File",
        command=on_decrypt,
        bg="white",
        fg="black",
        font=("Arial", 12),
        width=20,
        height=2
    )
    decrypt_button.pack(pady=20)

    # Display the GUI
    window.mainloop()
