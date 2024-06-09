import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import re

def read_item():
    for attempt in range(5):
        pyperclip.copy('')
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        time.sleep(0.1)
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        time.sleep(0.1)
        item_text = pyperclip.paste()
        if item_text.startswith("Item"):
            return item_text
        else:
            print(f"Attempt {attempt + 1}: Cursor not pointed at a valid item. Retrying...")
    print("Failed to read a valid item after 2 attempts. Please check the cursor placement and try again.")
    exit()

def get_item_name(item_text):
    return item_text.strip().split('\n')[2]

def extract_currency(item_text):
    # This regex looks for the pattern `~b/o` followed by one or more digits (`\d+`)
    # and then one or more word characters (`\w+`) which represent the currency type.
    match = re.search(r'~(b/o|price) (\d+) (\w+)', item_text)
    if match:
        # If a match is found, group 1 is the currency amount and group 2 is the currency type.
        currency_amount = int(match.group(2))
        currency_type = match.group(3)
        return currency_amount, currency_type
    else:
        return None, None