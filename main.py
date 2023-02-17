import title_screen
import rooms
import inventory
import commands


my_inventory = inventory.Inventory()
current_room = rooms.Room()

title_screen.title_screen()
commands.player_prompt()
