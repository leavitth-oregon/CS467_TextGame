import json

from inventory import Inventory
from inventory_item import Gear, Spell, Item
from player import Player
from enemy import Enemy
from combat import Combat


def GetItemsFileInfo(f_name):
    # import item data from item json file
    with open(f_name) as in_file:
        unparsed_items = in_file.read()

        # parse the json data into a directory in Python format
        parsed_items = json.loads(unparsed_items)

    return parsed_items


def GetSpellsFileInfo(f_name):
    # import spell data from spell json file
    with open(f_name) as in_file:
        unparsed_spells = in_file.read()

        # parse the json data into a directory in Python format
        parsed_spells = json.loads(unparsed_spells)

    return parsed_spells


def GetEnemiesFileInfo(f_name):
    # import item data from item json file
    with open(f_name) as in_file:
        unparsed_enemies = in_file.read()

        # parse the json data into a directory in Python format
        parsed_enemies = json.loads(unparsed_enemies)

    return parsed_enemies


def CreateInventory(items, spells):
    inv = Inventory()
    for key in items:
        if items[key]["item_type"] == "item":
            inv_item = Item(
                name=items[key]["name"],
                synonym=items[key]["synonym"].split(', '),
                description=items[key]["description"],
                item_type=items[key]["item_type"],
                equippable=items[key]["equippable"],
                equipped=items[key]["equipped"],
                cost=int(items[key]["cost"]),
                qty=int(items[key]["qty"]),
                hp_mod=int(items[key]["hp_mod"]),
                mana_mod=int(items[key]["mana_mod"])
            )
        else:
            inv_item = Gear(
                name=items[key]["name"],
                synonym=items[key]["synonym"].split(', '),
                description=items[key]["description"],
                item_type=items[key]["item_type"],
                equippable=items[key]["equippable"],
                equipped=items[key]["equipped"],
                cost=int(items[key]["cost"]),
                hp_mod=int(items[key]["hp_mod"]),
                atk_mod=int(items[key]["atk_mod"]),
                def_mod=int(items[key]["def_mod"]),
                mag_mod=int(items[key]["mag_mod"]),
                mana_mod=int(items[key]["mana_mod"])
            )

        inv.AddItem(inv_item)

    for key in spells:
        inv_spell = Spell(
            name=spells[key]["name"],
            synonym=spells[key]["synonym"].split(', '),
            description=spells[key]["description"],
            item_type=spells[key]["item_type"],
            equippable=spells[key]["equippable"],
            equipped=spells[key]["equipped"],
            cost=int(spells[key]["cost"]),
            mana_cost=int(spells[key]["mana_cost"]),
            duration=int(spells[key]["duration"]),
            casts=int(spells[key]["casts"]),
            lvl_up=int(spells[key]["lvl_up"]),
            base_dmg=int(spells[key]["base_dmg"])
        )

        inv.AddItem(inv_spell)

    return inv


def SetUpPlayer(item_set):
    items = GetItemsFileInfo("items.json")
    spells = GetSpellsFileInfo("Spellbook.json")

    player = Player(
        inventory=CreateInventory(items=items, spells=spells),
        hp=20,
        defense=10,
        atk=10,
        mag=10,
        mana=30,
        sword_eqp=None,
        armor_eqp=None,
        staff_eqp=None,
        money=50
    )

    if item_set == 1:
        player.EquipItem("Wooden Sword")
        player.EquipItem("Cloth Armor")
        player.EquipItem("Weathered Staff")

    if item_set == 2:
        player.EquipItem("War Hammer")
        player.EquipItem("Chainmail")
        player.EquipItem("Wand")

    if item_set == 3:
        player.EquipItem("Katana")
        player.EquipItem("Wizard's Robe")
        player.EquipItem("Wand")

    return player


def SetUpEnemies():
    all_enemies = []
    enemies = GetItemsFileInfo("enemies.json")

    for key in enemies:
        enemy = Enemy(
            name=enemies[key]["name"],
            hp=enemies[key]["hp"],
            atk=enemies[key]["atk"],
            defense=enemies[key]["defense"],
            mag=enemies[key]["mag"],
            mana=enemies[key]["mana"],
            prize=enemies[key]["prize"]
        )

        all_enemies.append(enemy)

    return all_enemies


if __name__ == "__main__":
    player = SetUpPlayer(2)
    enemies = SetUpEnemies()
    battle = Combat(player=player, enemy=enemies[5])
    battle.StartCombat()
    print()
