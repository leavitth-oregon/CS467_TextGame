from inventory import Inventory
from inventory_item import Gear, Spell, Item
from player import Player

def MakePlayer():
    return Player(
        inventory = MakeInventory(),
        hp = 50,
        defense = 20,
        atk = 10,
        mag = 10, 
        mana = 10, 
        sword_eqp = None, 
        armor_eqp = None, 
        staff_eqp = None
    )


def MakeInventory():
    sword1 = Gear(
        name="Wooden Sword",
        description="A stick found on the ground",
        item_type="sword",
        equipable=True,
        equipped=False,
        cost=10,
        hp_mod=0,
        atk_mod=5,
        def_mod=0,
        mag_mod=0,
        mana_mod=0)
    sword2 = Gear(
        name="Long Sword",
        description="A long sword",
        item_type="sword",
        equipable=True,
        equipped=False,
        cost=40,
        hp_mod=5,
        atk_mod=20,
        def_mod=0,
        mag_mod=0,
        mana_mod=0)
    sword3 = Gear(
        name="Katana",
        description="A magical katana",
        item_type="sword",
        equipable=True,
        equipped=False,
        cost=50,
        hp_mod=0,
        atk_mod=10,
        def_mod=0,
        mag_mod=5,
        mana_mod=20)
    sword4 = Gear(
        name="King's Sword",
        description="The sword of the true king",
        item_type="sword",
        equipable=True,
        equipped=False,
        cost=500,
        hp_mod=20,
        atk_mod=50,
        def_mod=10,
        mag_mod=10,
        mana_mod=30)
    armor1 = Gear(
        name="Cloth Armor",
        description="Tattered rags sewn together",
        item_type="armor",
        equipable=True,
        equipped=False,
        cost=10,
        hp_mod=10,
        atk_mod=0,
        def_mod=5,
        mag_mod=0,
        mana_mod=0)
    armor2 = Gear(
        name="King's Armor",
        description="The finest armor in the kingdom",
        item_type="armor",
        equipable=True,
        equipped=False,
        cost=500,
        hp_mod=100,
        atk_mod=20,
        def_mod=50,
        mag_mod=10,
        mana_mod=30)
    staff1 = Gear(
        name="Weathered Staff",
        description="Looks like there may still be a spark of magic left ",
        item_type="staff",
        equipable=True,
        equipped=False,
        cost=10,
        hp_mod=0,
        atk_mod=0,
        def_mod=0,
        mag_mod=5,
        mana_mod=5)
    staff2 = Gear(
        name="Royal Staff",
        description="Able to cast magic only known to the royal family",
        item_type="staff",
        equipable=True,
        equipped=False,
        cost=10,
        hp_mod=20,
        atk_mod=20,
        def_mod=20,
        mag_mod=100,
        mana_mod=50)
    spell1 = Spell(
        name="Fire Ball",
        description="Sends a ball of fire from your staff",
        item_type="spell",
        equipable=False,
        equipped=False,
        cost=10,
        mana_cost=10,
        hp_mod=0,
        atk_mod=0,
        def_mod=0,
        mag_mod=5,
        dmg_per_turn=[10, 15, 25],
        duration=1,
        effect="burn",
        effect_pct=[5, 10, 20],
        casts=0,
        lvl=1,
        lvl_reqs=[0, 25, 50])
    item1 = Item(
        name="Health Potion",
        description="Restores 25 health",
        item_type="item",
        equipable=False,
        equipped=False,
        cost=20,
        qty=5,
        hp_mod=25,
        mana_mod=0)
    item2 = Item(
        name="Mana Potion",
        description="Restores 25 mana",
        item_type="item",
        equipable=False,
        equipped=False,
        cost=20,
        qty=3,
        hp_mod=0,
        mana_mod=25)
    item3 = Item(
        name="Tattered Photo",
        description="A damaged photo that appears to show two people",
        item_type="item",
        equipable=False,
        equipped=False,
        cost=0,
        qty=1,
        hp_mod=0,
        mana_mod=0)
    item4 = Item(
        name="Everburning Lamp",
        description="A lamp that never extinguishes",
        item_type="item",
        equipable=False,
        equipped=False,
        cost=0,
        qty=1,
        hp_mod=0,
        mana_mod=0)
    item5 = Item(
        name="King's Crown",
        description="The crown of the king",
        item_type="item",
        equipable=False,
        equipped=False,
        cost=0,
        qty=1,
        hp_mod=0,
        mana_mod=0)
    inv = Inventory()
    inv.AddItem(sword1)
    inv.AddItem(sword2)
    inv.AddItem(sword3)
    inv.AddItem(sword4)
    inv.AddItem(armor1)
    inv.AddItem(armor2)
    inv.AddItem(staff1)
    inv.AddItem(staff2)
    inv.AddItem(spell1)
    inv.AddItem(item1)
    inv.AddItem(item2)
    inv.AddItem(item3)
    inv.AddItem(item4)
    inv.AddItem(item5)
    return inv
