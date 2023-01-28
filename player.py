import math


class Player:
  def __init__(self, inventory, hp, defense, atk, mag, mana, 
  sword_eqp, armor_eqp, staff_eqp):
    self.inventory = inventory
    self.hp = hp
    self.hp_cur = hp
    self.defense = defense
    self.def_cur = defense
    self.atk = atk
    self.atk_cur = atk
    self.mag = mag
    self.mag_cur = mag
    self.mana = mana
    self.mana_cur = mana
    self.sword_eqp = sword_eqp
    self.armor_eqp = armor_eqp
    self.staff_eqp = staff_eqp
    

  def EquipItem(self, name):
    # Equips item from player's inventory and updates player's stats
    #
    # Output:
    # "item not found" - name of desired item not found in player's inventory
    # "item not equipable" - item is not allowed to be equipped
    # "item equiped" - item was successfully equipped

    item = self.inventory.GetItem(name)

    if item == None:
      return "item not found"
    
    if not item.equipable:
      return "item not equipable"

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

    if not item == None:
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

    if not item == None:
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
