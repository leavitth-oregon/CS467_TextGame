import title_screen
import inventory
import commands
import fugue_map
import os


my_inventory = inventory.Inventory()
current_room = fugue_map.campfire
os.system('cls')
title_screen.title_screen()
commands.player_prompt()
