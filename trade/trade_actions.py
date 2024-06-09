import pyautogui
from trade.trade_order import TradeOrder
from trade.stash import go_to_item, extract_currency_from_tab, go_to_inv, dump
from utils.item_utils import read_item, extract_currency, get_item_name
import pyperclip
import re
import time
from pynput.keyboard import Key, Controller
from utils.waits import check_for_trade_window, check_for_mouse_over
from utils.trade_utils import verify_payment
keyboard = Controller()

TRADE_WINDOW = ()
CELL_SIZE = ()

def verify_whisper(tradeorder: TradeOrder):
    print(f"verifying trade. going to item in tab {tradeorder.tab}, left: {tradeorder.pos_left}, top: {tradeorder.pos_top}")
    go_to_item(tradeorder.tab, tradeorder.pos_left, tradeorder.pos_top)
    actual_item = read_item()
    print("extracting currency info")
    actual_amount, actual_currency = extract_currency(actual_item)
    if actual_amount == None and actual_currency == None:
        print("item does not have a note price, getting price from tab")
        actual_amount, actual_currency = extract_currency_from_tab(tradeorder.tab)

    if actual_amount != tradeorder.sell_amount or actual_currency != tradeorder.sell_currency:
        print(f"item amount incorrect, actual price is {actual_amount} {actual_currency}")
        return False
    
    if tradeorder.item_name not in get_item_name(actual_item):
        print("item mismatch")
        return False
    
    return True

def invite_user(username):
    print(username)
    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(0.1)
    command = f'/invite {username}'
    pyautogui.typewrite(command)
    pyautogui.press('enter')

def trade_user(username):
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(0.1)
    command = f'/tradewith {username}'
    pyautogui.typewrite(command)
    pyautogui.press('enter')


def take_item(tradeorder: TradeOrder):
    go_to_item(tradeorder.tab, tradeorder.pos_left, tradeorder.pos_top)
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.keyUp('ctrl')

def place_item_in_trade():
    go_to_inv()
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.keyUp('ctrl')

def accept():
    pyautogui.moveTo(300.2109375, 687.453125, 0.1)
    pyautogui.click()
    time.sleep(0.2)

def execute_trade(tradeorder: TradeOrder):
    take_item(tradeorder)
    trade_user(tradeorder.buyer)
    # try:
    #     while not check_for_trade_window():
    #         print("waiting for trade window inside while lopp")
    # except Exception as e:
    #     print(e)


    while not check_for_trade_window():
        print("waiting for trade window")
    
    if check_for_trade_window():
        # if pyautogui.locate('images/tradeWindow.png', pyautogui.screenshot(region=(296, 496, 664, 362))):
            print("placing item in trade")
            place_item_in_trade()
            time.sleep(1)
            
            while not check_for_mouse_over():
                print("waiting for mouse over prompt")
    
            if check_for_mouse_over():
                print(f"total in d {tradeorder.total_in_d}")
                while not verify_payment(tradeorder.total_in_d):
                    print("startig to verify")
                
                print("amount verified")
                accept()

                while check_for_trade_window():
                    print("waiting for window to close")
                print("dumping")
                dump()
    print("reached the end of execute trade")




