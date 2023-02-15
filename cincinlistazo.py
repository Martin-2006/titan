import keyboard
import os
import datetime
from pynput import mouse

def record_mouse_events():
    hely = os.path.join(os.path.dirname(__file__), 'eger.txt')

    with open(hely, "a") as f:

        def on_click(x, y, button, pressed):
            if pressed:
                ido = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{ido} - {button} clicked at ({x}, {y})\n")

        def on_scroll(x, y, dx, dy):
            ido = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{ido} - mouse scrolled at ({x}, {y})\n")
            
        with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
            while True:
                key = keyboard.read_key()
                if key == 'esc':
                    break
            listener.stop()

record_mouse_events()
