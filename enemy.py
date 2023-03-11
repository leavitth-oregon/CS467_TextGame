import random
from character import Character


class Enemy(Character):
    def __init__(self, hp, defense, atk, mag, mana, name, prize, image):
        super().__init__(hp, defense, atk, mag, mana)
        self.name = name
        self.prize = prize
        self.image = image

    def GetAction(self):
        run_val = random.randrange(0, 10, 1)
        if run_val < 6:
            return "attack"

        return "defend"

    def PrintImage(self):
        print(self.image)
