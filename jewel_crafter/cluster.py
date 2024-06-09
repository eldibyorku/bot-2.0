
import re
import time
import beepy #notification sound on completion
import misc_utils.windowFocus as windowFocus #brings window into focus
from jewel_crafter.use_currency import read_item, aug, alt, regal, scoure, chaos, slam, annul, roll_alt, transmute, go_to_center, roll_chaos
from pynput.keyboard import Key, Controller
import pyperclip
import beepy
from jewel_crafter.update_used import update_currency_data

keyboard = Controller()
currency_file = 'currency_used.txt'


class JewelCrafter:
    def __init__(self, mandatory_mods, optional_mods, num_mandatory_required, num_optional_required,\
                  no_slam=None, no_regal=None, no_annul=None):
        self.mandatory_mods = mandatory_mods
        self.optional_mods = optional_mods
        self.num_mandatory_required = num_mandatory_required
        self.num_optional_required = num_optional_required
        self.num_mods_needed = num_mandatory_required + num_optional_required
        self.item_mods = []
        
        self.currency_used = {
            "augs": 0,
            "alts": 0,
            "regals": 0,
            "scoures": 0,
            "exalts": 0,
            "annulls": 0,
            "chaos": 0,
        }
        self.alting = False
        self.chaosing = False
    
        self.no_slam = no_slam if no_slam is not None else []
        self.no_regal = no_regal if no_regal is not None else []
        self.no_annul = no_annul if no_annul is not None else []

    def read_mods(self):
        for attempt in range(5):
            pyperclip.copy('')
            keyboard.press(Key.ctrl)
            keyboard.press('c')
            time.sleep(0.1)
            keyboard.release('c')
            keyboard.release(Key.ctrl)
            time.sleep(0.1)
            item = pyperclip.paste()
            if item.startswith("Item"):
                return item
            else:
                print(f"Attempt {attempt + 1}: Cursor not pointed at a valid item. Retrying...")
        print("Failed to read a valid item after 2 attempts. Please check the cursor placement and try again.")
        update_currency_data(currency_file, self.currency_used)
        exit()

    def get_mods(self):
        item_description = self.read_mods()
        pattern = r"(Added Small Passive Skills|1 Added Passive Skill) +(have|also grant:|is) (.*)"
        self.item_mods = []
        for line in item_description.strip().split('\n'):
            match = re.match(pattern, line)
            if match:
                mod = match.group(3).replace("\r", "")
                if " (fractured)" in mod:
                    mod = mod.replace(" (fractured)", "")
                self.item_mods.append(mod)

    def check_required_mods(self):
        mandatory_present_count = self.get_num_mandatory_present()
        optional_present_count = self.get_num_optional_present()
        return (mandatory_present_count >= self.num_mandatory_required and
                optional_present_count >= self.num_optional_required)

    def get_num_mandatory_present(self):
        return sum(mod in self.item_mods for mod in self.mandatory_mods)

    def get_num_optional_present(self):
        return sum(mod in self.item_mods for mod in self.optional_mods)

    def get_num_good_mods(self):
        return self.get_num_mandatory_present() + self.get_num_optional_present()
    


    def check_for_trans(self):
        return len(self.item_mods) == 0

    def check_for_aug(self):
        return len(self.item_mods) == 1 and (self.get_num_good_mods() == 1 or self.num_mods_needed < 4)


    def check_for_alt(self):
        return len(self.item_mods) < 3 and len(self.item_mods) > 0 and (self.num_mods_needed == 4 and self.get_num_good_mods() < 2 or \
                                                                        self.num_mods_needed < 4 and self.get_num_good_mods() < 1)

    def check_for_regal(self):
        return (len(self.item_mods) == 2) and ((self.num_mods_needed < 4 and self.get_num_good_mods() == 1) or
                                               (self.get_num_good_mods() == 2 and self.num_mods_needed >= 2))

    def check_for_scoure(self):
        return len(self.item_mods) > 2 and not (self.check_for_slam() or self.check_for_annul())\
                  and (self.get_num_good_mods() < self.num_mods_needed or self.get_num_mandatory_present() < self.num_mandatory_required)

    def check_for_slam(self):
        # Check if the basic condition for a slam is met
        if len(self.item_mods) == 3 and ((self.num_mods_needed == 4 and self.get_num_good_mods() == 3) or
                                        (self.num_mods_needed == 3 and self.get_num_good_mods() == 2)):
            # Identify the missing mod
            all_possible_mods = set(self.mandatory_mods + self.optional_mods)
            current_mods_set = set(self.item_mods)
            missing_mods = all_possible_mods - current_mods_set

            # There should be exactly one missing mod, check if it is in the no_slam list
            too_risky_to_slam = missing_mods & set(self.no_slam)
            # missing_mod = next(iter(missing_mods)) if missing_mods else None
            return not too_risky_to_slam

        return False

    def check_for_annul(self):
        return (len(self.item_mods) == 4 and self.num_mods_needed == 4 and self.get_num_good_mods() == 3)


    def alt_regal(self):
        go_to_center()
        self.get_mods()
        while not self.check_required_mods():
            if self.check_for_annul():
                # check if item_mods contains any mod that is in no_anull list
                common_mods = set(self.item_mods) & set(self.no_annul)
                if not common_mods:
                    annul()
                    self.currency_used['annulls'] += 1
                    time.sleep(3)
                    self.get_mods()
                else:
                    break
            elif self.check_for_slam():
                slam()
                self.currency_used['exalts'] += 1
                time.sleep(3)
                self.get_mods()
            elif self.check_for_regal():
                regal()
                self.currency_used['regals'] += 1
                time.sleep(0.5)
                self.get_mods()
            elif self.check_for_aug():
                aug()
                self.currency_used['augs'] += 1
                self.get_mods()
            elif self.check_for_alt():
                keyboard.press(Key.shift)
                while self.check_for_alt():
                    if self.check_for_aug() or self.check_required_mods():
                        break
                    elif self.alting:
                        roll_alt()
                        time.sleep(0.1)
                        self.currency_used['alts'] += 1
                        self.get_mods()
                    else:
                        alt()
                        self.currency_used['alts'] += 1
                        self.get_mods()
                        self.alting = True  
                keyboard.release(Key.shift)
                self.alting = False   
            elif self.check_for_trans():
                transmute()
                self.get_mods()
            else:
                scoure()
                self.currency_used['scoures'] += 1
                self.get_mods()
        update_currency_data(currency_file, self.currency_used)
        beepy.beep(sound=8)

    def alt_aug(self):
        go_to_center()
        self.get_mods()
        while not self.check_required_mods():
            print("in outer check")
            if self.check_for_aug():
                print("in outer aug")
                aug()
                self.currency_used['augs'] += 1
                self.get_mods()
            elif self.check_for_alt():
                keyboard.press(Key.shift)
                while self.check_for_alt():
                    print("in outer alt")
                    if self.check_for_aug() or self.check_required_mods():
                        print("in inner aug")
                        break
                    elif self.alting:
                        roll_alt()
                        time.sleep(0.1)
                        self.currency_used['alts'] += 1
                        self.get_mods()
                    else:
                        alt()
                        self.currency_used['alts'] += 1
                        self.get_mods()
                        self.alting = True  
                keyboard.release(Key.shift)
                self.alting = False   

    def chaos_spam(self):
        go_to_center()
        self.get_mods()
        while not self.check_required_mods():
                if self.get_num_good_mods() == 2 and len(self.get_mods) == 3:
                    slam()
                elif self.chaosing:
                    roll_chaos()
                    time.sleep(0.1)
                    self.currency_used['chaos'] += 1
                    self.get_mods()
                else:
                    keyboard.press(Key.shift)
                    chaos()
                    self.currency_used['chaos'] += 1
                    self.get_mods()
                    self.chaosing = True        
        keyboard.release(Key.shift)
        self.alting = False   

                





