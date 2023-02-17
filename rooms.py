import ascii_art
import inventory_item


class Room:
    def __init__(self):
        self.name = ""
        self.description = None
        self.short_desc = None
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.ascii_art = None
        self.room_items = []
        self.NPCs = None
        self.item_description = None
        self.been_to = False
        self.in_current_room = False


woods_path = Room()
campfire = Room()
rooms_list = [campfire, woods_path]


# #######  CAMPFIRE LEVEL  ################################################################################
campfire.name = "campfire"
campfire.room_items = [inventory_item.backpack, inventory_item.tree, inventory_item.sword]
campfire.north = woods_path
campfire.ascii_art = ascii_art.campfire
campfire.description = "You slowly open your eyes. There's a campfire glowing brightly that blinds you. " \
                       "When your eyes finally adjust, you see your backpack hanging on a tree limb, swinging " \
                       "ever so gently as a soft breeze blows from the North.\n"

campfire.short_desc = "A big tree with strong branches glows in the light of the campfire.\n"
campfire.in_current_room = True

# #######  WOODS_PATH LEVEL  #####################################################################################

woods_path.south = campfire
woods_path.name = "Woods path"
woods_path.description = "You head up a beaten path you see in the woods..."
woods_path.ascii_art = ascii_art.woods_path


