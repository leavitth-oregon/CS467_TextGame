import math
from character import Character


class Enemy(Character):
    def __init__(self, hp, defense, atk, mag, mana, name, prize):
        super().__init__(hp, defense, atk, mag, mana)
        self.name = name
        self.prize = prize
