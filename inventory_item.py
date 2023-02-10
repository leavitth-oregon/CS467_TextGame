import math

class InventoryItem:
    def __init__(self, name, description, item_type, equippable, equipped, cost, synonym):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.equippable = equippable
        self.equipped = equipped
        self.cost = cost
        self.synonym = synonym


class Gear(InventoryItem):
    def __init__(self, name, description, item_type, equippable, equipped, cost, synonym,
                 hp_mod, atk_mod, def_mod, mag_mod, mana_mod):
        super().__init__(name, description, item_type, equippable, equipped, cost, synonym)
        self.hp_mod = hp_mod
        self.atk_mod = atk_mod
        self.def_mod = def_mod
        self.mag_mod = mag_mod
        self.mana_mod = mana_mod


class Spell(InventoryItem):
    def __init__(self, name, description, item_type, equippable, equipped, cost, synonym,
                 mana_cost, base_dmg, duration, casts, lvl_up):
        super().__init__(name, description, item_type, equippable, equipped, cost, synonym)
        self.mana_cost = mana_cost
        self.base_dmg = base_dmg
        self.duration = duration
        self.casts = casts
        self.lvl_up = lvl_up

    def Cast(self):
        self.casts += 1
        return self.base_dmg * (math.ceil(self.casts / self.lvl_up))



class Item(InventoryItem):
    def __init__(self, name, description, item_type, equippable, equipped, cost, synonym,
                 qty, hp_mod, mana_mod):
        super().__init__(name, description, item_type, equippable, equipped, cost, synonym)
        self.qty = qty
        self.hp_mod = hp_mod
        self.mana_mod = mana_mod
