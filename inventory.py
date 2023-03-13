import json
import os
from inventory_item import Gear, Spell, Item


class Inventory:
    def __init__(self):
        self.swords = []
        self.armors = []
        self.staffs = []
        self.spells = []
        self.items = []


    def DisplayItemList(self, inventory_list, equippable):
        # Creates a string of inventory list item names to be printed to the console.
        # Items are displayed in columns of 20 characters in length.
        #
        # Inputs:
        # inventory_list - list of the category of items to display
        # equippable - True/False if the list contains items that can be equipped

        inv_str = ""
        inv_str_temp = ""

        for item in inventory_list:
            # Check for new line
            if len(inv_str_temp) == 80:
                if len(inv_str) == 0:
                    inv_str += inv_str_temp
                else:
                    inv_str += "\n" + inv_str_temp
                inv_str_temp = ""

            # Add item name
            inv_str_temp += item.name

            # Show if item is equipped
            if equippable:
                if item.equipped:
                    inv_str_temp += " (E)"

            # Show quantity if more than 1
            if item.item_type == "item":
                if item.qty > 1:
                    inv_str_temp += " (" + str(item.qty) + ")"

            # Align items in columns of 20 characters
            item_char_count = len(inv_str_temp) % 20
            for i in range(20 - item_char_count):
                inv_str_temp += " "

                # Add final temp string
        if len(inv_str) == 0:
            inv_str += inv_str_temp
        else:
            inv_str += "\n" + inv_str_temp

        return inv_str

    def DisplayInventory(self):
        # Displays contents of the inventory to the user

        print('Swords')
        print(self.DisplayItemList(self.swords, True))
        print()
        print('Armors')
        print(self.DisplayItemList(self.armors, True))
        print()
        print('Staffs')
        print(self.DisplayItemList(self.staffs, True))
        print()
        print('Spell Book')
        print(self.DisplayItemList(self.spells, False))
        print()
        print('Items')
        print(self.DisplayItemList(self.items, False))

    def DisplaySpells(self):
        # Creates a string of known spells and their mana costs

        spell_str = ""
        spell_str_temp = ""

        for spell in self.spells:
            # Check for new line
            if len(spell_str_temp) == 80:
                if len(spell_str) == 0:
                    spell_str += spell_str_temp
                else:
                    spell_str += "\n" + spell_str_temp
                spell_str_temp = ""

            # Add item name
            spell_str_temp += spell.name

            # Show mana cost
            spell_str_temp += " (" + str(spell.mana_cost) + ")"

            # Align items in columns of 20 characters
            item_char_count = len(spell_str_temp) % 20
            for i in range(20 - item_char_count):
                spell_str_temp += " "

                # Add final temp string
        if len(spell_str) == 0:
            spell_str += spell_str_temp
        else:
            spell_str += "\n" + spell_str_temp

        return spell_str

    def AddItem(self, item):
        # Adds an item to the inventory
        #
        # Inputs:
        # item - the item object to be added

        if item.item_type == 'sword':
            self.swords.append(item)

        if item.item_type == 'armor':
            self.armors.append(item)

        if item.item_type == 'staff':
            self.staffs.append(item)

        if item.item_type == 'spell':
            self.spells.append(item)

        if item.item_type == 'item':
            self.items.append(item)

    def RemoveItem(self, item):
        # Removes an item from the inventory
        #
        # Inputs:
        # item - the item object to be removed

        if item.item_type == 'sword':
            self.swords.remove(item)

        if item.item_type == 'armor':
            self.armors.remove(item)

        if item.item_type == 'staff':
            self.staffs.remove(item)

        if item.item_type == 'spell':
            self.spells.remove(item)

        if item.item_type == 'item':
            self.items.remove(item)

    def GetItem(self, name):
        for item in self.swords:
            if name.lower() == item.name.lower() or name.lower() in item.synonym:
                return item

        for item in self.armors:
            if name.lower() == item.name.lower() or name.lower() in item.synonym:
                return item

        for item in self.staffs:
            if name.lower() == item.name.lower() or name.lower() in item.synonym:
                return item

        for item in self.spells:
            if name.lower() == item.name.lower() or name.lower() in item.synonym:
                return item

        for item in self.items:
            if name.lower() == item.name.lower() or name.lower() in item.synonym:
                return item

        return None

    def HasSpell(self, name):
        for item in self.spells:
            if name.lower() == item.name.lower() or name.lower() in item.synonym:
                return True

        return False

    def CanCastSpell(self, name, cur_mana):
        for item in self.spells:
            if item.name.lower() == name.lower():
                if item.mana_cost <= cur_mana:
                    return True

        return False

    def SaveInventory(self):
        # Converts the contents of the inventory into JSON format and saves to inventory.json

        # Create dictionary to store inventory that will be converted to JSON
        inv = {}

        # Add swords to dictionary
        for item in self.swords:
            info = {
                "name": item.name,
                "synonym": item.synonym,
                "description": item.description,
                "item_type": item.item_type,
                "equippable": item.equippable,
                "equipped": item.equipped,
                "cost": item.cost,
                "hp_mod": item.hp_mod,
                "atk_mod": item.atk_mod,
                "def_mod": item.def_mod,
                "mag_mod": item.mag_mod,
                "mana_mod": item.mana_mod}

            inv[item.name] = info

        # Add armors to dictionary
        for item in self.armors:
            info = {
                "name": item.name,
                "synonym": item.synonym,
                "description": item.description,
                "item_type": item.item_type,
                "equippable": item.equippable,
                "equipped": item.equipped,
                "cost": item.cost,
                "hp_mod": item.hp_mod,
                "atk_mod": item.atk_mod,
                "def_mod": item.def_mod,
                "mag_mod": item.mag_mod,
                "mana_mod": item.mana_mod}

            inv[item.name] = info

        # Add staffs to dictionary
        for item in self.staffs:
            info = {
                "name": item.name,
                "synonym": item.synonym,
                "description": item.description,
                "item_type": item.item_type,
                "equippable": item.equippable,
                "equipped": item.equipped,
                "cost": item.cost,
                "hp_mod": item.hp_mod,
                "atk_mod": item.atk_mod,
                "def_mod": item.def_mod,
                "mag_mod": item.mag_mod,
                "mana_mod": item.mana_mod}

            inv[item.name] = info

            # Add spells to dictionary
            for item in self.spells:
                info = {
                    "name": item.name,
                    "synonym": item.synonym,
                    "description": item.description,
                    "item_type": item.item_type,
                    "equippable": item.equippable,
                    "equipped": item.equipped,
                    "cost": item.cost,
                    "mana_cost": item.mana_cost,
                    "duration": item.duration,
                    "casts": item.casts,
                    "lvl_up": item.lvl_up,
                    "base_dmg": item.base_dmg}

                inv[item.name] = info

                # Add items to dictionary
                for item in self.items:
                    info = {
                        "name": item.name,
                        "synonym": item.synonym,
                        "description": item.description,
                        "item_type": item.item_type,
                        "equippable": item.equippable,
                        "equipped": item.equipped,
                        "cost": item.cost,
                        "qty": item.qty,
                        "hp_mod": item.hp_mod,
                        "mana_mod": item.mana_mod}

                    inv[item.name] = info

        inv_json = json.dumps(inv, indent=4)

        with open("inventory.json", "w") as outfile:
            outfile.write(inv_json)
            
    def LoadInventory(self):
        # Clears the contents of the inventory then loads the contents of inventory.json, creates objects of the correct
        # type for each item, and adds them to the inventory.

        # Clear inventory
        self.swords.clear()
        self.armors.clear()
        self.staffs.clear()
        self.spells.clear()
        self.items.clear()

        # import item data from inventory.json file
        with open("inventory.json") as in_file:
            unparsed_inv = in_file.read()

        # parse the json data into a dictionary in Python format
        parsed_inv = json.loads(unparsed_inv)

        # Create item objects and add to inventory
        for key in parsed_inv:
            if parsed_inv[key]["item_type"] == "item":
                inv_item = Item(
                    name=parsed_inv[key]["name"],
                    synonym=parsed_inv[key]["synonym"],
                    description=parsed_inv[key]["description"],
                    item_type=parsed_inv[key]["item_type"],
                    equippable=parsed_inv[key]["equippable"],
                    equipped=parsed_inv[key]["equipped"],
                    cost=parsed_inv[key]["cost"],
                    qty=parsed_inv[key]["qty"],
                    hp_mod=parsed_inv[key]["hp_mod"],
                    mana_mod=parsed_inv[key]["mana_mod"]
                )
            elif parsed_inv[key]["item_type"] == "spell":
                inv_item = Spell(
                    name=parsed_inv[key]["name"],
                    synonym=parsed_inv[key]["synonym"],
                    description=parsed_inv[key]["description"],
                    item_type=parsed_inv[key]["item_type"],
                    equippable=parsed_inv[key]["equippable"],
                    equipped=parsed_inv[key]["equipped"],
                    cost=parsed_inv[key]["cost"],
                    mana_cost=parsed_inv[key]["mana_cost"],
                    duration=parsed_inv[key]["duration"],
                    casts=parsed_inv[key]["casts"],
                    lvl_up=parsed_inv[key]["lvl_up"],
                    base_dmg=parsed_inv[key]["base_dmg"]
                )
            else:
                inv_item = Gear(
                    name=parsed_inv[key]["name"],
                    synonym=parsed_inv[key]["synonym"],
                    description=parsed_inv[key]["description"],
                    item_type=parsed_inv[key]["item_type"],
                    equippable=parsed_inv[key]["equippable"],
                    equipped=parsed_inv[key]["equipped"],
                    cost=parsed_inv[key]["cost"],
                    hp_mod=parsed_inv[key]["hp_mod"],
                    atk_mod=parsed_inv[key]["atk_mod"],
                    def_mod=parsed_inv[key]["def_mod"],
                    mag_mod=parsed_inv[key]["mag_mod"],
                    mana_mod=parsed_inv[key]["mana_mod"]
                )

            if inv_item.equippable == "True":
                inv_item.equippable = True
            else:
                inv_item.equippable = False

            if inv_item.equipped == "True":
                inv_item.equipped = True
            else:
                inv_item.equipped = False

            self.AddItem(inv_item)

    def LoadAllInventory(self):
        # Clears the contents of the inventory then loads the contents of inventory.json, creates objects of the correct
        # type for each item, and adds them to the inventory.

        # Clear inventory
        self.swords.clear()
        self.armors.clear()
        self.staffs.clear()
        self.spells.clear()
        self.items.clear()

        # import item data from inventory.json file
        with open("all_inventory.json") as in_file:
            unparsed_inv = in_file.read()

        # parse the json data into a dictionary in Python format
        parsed_inv = json.loads(unparsed_inv)

        # Create item objects and add to inventory
        for key in parsed_inv:
            if parsed_inv[key]["item_type"] == "item":
                inv_item = Item(
                    name=parsed_inv[key]["name"],
                    synonym=parsed_inv[key]["synonym"],
                    description=parsed_inv[key]["description"],
                    item_type=parsed_inv[key]["item_type"],
                    equippable=parsed_inv[key]["equippable"],
                    equipped=parsed_inv[key]["equipped"],
                    cost=parsed_inv[key]["cost"],
                    qty=parsed_inv[key]["qty"],
                    hp_mod=parsed_inv[key]["hp_mod"],
                    mana_mod=parsed_inv[key]["mana_mod"]
                )
            elif parsed_inv[key]["item_type"] == "spell":
                inv_item = Spell(
                    name=parsed_inv[key]["name"],
                    synonym=parsed_inv[key]["synonym"],
                    description=parsed_inv[key]["description"],
                    item_type=parsed_inv[key]["item_type"],
                    equippable=parsed_inv[key]["equippable"],
                    equipped=parsed_inv[key]["equipped"],
                    cost=parsed_inv[key]["cost"],
                    mana_cost=parsed_inv[key]["mana_cost"],
                    duration=parsed_inv[key]["duration"],
                    casts=parsed_inv[key]["casts"],
                    lvl_up=parsed_inv[key]["lvl_up"],
                    base_dmg=parsed_inv[key]["base_dmg"]
                )
            else:
                inv_item = Gear(
                    name=parsed_inv[key]["name"],
                    synonym=parsed_inv[key]["synonym"],
                    description=parsed_inv[key]["description"],
                    item_type=parsed_inv[key]["item_type"],
                    equippable=parsed_inv[key]["equippable"],
                    equipped=parsed_inv[key]["equipped"],
                    cost=parsed_inv[key]["cost"],
                    hp_mod=parsed_inv[key]["hp_mod"],
                    atk_mod=parsed_inv[key]["atk_mod"],
                    def_mod=parsed_inv[key]["def_mod"],
                    mag_mod=parsed_inv[key]["mag_mod"],
                    mana_mod=parsed_inv[key]["mana_mod"]
                )

            if inv_item.equippable == "True":
                inv_item.equippable = True
            else:
                inv_item.equippable = False

            if inv_item.equipped == "True":
                inv_item.equipped = True
            else:
                inv_item.equipped = False

            self.AddItem(inv_item)