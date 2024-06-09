import pyautogui
import pyperclip
import re
from trade.constants import DIVINE_RATIO

TRADE_WINDOW_TL = (251.046875, 217.50390625)
TRADE_WINDOW_BR = (723.0, 413.54296875)
TRADE_WINDOW_CELL_SIZE = (TRADE_WINDOW_BR[0] - TRADE_WINDOW_TL[0]) / 12

def verify_payment(total_in_d):
    total_c = 0
    total_d = 0
    total_given = 0
    for row in range(5):
        for col in range(12):
            try:
                pyautogui.PAUSE = 0.005
                pyautogui.moveTo(TRADE_WINDOW_TL[0] + 15 +col*TRADE_WINDOW_CELL_SIZE,
                                    TRADE_WINDOW_TL[1] + 15 +row*TRADE_WINDOW_CELL_SIZE)
                pyautogui.keyDown('CTRL')
                pyautogui.press('C')
                pyautogui.keyUp('CTRL')
                clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ')
                currency_data = re.match(
                    '.+Rarity: \w+ - (.+) - -+ - Stack Size: (\d+).+', clipboard_data)
                if(currency_data):
                    cell_currency = currency_data.group(1)
                    cell_amount = int(currency_data.group(2))
                    pyperclip.copy('')
                    if cell_currency == "Divine Orb":
                        total_d += cell_amount
                    elif cell_currency == "Chaos Orb":
                        total_c += cell_amount
                total_given = total_d + total_c / DIVINE_RATIO
            except Exception as e:
                pass
    pyautogui.PAUSE = 0.05
    if total_given >= total_in_d:
        return True
    else:
        return False

