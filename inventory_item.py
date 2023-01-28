class InventoryItem:
    def __init__(self, name, description, item_type, equipable, equipped, cost):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.equipable = equipable
        self.equipped = equipped
        self.cost = cost


class Gear(InventoryItem):
    def __init__(self, name, description, item_type, equipable, equipped, cost,
                 hp_mod, atk_mod, def_mod, mag_mod, mana_mod):
        super().__init__(name, description, item_type, equipable, equipped, cost)
        self.hp_mod = hp_mod
        self.atk_mod = atk_mod
        self.def_mod = def_mod
        self.mag_mod = mag_mod
        self.mana_mod = mana_mod


class Spell(InventoryItem):
    def __init__(self, name, description, item_type, equipable, equipped, cost,
                 mana_cost, hp_mod, atk_mod, def_mod, mag_mod, dmg_per_turn,
                 duration, effect, effect_pct, casts, lvl, lvl_reqs):
        super().__init__(name, description, item_type, equipable, equipped, cost)
        self.mana_cost = mana_cost
        self.hp_mod = hp_mod
        self.atk_mod = atk_mod
        self.def_mod = def_mod
        self.mag_mod = mag_mod
        self.dmg_per_turn = dmg_per_turn
        self.duration = duration
        self.effect = effect
        self.effect_pct = effect_pct
        self.casts = casts
        self.lvl = lvl
        self.lvl_reqs = lvl_reqs


class Item(InventoryItem):
    def __init__(self, name, description, item_type, equipable, equipped, cost,
                 qty, hp_mod, mana_mod):
        super().__init__(name, description, item_type, equipable, equipped, cost)
        self.qty = qty
        self.hp_mod = hp_mod
        self.mana_mod = mana_mod
