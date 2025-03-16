from gui import create_gui
from key_manager import generate_or_load_key

if __name__ == "__main__":
    # Ensure the key and log files are available before launching the GUI

    generate_or_load_key()

    create_gui()  # Start the GUI
