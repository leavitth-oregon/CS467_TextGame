import unittest
from setup_test_classes import MakeInventory, MakePlayer


class TestCases(unittest.TestCase):

    def test_1(self):  # Test adding items
        inv = MakeInventory()
        self.assertTrue(len(inv.swords) == 4)
        self.assertTrue(len(inv.armors) == 2)
        self.assertTrue(len(inv.staffs) == 2)
        self.assertTrue(len(inv.spells) == 1)
        self.assertTrue(len(inv.items) == 5)

    def test_2(self):  # Test removing items
        inv = MakeInventory()
        self.assertTrue(len(inv.swords) == 4)
        self.assertTrue(len(inv.armors) == 2)
        self.assertTrue(len(inv.staffs) == 2)
        self.assertTrue(len(inv.spells) == 1)
        self.assertTrue(len(inv.items) == 5)
        sword = inv.GetItem("Katana")
        inv.RemoveItem(sword)
        self.assertTrue(len(inv.swords) == 3)
        self.assertTrue(len(inv.armors) == 2)
        self.assertTrue(len(inv.staffs) == 2)
        self.assertTrue(len(inv.spells) == 1)
        self.assertTrue(len(inv.items) == 5)

    def test_3(self):  # Test display strings
        inv = MakeInventory()
        self.assertTrue(inv.DisplayItemList(inv.swords, True) ==
                        "Wooden Sword        Long Sword          Katana              King's Sword        ")
        self.assertTrue(inv.DisplayItemList(inv.armors, True) ==
                        "Cloth Armor         King's Armor        ")
        self.assertTrue(inv.DisplayItemList(inv.staffs, True) ==
                        "Weathered Staff     Royal Staff         ")
        self.assertTrue(inv.DisplayItemList(inv.spells, True) ==
                        "Fire Ball           ")
        self.assertTrue(inv.DisplayItemList(inv.items, True) ==
                        "Health Potion (5)   Mana Potion (3)     Tattered Photo      Everburning Lamp    \nKing's Crown        ")

    def test_4(self):  # Test player is created
        player = MakePlayer()
        self.assertTrue(player.hp == 50)
        self.assertTrue(player.hp_cur == 50)
        self.assertTrue(player.defense == 20)
        self.assertTrue(player.def_cur == 20)
        self.assertTrue(player.atk == 10)
        self.assertTrue(player.atk_cur == 10)
        self.assertTrue(player.mag == 10)
        self.assertTrue(player.mag_cur == 10)
        self.assertTrue(player.mana == 10)
        self.assertTrue(player.mana_cur == 10)
        self.assertTrue(player.sword_eqp is None)
        self.assertTrue(player.armor_eqp is None)
        self.assertTrue(player.staff_eqp is None)

    def test_5(self):  # Test equipping items
        player = MakePlayer()
        player.EquipItem("Long Sword")
        player.EquipItem("Cloth Armor")
        player.EquipItem("Royal Staff")
        self.assertTrue(player.hp == 85)
        self.assertTrue(player.hp_cur == 85)
        self.assertTrue(player.defense == 45)
        self.assertTrue(player.def_cur == 45)
        self.assertTrue(player.atk == 50)
        self.assertTrue(player.atk_cur == 50)
        self.assertTrue(player.mag == 110)
        self.assertTrue(player.mag_cur == 110)
        self.assertTrue(player.mana == 60)
        self.assertTrue(player.mana_cur == 60)
        self.assertTrue(player.sword_eqp == player.inventory.GetItem("Long Sword"))
        self.assertTrue(player.armor_eqp == player.inventory.GetItem("Cloth Armor"))
        self.assertTrue(player.staff_eqp == player.inventory.GetItem("Royal Staff"))

    def test_6(self):  # Test changing items
        player = MakePlayer()
        player.EquipItem("Long Sword")
        player.EquipItem("Cloth Armor")
        player.EquipItem("Royal Staff")
        player.EquipItem("Wooden Sword")
        player.EquipItem("King's Armor")
        player.EquipItem("Weathered Staff")
        self.assertTrue(player.hp == 150)
        self.assertTrue(player.hp_cur == 150)
        self.assertTrue(player.defense == 70)
        self.assertTrue(player.def_cur == 70)
        self.assertTrue(player.atk == 35)
        self.assertTrue(player.atk_cur == 35)
        self.assertTrue(player.mag == 25)
        self.assertTrue(player.mag_cur == 25)
        self.assertTrue(player.mana == 45)
        self.assertTrue(player.mana_cur == 45)
        self.assertTrue(player.sword_eqp == player.inventory.GetItem("Wooden Sword"))
        self.assertTrue(player.armor_eqp == player.inventory.GetItem("King's Armor"))
        self.assertTrue(player.staff_eqp == player.inventory.GetItem("Weathered Staff"))

    def test_7(self):  # Test equipped items are displayed
        player = MakePlayer()
        player.EquipItem("Long Sword")
        player.EquipItem("Cloth Armor")
        player.EquipItem("Royal Staff")
        inv = player.inventory
        self.assertTrue(inv.DisplayItemList(inv.swords, True) ==
                        "Wooden Sword        Long Sword (E)      Katana              King's Sword        ")
        self.assertTrue(inv.DisplayItemList(inv.armors, True) ==
                        "Cloth Armor (E)     King's Armor        ")
        self.assertTrue(inv.DisplayItemList(inv.staffs, True) ==
                        "Weathered Staff     Royal Staff (E)     ")
        self.assertTrue(inv.DisplayItemList(inv.spells, True) ==
                        "Fire Ball           ")
        self.assertTrue(inv.DisplayItemList(inv.items, True) ==
                        "Health Potion (5)   Mana Potion (3)     Tattered Photo      Everburning Lamp    \nKing's Crown        ")