if __name__ == '__main__':
    windowFocus.focus()  # Brings the game screen into focus so we can interact with it
    time.sleep(2)        # Pause for 2 seconds to allow window focus to settle
   
    test_m = ['Overlord']
    test_o = ['Martial Prowess', 'Feed the Fury', 'Fuel the Fight', 'Weight Advantage', '+8 to Strength']   
    
    mandatory_mods = ['35% increased Effect',  '+4 to All Attributes']
    o2_mods = ['+6 to Strength',
                '+7 to Strength',
                '+8 to Strength']
    optional_mods = ['+10 to Maximum Life',
                 '+9 to Maximum Life',
                 '+8 to Maximum Life',
                 
                ]
    no_annul = ['+7 to Maximum Life','+6 to Maximum Life','+5 to Maximum Life','+4 to Maximum Life','+3 to Maximum Life','+2 to Maximum Life', '4% increased Damage', '3% increased Damage']                
    JC = JewelCrafter(mandatory_mods, optional_mods, 2, 1, no_annul=no_annul)
    JC.chaos_spam()
    

    # mandatory_mods_chaos = ['35% increased Effect']
    # optional_mods_chaos = ['3% increased Attack Speed', '+10 to Maximum Life']
    # JC = JewelCrafter(test_m, test_o, 1, 1)
    # JC.alt_aug()
    # go_to_center()
    # JC.get_mods()
    # print(JC.item_mods)
   


    # optional_mods = ['+5% to Chaos Resistance',
#                 '+4% to all Elemental Resistances',
#                 '+6 to Strength',
#                 '+7 to Strength',
#                 '+8 to Strength',
#                 '+6 to Dexterity',
#                 '+7 to Dexterity',
#                 '+8 to Dexterity',
#                 '+6 to Intelligence',
#                 '+7 to Intelligence',
#                 '+8 to Intelligence',
#                 '+4 to All Attributes',
#                 ]

# mandatory_mods = ['6% increased maximum Energy Shield','7% increased maximum Energy Shield','8% increased maximum Energy Shield',
#                   '6% increased maximum Life','7% increased maximum Life','8% increased maximum Life',
#                   '8% increased maximum Mana','9% increased maximum Mana','10% increased maximum Mana',
#                   '+12% to Critical Strike Multiplier for Spell Damage','+13% to Critical Strike Multiplier for Spell Damage',
#                   '+14% to Critical Strike Multiplier for Spell Damage','+15% to Critical Strike Multiplier for Spell Damage',
#                   '+12% to Critical Strike Multiplier with Elemental Skills','+13% to Critical Strike Multiplier with Elemental Skills',
#                   '+14% to Critical Strike Multiplier with Elemental Skills','+15% to Critical Strike Multiplier with Elemental Skills',]
# mandatory_mods = ['35% increased Effect', 'Heavy Hitter', '+8 to Strength', 'Feed the Fury']
# optional_mods = ['Fuel The Fight','+7 to Dexterity']

# mandatory_mods = ["Overlord"]
# optional_mods = ["Fuel the Fight", "Feed the Fury", "Martial Prowess", "Weight Advantage", "Calamitous"]
