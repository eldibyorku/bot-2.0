import pyautogui

# def wait_for_window():
#     pyautogui.sleep(1)

#     while True:
#         if not pyautogui.locate('images/waitingForTradeAccept.png', pyautogui.screenshot(region=(726, 490, 465, 96))):
#             print("inside if")
#             break
#         pyautogui.sleep(1)
#         print("after sleep")
#     print("exited loop")
#     return pyautogui.locate('images/tradeWindow.png', pyautogui.screenshot(region=(296, 496, 664, 362)))
    
def check_for_trade_window():
    try:
        if pyautogui.locateOnScreen('/Users/ahmedel-dib/Desktop/Trying_stuff/Bot2.0/images/trade_open.png', confidence=0.7):
            print("trade window found")
            return True
        else:
            print("trade window not found")
            return  False
    except pyautogui.ImageNotFoundException:
        print(" wait for trade window fucked up")

def check_for_mouse_over():
    try:
        if pyautogui.locateOnScreen('/Users/ahmedel-dib/Desktop/Trying_stuff/Bot2.0/images/mouse_over_items.png', confidence=0.7):
            print("should start mousing over")
            return True
        else:
            print("mouse over prompt not started")
            return  False
    except pyautogui.ImageNotFoundException:
        print(" mouse over fucked up")
    


##trade_open
# Mouse clicked at position: (395.046875, 89.890625)
# Mouse clicked at position: (578.37109375, 169.0)
# , pyautogui.screenshot(region=(390, 85, 200, 100))
# import time
# time.sleep(1)
# check_for_trade_window()