import threading
import tkinter as tk
from pynput.mouse import Listener
import subprocess
import pyautogui
import pygetwindow as gw
import time

# Open the Calculator app
# subprocess.Popen(['open', '-a', 'PathOfExileClient'])

# Wait for the app to open
# time.sleep(5)

# Get a reference to the Calculator window
app_name = "PathOfExileClient"
cmd = f'osascript -e \'activate application "{app_name}"\''
subprocess.call(cmd, shell=True)

# Bring the Calculator window to the forefront


def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at position: ({x}, {y})")


def on_move(x, y):
    popup_label.config(text=f"Mouse position: ({x}, {y})")
    popup.update_idletasks()
    popup.geometry(f"+{int(x) + 20}+{int(y) + 20}")


def start_listener():
    with Listener(on_click=on_click, on_move=on_move) as listener:
        listener.join()


popup = tk.Tk()
popup.overrideredirect(1)  # Remove window decorations
popup.attributes('-topmost', 1)  # Keep the popup on top
popup.geometry('+500+500')  # Initialize popup position

popup_label = tk.Label(popup, text="Mouse position")
popup_label.pack()

listener_thread = threading.Thread(target=start_listener)
listener_thread.start()


popup.mainloop()
