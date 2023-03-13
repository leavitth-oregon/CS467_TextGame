from title_screen import *
from inventory import *
from commands import *
from fugue_map import *
from fugue_jukebox import *
import os

# put original files, which will not be edited in here
ogfiles = []

# put the copy of the files for the save in here, which will be edited
savefiles = []

my_map = Fugue_Map()
my_map.prep_data()

jukebox = Jukebox()

my_inventory = inventory.Inventory()
current_room = my_map.desert_camp
# os.system('cls')
current_room = title_screen(my_map, jukebox)
player_prompt()
