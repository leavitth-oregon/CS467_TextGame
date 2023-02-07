import math
import random


class Character:
    def __init__(self, hp, defense, atk, mag, mana):
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

    def DealDamage(self, dmg):
        self.hp_cur -= dmg

    def Defend(self):
        def_added = math.ceil(self.def_cur * 0.1)
        self.def_cur += def_added
        return def_added

    def Run(self):
        run_val = random.randrange(0, 10, 1)
        if run_val < 3:
            return False

        return True