import os


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

        os.system("cls")
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

