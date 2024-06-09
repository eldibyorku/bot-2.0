import pyautogui
import time

STASH_LOCATION = (681.140625, 411.0859375)
SALE_TABS={
     "~b/o 10 divine": {
        "location": (357.859375, 150.609375),
        "type": "quad",
        "default_price": 10,
        "default_currency": "divine"
    },
    "~price 4 divine": {
        "location": (585.5390625, 500.25390625),
        "type": "quad",
        "default_price": 4,
        "default_currency": "divine"
    },

    "~b/o 2 divine": {
        "location": (583.98828125, 250.42578125),
        "type": "quad",
        "default_price": 2,
        "default_currency": "divine"
    },

    "~b/o 1 divine": {
        "location": (584.12890625, 236.2734375),
        "type": "quad",
        "default_price": 1,
        "default_currency": "divine"
    },

    "Sale 1": {
        "location": (570.33203125, 374.55859375),
        "type": "regular"
    },

    "Sale 2": {
        "location": (566.19140625, 394.52734375),
        "type": "regular"
    },

    "Beasts": {
        "location": (568.69140625, 427.75),
        "type": "regular"
    }
}


REG_TL = (13.5859375, 161.609375)
REG_BR = (481.8046875, 630.12890625)

INV_TL = (988.8359375, 505.5859375)
INV_BR = (1458.9453125, 698.83984375)
INV_WIDGTH = (INV_BR[0] - INV_TL[0]) / 12

def go_to_inv():
    pyautogui.moveTo(INV_TL[0] + 20, INV_TL[1] + 20, 0.1)

def go_to_item(tab, pos_left, pos_top):
    stash_tab = SALE_TABS[tab]
    open_stash()
    go_to_tab(stash_tab["location"] )
    if stash_tab["type"] == "quad":
        find_in_quad(pos_left, pos_top)
    elif stash_tab["type"] == "regular":
        find_in_reg(pos_left, pos_top)

def open_stash():
    try:
        pyautogui.locateOnScreen('trade/stash.png')
        return
    except pyautogui.ImageNotFoundException:
        pyautogui.press('Space')
        pyautogui.moveTo(STASH_LOCATION[0], STASH_LOCATION[1], 0.1)
        pyautogui.click()
        time.sleep(1)

def go_to_tab(location):
    pyautogui.moveTo(location[0], location[1], 0.1)
    pyautogui.click()

def find_in_quad(left, top):
    width = (REG_BR[0] - REG_TL[0]) / 24
    x = REG_TL[0] + (left - 0.5) * width
    y = REG_TL[1] + (top - 0.5) * width
    print("in quad")
    print(x, y)
    pyautogui.moveTo(x,y,0.1)

def find_in_reg(left, top):
    width = (REG_BR[0] - REG_TL[0]) / 12
    x = REG_TL[0] + (left - 0.5) * width
    y = REG_TL[1] + (top - 0.5) * width
    print("in reg")
    print(x, y)
    pyautogui.moveTo(x,y,0.1)

def extract_currency_from_tab(tab):
    stash_tab = SALE_TABS[tab]
    default_currency = stash_tab["default_currency"]
    default_price = stash_tab["default_price"]
    return default_price, default_currency


def dump():
    open_stash()
    pyautogui.keyDown('CTRL')
    pyautogui.PAUSE = 0.03
    for row in range(5):
        for col in range(12):
            pyautogui.moveTo(INV_TL[0] + 20 + col*INV_WIDGTH, INV_TL[1] + 20 + row*INV_WIDGTH)
            pyautogui.click()   
    pyautogui.keyUp('CTRL')
    pyautogui.PAUSE = 0.05
# width = (REG_BR[0] - REG_TL[0]) / 24  
# x = REG_TL[0] + (12 - 0.5) * width
# y = REG_TL[1] + (12 - 0.5) * width

# print(width, x, y)

# time.sleep(2)
# dump()