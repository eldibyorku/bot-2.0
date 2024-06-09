
import re
import time
import beepy #notification sound on completion
import misc_utils.windowFocus as windowFocus #brings window into focus
from jewel_crafter.use_currency import read_item, aug, alt, regal, scoure, chaos, slam, annul, roll_alt, transmute, go_to_center, roll_chaos
from pynput.keyboard import Key, Controller
import pyperclip
import beepy



class Item:
    def __init__(self, description):
        self.mods = []
        self.prefixes = []
        self.suffixes = []
        self.description = description
        self.get_mods()

    def get_mods(self):
        self.mods = []
        self.prefixes = []
        self.suffixes = []
        
        # Split the description into lines
        lines = self.description.strip().split('\n')
        
        # Updated regex to match the prefix and suffix mods
        pattern = r'{\s*(Prefix|Suffix)\s*Modifier\s*"([^"]+)"\s*\(Tier:\s*(\d+)\)[^}]*}'
        for i in range(len(lines)):
            if re.match(pattern, lines[i]):
                match = re.match(pattern, lines[i])
                if match and i + 1 < len(lines):
                    mod_info = {
                        'type': match.group(1).lower(),
                        'name': match.group(2),
                        'tier': match.group(3),
                        'text': lines[i + 1].strip()
                    }
                    self.mods.append(mod_info)
                    if mod_info['type'] == 'prefix':
                        self.prefixes.append(mod_info)
                    elif mod_info['type'] == 'suffix':
                        self.suffixes.append(mod_info)
        return self.mods
    
    def get_prefixes(self):
        return self.prefixes
    
    def count_prefixes(self):
        return len(self.prefixes)
    
    def get_suffixes(self):
        return self.suffixes
    
    def count_suffixes(self):
        return len(self.suffixes)
    
    def count_mods(self):
        return len(self.mods)
    
des = """Item Class: Jewels
Rarity: Rare
Glyph Heart
Large Cluster Jewel
--------
Requirements:
Level: 67
--------
Item Level: 84
--------
Adds 12 Passive Skills (enchant)
(Added Passive Skills are never considered to be in Radius by other Jewels) (enchant)
(All Added Passive Skills are Small unless otherwise specified) (enchant)
2 Added Passive Skills are Jewel Sockets (enchant)
Added Small Passive Skills grant: 10% increased Spell Damage (enchant)
(Passive Skills that are not Notable, Masteries, Keystones, or Jewel Sockets are Small) (enchant)
--------
{ Prefix Modifier "Notable" (Tier: 1) }
1 Added Passive Skill is Arcane Heroism — Unscalable Value
{ Prefix Modifier "Glimmering" (Tier: 2) — Defences, Energy Shield }
Added Small Passive Skills also grant: +6(6-9) to Maximum Energy Shield
{ Suffix Modifier "of the Meteor" (Tier: 1) — Attribute }
Added Small Passive Skills also grant: +4 to All Attributes (fractured)
{ Suffix Modifier "of Excitement" (Tier: 3) — Mana }
Added Small Passive Skills also grant: 4% increased Mana Regeneration Rate
--------
Place into an allocated Large Jewel Socket on the Passive Skill Tree. Added passives do not interact with jewel radiuses. Right click to remove from the Socket.
--------
Fractured Item
"""

item = Item(des)
print(item.count_prefixes())


# # Example input data
# data = '''
# { Prefix Modifier "Notable" (Tier: 1) }
# 1 Added Passive Skill is Arcane Heroism — Unscalable Value
# { Prefix Modifier "Glimmering" (Tier: 2) — Defences, Energy Shield }
# Added Small Passive Skills also grant: +6(6-9) to Maximum Energy Shield
# { Suffix Modifier "of the Meteor" (Tier: 1) — Attribute }
# Added Small Passive Skills also grant: +4 to All Attributes (fractured)
# { Suffix Modifier "of Excitement" (Tier: 3) — Mana }
# Added Small Passive Skills also grant: 4% increased Mana Regeneration Rate
# '''

# # Regex to capture the necessary parts
# pattern = r'{\s*(Prefix|Suffix)\s*Modifier\s*"([^"]+)"\s*\(Tier:\s*(\d+)\)[^}]*}'
# regex = re.compile(pattern, re.IGNORECASE)

# # Process the data
# results = []
# lines = data.split('\n')
# for i in range(len(lines)):
#     match = regex.match(lines[i])
#     if match:
#         if i + 1 < len(lines):
#             mod_info = {
#                 'type': match.group(1).lower(),
#                 'name': match.group(2).lower(),
#                 'tier': match.group(3),
#                 'text': lines[i+1].strip().lower()
#             }
#             results.append(mod_info)

# # Display the results
# for result in results:
#     print(result)
        
    