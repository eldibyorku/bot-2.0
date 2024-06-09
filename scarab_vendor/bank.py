import pyautogui
import time
from scarab_vendor.BankGrid import BankGrid
from scarab_vendor.InventoryGrid import InventoryGrid
import misc_utils.windowFocus as windowFocus
import misc_utils.captureRegion as captureRegion
import keyboard
import threading

windowFocus.focus()
time.sleep(2)

accept_inv=(1256,650)
trade_grid = InventoryGrid(top_left=(255,218), bottom_right=(727.5, 415.5),rows=5, columns=12, empty_cell_color=(0,0,0))
accept_trade = (290,682)


inventory_grid = InventoryGrid(top_left=(986.375, 505.6640625), bottom_right=(1459.05078125, 698.921875), rows=5, columns=12, empty_cell_color=(0,0,0))

#trade
pyautogui.moveTo(accept_inv)
time.sleep(0.1)
pyautogui.click(accept_inv)
time.sleep(3)
for row in range(trade_grid.rows):
    for col in range(trade_grid.columns):  
        cell_center = trade_grid.get_cell_center(row, col)
        pyautogui.moveTo(cell_center)
pyautogui.moveTo(accept_trade)
pyautogui.click(accept_trade)

#bank
stash_center = (688, 375)  # Replace with actual coordinates
pyautogui.moveTo(stash_center)
time.sleep(0.2)
pyautogui.click(stash_center) 
time.sleep(0.2) 
pyautogui.keyDown('ctrl') 
pyautogui.moveTo(inventory_grid.get_cell_center(0,0)) 
for row in range(inventory_grid.rows):
    for col in range(inventory_grid.columns):    
        cell_center = inventory_grid.get_cell_center(row, col)
        # pyautogui.moveTo(cell_center)
        pyautogui.click(cell_center)
        pyautogui.click(cell_center)
        # time.sleep(0.05)
        # control_click_cell(cell_center)
        # control_click_cell(cell_center)
        # control_click_cell(cell_center)
pyautogui.keyUp('ctrl')
time.sleep(5)