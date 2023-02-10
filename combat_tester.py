import unittest
from setup_test_classes import MakePlayer, MakeEnemy
from combat import Combat


class TestCases(unittest.TestCase):

    def test_1(self):  # Verify player action
        player = MakePlayer()
        spider = MakeEnemy()
        fight = Combat(player, spider)
        self.assertTrue(fight._VerifyValidAction(["attack", "spell"]))
        self.assertTrue(fight._VerifyValidAction(["defend"]))
        self.assertTrue(fight._VerifyValidAction(["cast", "Fire Ball"]))
        self.assertTrue(fight._VerifyValidAction(["run", "spell"]))
        self.assertFalse(fight._VerifyValidAction(["cast", "Fire"]))
        self.assertFalse(fight._VerifyValidAction(["cast"]))
        self.assertFalse(fight._VerifyValidAction(["swim", "Fire"]))

    def test_2(self): # Attacks
        player = MakePlayer()
        spider = MakeEnemy()
        fight = Combat(player, spider)
        fight._PerformAction(["attack"], player, spider)
        fight._PerformAction(["attack"], spider, player)
        self.assertTrue(spider.hp_cur == 91)
        self.assertTrue(player.hp_cur == 42)

    def test_3(self): # Defends
        player = MakePlayer()
        spider = MakeEnemy()
        fight = Combat(player, spider)
        fight._PerformAction(["defend"], player, spider)
        fight._PerformAction(["defend"], spider, player)
        self.assertTrue(spider.def_cur == 11)
        self.assertTrue(player.def_cur == 22)

    def test_4(self): # Cast spell
        player = MakePlayer()
        fb = player.inventory.GetItem("Fire Ball")
        spider = MakeEnemy()
        fight = Combat(player, spider)
        fight._PerformAction(["cast", "Fire Ball"], player, spider)
        self.assertTrue(spider.hp_cur == 90)
        self.assertTrue(fb.casts == 1)
