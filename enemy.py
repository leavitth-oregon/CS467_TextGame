import math
from character import Character


class Enemy(Character):
    def __init__(self, hp, defense, atk, mag, mana, name):
        super().__init__(hp, defense, atk, mag, mana)
        self.name = name
