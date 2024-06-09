import pyautogui
import pyperclip
import re
import time
import beepy
# import misc_utils.windowFocus as windowFocus

# import keyboard
from pynput.keyboard import Key, Controller
keyboard = Controller()
# aug_config = CURRENCY_TAB['Orb of Augmentation']
# alt_config = CURRENCY_TAB['Orb of Alteration']


jewel_types = ['Crimson Jewel', 'Cobalt Jewel', 'Viridian Jewel']
# desired_mods = ['Arming','Enlightened', 'Vivid', 'of Potency', 'of Demolishing', 'of the Elements', 'of Zealousness', 'of Exsanguinating', 'of Acrimony', 'Shimmering', 'of Unmaking', 'of Atrophy', 'of Gelidity']
desired_mods = ['Arming','Enlightened', 'Vivid', 'of Potency', 'of Demolishing', 'of the Elements', 'of Zealousness', 'Unmaking', 'Shimmering']
aug_location = (173,308)
alt_location = (90, 268)    
jewel_location = (255, 400)


def read_name():
    pyperclip.copy('')
    keyboard.press(Key.ctrl)
    time.sleep(0.1) 
    keyboard.press('c') 
    time.sleep(0.1)  
    keyboard.release('c')
    time.sleep(0.1) 
    keyboard.release(Key.ctrl)
    time.sleep(0.1) 
    name = pyperclip.paste().strip().split('\n')[2]
    return name

def aug():
   
    pyautogui.keyUp('shift')
    pyautogui.moveTo(aug_location[0], aug_location[1], 0.1)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()

def alt(): 
    
    print("geting new alt")
    keyboard.release(Key.shift)
    pyautogui.moveTo(alt_location[0], alt_location[1], 0.1)
    # pyautogui.keyDown('shift')
    keyboard.press(Key.shift)
    pyautogui.rightClick()
    pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
    pyautogui.leftClick()
   
   
def alt2():
    print("alt shift clicked")
    keyboard.press(Key.shift)
    time.sleep(0.5)
    pyautogui.leftClick()

def extract_jewel_name_components(name, jewel_types):
    parts = name.split()
    components = {
        'optional_meta_type': None,
        'prefix': None,
        'jewel_type': None,
        'suffix': None
    }

    # Identify suffix starting with "of" if present
    if "of" in parts:
        of_index = parts.index("of")
        components['suffix'] = ' '.join(parts[of_index:])

    # Attempt to find the jewel type by checking each known type against the name
    for jewel_type in jewel_types:
        if jewel_type in name:
            components['jewel_type'] = jewel_type
            break

    if components['jewel_type']:
        jewel_type_index = name.index(components['jewel_type'])
        # Extract everything before the jewel type as a single string
        before_jewel_type = name[:jewel_type_index].strip()
        before_parts = before_jewel_type.split()

        # Depending on the count of parts before the jewel type, assign meta type and/or prefix
        if len(before_parts) > 1:
            components['optional_meta_type'] = before_parts[0]
            components['prefix'] = ' '.join(before_parts[1:])
        elif len(before_parts) == 1:
            # If only one part exists, it might be a prefix or meta type; context needed
            # This example assumes it's a prefix for simplicity
            components['prefix'] = before_parts[0]

    return components

def check_prefix_suffix_in_desired_mods(name_components, desired_mods):
    matches = 0  # Initialize the count of matches

    # Check if the prefix is in the desired mods
    if name_components['prefix'] and any(mod for mod in desired_mods if mod in name_components['prefix']):
        matches += 1

    # Check if the suffix is in the desired mods
    if name_components['suffix'] and any(mod for mod in desired_mods if mod in name_components['suffix']):
        matches += 1

    return matches

def craft():
    alting = False
    alts=0
    augs=0
    while True:
        time.sleep(0.1)
        j_name = read_name()
        jewel = extract_jewel_name_components(j_name, jewel_types)
        
        matches = check_prefix_suffix_in_desired_mods(jewel, desired_mods)

        if(matches == 2):
            time.sleep(0.1)
            keyboard.release(Key.shift)
            beepy.beep(sound=8)
            # keyboard.release(Key.shift)
            # print("ALLAHU AKBAR!")
            print(f"augs used: {aug}, alts used: {alts}")
            exit()
        elif(matches == 1 and (not jewel['prefix'] or not jewel['suffix'])):
            alting = False
            aug()
            augs = augs + 1
        else:
            if alting:
                alt2()
                alts = alts +1
            else:
                alting = True
                alt()
                alts = alts +1
                time.sleep(0.2)
                
    



# windowFocus.focus()    
time.sleep(2)
pyautogui.moveTo(jewel_location[0], jewel_location[1], 0.1)
time.sleep(0.1)
craft()
# read_name()
# alt()
# alting = True
# time.sleep(1)
# pyperclip.copy('')
# keyboard.press(Key.ctrl)
# time.sleep(0.1) 
# keyboard.press('c')  
# keyboard.release('c')
# keyboard.release(Key.ctrl)

# text = pyperclip.paste()
# print(text)
# for _ in range(3):
#     if alting:
#         time.sleep(1)
#         alt2()


