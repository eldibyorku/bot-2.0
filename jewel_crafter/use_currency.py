import pyautogui
import pyperclip
import re
import time
import beepy #notification sound on completion
import misc_utils.windowFocus as windowFocus #brings window into focus
from pynput.keyboard import Key, Controller, Listener

is_shift_pressed = False

keyboard = Controller()
# Coordinates for the game's UI elements
jewel_location = (255, 400)
transmute_location = (50, 275)
aug_location = (173,308)
alt_location = (90, 268)
regal_location = (319, 262)
scoure_location = (324, 447)
chaos_location = (408, 262) 
exalt_location = (223, 267)
annull_location = (123, 268)




# Function to read the current mods on the jewel

def go_to_center():
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)

def read_item():
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyperclip.copy('')  # Clear clipboard content before copying
    keyboard.press(Key.ctrl)
    time.sleep(0.1)
    keyboard.press('c')
    time.sleep(0.1)
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(1)
    item = pyperclip.paste()
    if not item.startswith("Item"):
        print("Cursor not pointed at a valid item")
        exit()
    return item

# Functions to simulate mouse movements and clicks for crafting with currency
# TODO, spam alt (done in cluster.py), spam chaos
def transmute():
    pyautogui.moveTo(transmute_location[0], transmute_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()
    print("transed")


def alt():
    pyautogui.moveTo(alt_location[0], alt_location[1], 0.05)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.05)
    pyautogui.leftClick()

def roll_alt():
   pyautogui.leftClick()

def aug():
    pyautogui.moveTo(aug_location[0], aug_location[1], 0.05)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.05)
    pyautogui.leftClick()

def regal():
    pyautogui.moveTo(regal_location[0], regal_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()

def scoure():
    pyautogui.moveTo(scoure_location[0], scoure_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()

def chaos():
    pyautogui.moveTo(chaos_location[0], chaos_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()

def roll_chaos():
   pyautogui.leftClick()

def slam():  
    pyautogui.moveTo(exalt_location[0], exalt_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()

def annul():
    pyautogui.moveTo(annull_location[0], annull_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()


