import title_screen
import inventory
import commands
import fugue_map


my_inventory = inventory.Inventory()
current_room = fugue_map.campfire

title_screen.title_screen()
commands.player_prompt()
