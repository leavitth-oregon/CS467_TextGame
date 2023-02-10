import math
from character import Character


class Player(Character):
    def __init__(self, inventory, hp, defense, atk, mag, mana,
                 sword_eqp, armor_eqp, staff_eqp, money):
        super().__init__(hp, defense, atk, mag, mana)
        self.name = "You"
        self.inventory = inventory
        self.sword_eqp = sword_eqp
        self.armor_eqp = armor_eqp
        self.staff_eqp = staff_eqp
        self.money = money

    def EquipItem(self, name):
        # Equips item from player's inventory and updates player's stats
        #
        # Output:
        # "item not found" - name of desired item not found in player's inventory
        # "item not equippable" - item is not allowed to be equipped
        # "item equipped" - item was successfully equipped

        item = self.inventory.GetItem(name)

        if item is None:
            return "item not found"

        if not item.equippable:
            return "item not equippable"

        hp_pct = self.hp_cur / self.hp
        mana_pct = self.mana_cur / self.mana

        if item.item_type == "sword":
            self.RemoveItemStats(self.sword_eqp)
            self.sword_eqp = item
            self.AddItemStats(self.sword_eqp)

        if item.item_type == "armor":
            self.RemoveItemStats(self.armor_eqp)
            self.armor_eqp = item
            self.AddItemStats(self.armor_eqp)

        if item.item_type == "staff":
            self.RemoveItemStats(self.staff_eqp)
            self.staff_eqp = item
            self.AddItemStats(self.staff_eqp)

        self.hp_cur = math.ceil(self.hp * hp_pct)
        self.mana_cur = math.ceil(self.mana * mana_pct)
        self.CheckMaxStats()
        return "item equipped"

    def AddItemStats(self, item):
        # Updates the player's stats for the item's stat mods
        # and marks the item as equipped

        if item is not None:
            self.hp += item.hp_mod
            self.defense += item.def_mod
            self.def_cur += item.def_mod
            self.atk += item.atk_mod
            self.atk_cur += item.atk_mod
            self.mag += item.mag_mod
            self.mag_cur += item.mag_mod
            self.mana += item.mana_mod
            item.equipped = True

    def RemoveItemStats(self, item):
        # Updates the player's stats for the item's stat mods
        # and marks the item as unequipped

        if item is not None:
            self.hp -= item.hp_mod
            self.defense -= item.def_mod
            self.def_cur -= item.def_mod
            self.atk -= item.atk_mod
            self.atk_cur -= item.atk_mod
            self.mag -= item.mag_mod
            self.mag_cur -= item.mag_mod
            self.mana -= item.mana_mod
            item.equipped = False

    def CheckMaxStats(self):
        # Verifies current HP and mana are not greater than allowed

        if self.hp_cur > self.hp:
            self.hp_cur = self.hp

        if self.mana_cur > self.mana:
            self.mana_cur = self.mana

    def CastSpell(self, name):
        spell = self.inventory.GetItem(name)
        return spell.Cast()
