import threading
import tkinter as tk
from pynput.mouse import Listener, Button
import subprocess
import pyautogui
import pygetwindow as gw
import time


app_name = "PathOfExileClient"
cmd = f'osascript -e \'activate application "{app_name}"\''
subprocess.call(cmd, shell=True)



def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.left:
            try:
                # item_name = read_name()
                # print(item_name)
                print(f"Mouse clicked at position: ({x}, {y})")
            except Exception as e:
                print(f"Mouse clicked at position: ({x}, {y})")
            
        else:
            popup.quit()
            exit()



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
