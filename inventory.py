import os


class Inventory:
    def __init__(self):
        self._swords = []
        self._armors = []
        self._staffs = []
        self._spells = []
        self._items = []

    def _DisplayItemList(self, inventory_list, equipable):
        # Creates a string of inventory list item names to be printed to the console.
        # Items are displayed in columns of 20 characters in length.
        #
        # Inputs:
        # inventory_list - list of the category of items to display
        # equipable - True/False if the list contains items that can be equipped

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
            if equipable:
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
        print(self._DisplayItemList(self._swords, True))
        print()
        print('Armors')
        print(self._DisplayItemList(self._armors, True))
        print()
        print('Staffs')
        print(self._DisplayItemList(self._staffs, True))
        print()
        print('Spell Book')
        print(self._DisplayItemList(self._spells, False))
        print()
        print('Items')
        print(self._DisplayItemList(self._items, False))

    def AddItem(self, item):
        # Adds an item to the inventory
        #
        # Inputs:
        # item - the item object to be added

        if item.item_type == 'sword':
            self._swords.append(item)

        if item.item_type == 'armor':
            self._armors.append(item)

        if item.item_type == 'staff':
            self._staffs.append(item)

        if item.item_type == 'spell':
            self._spells.append(item)

        if item.item_type == 'item':
            self._items.append(item)

    def RemoveItem(self, item):
        # Removes an item from the inventory
        #
        # Inputs:
        # item - the item object to be removed

        if item.item_type == 'sword':
            self._swords.remove(item)

        if item.item_type == 'armor':
            self._armors.remove(item)

        if item.item_type == 'staff':
            self._staffs.remove(item)

        if item.item_type == 'spell':
            self._spells.remove(item)

        if item.item_type == 'item':
            self._items.remove(item)

    def GetItem(self, name):
        for item in self._swords:
            if item.name == name:
                return item

        for item in self._armors:
            if item.name == name:
                return item

        for item in self._staffs:
            if item.name == name:
                return item

        for item in self._spells:
            if item.name == name:
                return item

        for item in self._items:
            if item.name == name:
                return item

        return None
