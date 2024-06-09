import pyautogui
import time
from scarab_vendor.BankGrid import BankGrid
from scarab_vendor.InventoryGrid import InventoryGrid
import misc_utils.windowFocus as windowFocus
import misc_utils.captureRegion as captureRegion
import keyboard
import threading



# Function to simulate the control+click action on a bank cell
def control_click_cell(cell_center):
    pyautogui.keyDown('ctrl')
    pyautogui.click(cell_center)
    pyautogui.keyUp('ctrl')


# Function to execute the main script
def main():
    windowFocus.focus()
    time.sleep(2)
 
    top_left = (66, 267)
    bottom_right = (446.140625, 565.81640625)
    rows = 7  # The number of rows in the bank grid
    columns = 8  # The number of columns in the bank grid

    # Create an instance of BankGrid
    bank_grid = BankGrid(top_left=top_left, bottom_right=bottom_right, rows=rows, columns=columns)

    # Capture the image of the bank grid area
    bank_grid.load_from_csv("/Users/ahmedel-dib/Desktop/Trying stuff/Bot2.0/Untitled.csv")
    bank_grid.display_grid()  
    inventory_grid = InventoryGrid(top_left=(986.375, 505.6640625), bottom_right=(1459.05078125, 698.921875), rows=5, columns=12, empty_cell_color=(0,0,0))


    cell_center = (75,300)
    pyautogui.moveTo(cell_center)
    time.sleep(0.2)
    control_click_cell(cell_center)
    control_click_cell(cell_center)
    # control_click_cell(cell_center)

    # vendor
    vendor_center = (840, 400)  # Replace with actual coordinates
    pyautogui.moveTo(vendor_center)
    time.sleep(0.2)
    pyautogui.keyDown('option')
    pyautogui.keyDown('ctrl')
    pyautogui.click(vendor_center)
    pyautogui.keyUp('option')
    pyautogui.keyUp('ctrl')
    time.sleep(0.2)
    for row in range(2):  # Assuming we start at the first row
        cell_center = inventory_grid.get_cell_center(row, 0)
        pyautogui.moveTo(cell_center)
        control_click_cell(cell_center) 
    accept = (330,715)
    pyautogui.moveTo(accept)
    time.sleep(0.2)
    pyautogui.click(accept)

    # bank
    stash_center = (715, 450)  # Replace with actual coordinates
    pyautogui.moveTo(stash_center)
    time.sleep(0.2)
    pyautogui.click(stash_center) 
    time.sleep(0.2) 
    pyautogui.keyDown('ctrl') 
    pyautogui.moveTo(inventory_grid.get_cell_center(0,0)) 
    for row in range(inventory_grid.rows):
        for col in range(12):    
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
  

def run_main_in_thread():
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

def check_esc_key():
    print("Press ESC to stop...")
    try:
        while True:
            if keyboard.is_pressed('esc'):  # Check if the Escape key is pressed
                print("Escape key pressed. Exiting...")
                # Terminate the program
                exit(0)
    except Exception as e:
        print(f"Error detecting key press: {e}")

if __name__ == "__main__":
    # Create a thread for listening to the Escape key
    esc_listener = threading.Thread(target=check_esc_key, daemon=True)
    esc_listener.start()

    for _ in range(200):
        run_main_in_thread()