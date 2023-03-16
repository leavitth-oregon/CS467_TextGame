import title_screen
import inventory
import commands
import fugue_map
import os

my_map = fugue_map.Fugue_Map()
my_map.prep_data()


my_inventory = inventory.Inventory()
current_room = my_map.desert_camp
os.system('cls')
title_screen.title_screen()
commands.player_prompt()
