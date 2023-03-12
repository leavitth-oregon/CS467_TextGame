"""
Fugue Map 
Hayley Leavitt 2023
Version 3.0


"""

# libraries
import json
from fugue_jukebox import Jukebox

# global variables
location_file = "fugue_locations.json"
npc_file = "npc.json"
enemy_file = "enemies.json"
item_file = "items.json"
game_files = [location_file, npc_file, enemy_file, item_file]
jukebox = Jukebox()

def get_file_info(nfile) -> dict:
    """
    :param nfile: the json file where the data is stored
    :return parsed_info: a directory containing the parsed data inside the nfile json file

    Uses json.loads() to read a json file and convert it into a directory in python format. This allows
    the data to be stored externally in a JSON file.
    """
    # import location data from location json file
    with open(nfile) as in_file:
        unparsed_info = in_file.read()

        # parse the json data into a directory in Python format
        parsed_info = json.loads(unparsed_info)

    return parsed_info

def save_file_info(ofile, file_dict) -> None: 
    # prep info for json writing
    json_object = json.dumps(file_dict, indent = 4)

    # write the info to the json file
    with open(ofile) as out_file:
        out_file.write(file_dict)


class Fugue_NPC: 
    def __init__(self, id:str) -> None: 
        self.id = id
        self.aliases = None
        self.name = None
        self.description = None
        self.location = None 
        self.is_impostor = False
        self.dialogue = None

    def load_info(self, npc_info:dict) -> None: 
        self.aliases = npc_info.get("aliases")
        self.name = npc_info.get("name")
        self.description = npc_info.get("description")
        self.location = npc_info.get("location") 
        self.is_impostor = npc_info.get("is_impostor")
        self.dialogue = npc_info.get("dialogue")

    def talk_to(self, keyword) -> str: 
        says = self.dialogue.get("other")

        if keyword in self.dialogue: 
            says = self.dialogue.get(keyword)

        return says


class Fugue_Location:
    def __init__(self, name: str) -> None:
        """
        :param name: the string name of the location
        :returns None:

        Sets up all the variables of the location
        """
        self.name = name
        self.is_start = False
        self.is_current_location = False

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.times_visited = 0
        self.was_forgotten = False

        self.long_description = ""
        self.short_description = ""
        self.forgotten_description = ""
        self.ascii_art = ""

        self.features = {}
        self.npcs = {}
        self.enemies = {}
        self.items = {}

        return 

    def load_info(self, location_info: dict) -> None:
        """
        :param location_info: a dictionary that contains the json data to be loaded into the location variables
        """
        # load game info
        self.is_start    = location_info.get("is_start")
        self.is_current_location = location_info.get("is_current_location")

        # load location descriptions 
        self.long_description      = location_info.get("long_description")
        self.short_description     = location_info.get("short_description")
        self.forgotten_description = location_info.get("forgotten_description")
        
        # load the location art
        self.ascii_art = location_info.get("ascii_art")
        self.song = location_info.get("song")

        # load location features, etc. 
        self.features = location_info.get("features")
        self.npcs     = location_info.get("npcs")
        self.enemies  = location_info.get("enemies")
        self.items    = location_info.get("items")

        return

    def get_description(self) -> str:
        """
        :param self: the location
        :return location_description: the string description of the location being visited, relative to when and how it
        is being visited
        """
        location_description = self.short_description

        if (self.times_visited <= 0) and (self.was_forgotten is False):
            location_description = self.long_description
        elif (self.times_visited <= 0) and (self.was_forgotten is True): 
            location_description = self.forgotten_description
        else:
            location_description = self.short_description

        return location_description

    def get_direction(self, direction: str) -> str:
        """
        :param direction: the input requesting what is in a certain direction
        :return location_info:
        """
        # convert the direction info into all lower case for easier parsing
        direction = direction.lower()

        if (direction == "north") or (direction == "up"):
            location_info = self.north
        elif (direction == "east") or (direction == "right"):
            location_info = self.east
        elif (direction == "south") or (direction == "down"):
            location_info = self.south
        elif (direction == "west") or (direction == "left"):
            location_info = self.west
        else:
            location_info = "There doesn't seem to be anything in that direction..."

        return location_info

    def is_npc_here(self, npc_name: str) -> bool:
        """
        :param npc_name: a string input of the name or identifier of an NPC
        :return bool: return a true or false depending on whether the NPC is found or not
        """
        if npc_name in self.npcs:
            return True
        else:
            return False

    def is_item_here(self, item: str) -> bool:
        """
        :param itme: a string input of the name or identifier of an item
        :return bool: return a true or false depending on whether the item is found or not
        """
        if item in self.items:
            return True
        else:
            return False

    def been_to(self) -> bool: 
        if self.times_visited > 0:
            return True
        else:
            return False
        
    def play_music(self) -> None: 
        jukebox.stop_song()
        jukebox.play_song(self.song)


class Fugue_Map:
    def __init__(self) -> None:
        """
        Sets up all of the variables for the map object, including all of the locations
        """
        # create all locations in the map
        self.desert_camp       = Fugue_Location("desert camp")
        self.desert_wilderness = Fugue_Location("desert wilderness")
        self.path_1            = Fugue_Location("path 1")
        self.path_2            = Fugue_Location("path 2")
        self.path_3            = Fugue_Location("path 3")
        self.city_gates        = Fugue_Location("city gates")
        self.city_road_1       = Fugue_Location("city road 1")
        self.city_road_2       = Fugue_Location("city road 2")
        self.city_road_3       = Fugue_Location("city road 3")
        self.palace_walls      = Fugue_Location("palace walls")
        self.marketplace       = Fugue_Location("marketplace")
        self.secret_passage    = Fugue_Location("secret passage")
        self.gardens           = Fugue_Location("gardens")
        self.well              = Fugue_Location("well")
        self.tower             = Fugue_Location("tower")
        self.bedroom           = Fugue_Location("bedroom")
        self.great_hall        = Fugue_Location("great hall")
        self.throne_room       = Fugue_Location("throne room")
        self.dining_hall       = Fugue_Location("dining hall")

        # link all of the locations in the map 
        self.desert_camp.north = self.path_1
        self.desert_camp.east  = self.desert_wilderness
        self.desert_camp.south = self.desert_wilderness
        self.desert_camp.west  = self.desert_wilderness

        self.desert_wilderness.north = self.desert_camp
        self.desert_wilderness.east  = self.desert_camp
        self.desert_wilderness.west  = self.desert_camp

        self.path_1.north = self.path_2
        self.path_1.south = self.desert_camp
        
        self.path_2.north = self.path_3
        self.path_2.south = self.path_1

        self.path_3.north = self.city_gates
        self.path_3.south = self.path_2

        self.city_gates.north = self.city_road_2
        self.city_gates.south = self.path_3

        self.city_road_1.north = self.secret_passage
        self.city_road_1.west = self.city_road_2

        self.city_road_2.north = self.palace_walls
        self.city_road_2.east  = self.city_road_3
        self.city_road_2.south = self.city_gates
        self.city_road_2.west  = self.city_road_1

        self.city_road_3.north = self.marketplace
        self.city_road_3.west  = self.city_road_2

        self.palace_walls.south = self.city_road_2
        self.palace_walls.west  = self.marketplace

        self.marketplace.south = self.city_road_3
        self.marketplace.west  = self.palace_walls

        self.secret_passage.north = self.gardens
        self.secret_passage.south = self.city_road_1

        self.gardens.east  = self.tower
        self.gardens.south = self.secret_passage
        self.gardens.west  = self.well

        self.well.east = self.gardens
        
        self.tower.west  = self.gardens
        self.tower.north = self.great_hall
        self.tower.east = self.bedroom

        self.great_hall.north = self.throne_room
        self.great_hall.east  = self.dining_hall
        self.great_hall.south = self.tower

        self.dining_hall.west = self.great_hall

        self.throne_room.south = self.great_hall

        # create location tracking data
        self.start   = self.desert_camp
        self.current = self.start

        # create a key for the dictionary
        self.map_key = ["desert_camp",
                        "desert_wilderness",
                        "path_1",
                        "path_2",
                        "path_3",
                        "city_gates",
                        "city_road_1",
                        "city_road_2",
                        "city_road_3",
                        "palace_walls", 
                        "marketplace",
                        "secret_passage", 
                        "gardens",
                        "well",
                        "tower",
                        "bedroom",
                        "great_hall", 
                        "throne_room",
                        "dining_hall"]

        # create an array of our locations
        self.map_array = [self.desert_camp, 
                          self.desert_wilderness, 
                          self.path_1, 
                          self.path_2, 
                          self.path_3, 
                          self.city_gates, 
                          self.city_road_1, 
                          self.city_road_2, 
                          self.city_road_3, 
                          self.palace_walls, 
                          self.marketplace, 
                          self.secret_passage, 
                          self.gardens, 
                          self.well, 
                          self.tower, 
                          self.bedroom, 
                          self.great_hall, 
                          self.throne_room, 
                          self.dining_hall]
        
        # create all of our npcs
        self.impostor = Fugue_NPC("Impostor")
        self.city_gate_guard = Fugue_NPC("City Gate Guard")
        self.city_guide = Fugue_NPC("City Guide")
        self.little_boy = Fugue_NPC("Little Boy")
        self.wizard = Fugue_NPC("Wizard")
        self.merchant = Fugue_NPC("Merchant")
        self.person_in_mirror = Fugue_NPC("Person in the Mirror")
        self.soldier_ghost = Fugue_NPC("Soldier Ghost")

        # create an array of our npcs ids and npc objects
        self.npc_ids = ["Impostor", "City Gate Guard", "City Guide", "Little Boy", "Wizard", "Merchant", "Person in the Mirror", "Soldier Ghost"]
        self.npc_array = [self.impostor, self.city_gate_guard, self.city_guide, self.little_boy, self.wizard, self.merchant, self.person_in_mirror, self.soldier_ghost]

        return
    
    def prep_data(self) -> None:
        """
        :param map_dictionary: a dictionary that contains all of the json data that has not yet been prepared to be loaded into the location variables 
        """
        # get the data from the original location json file (template)
        map_dictionary = get_file_info(game_files[0])
        npc_dictionary = get_file_info(game_files[1])

        # fill in the location data, correcting strings to objects as needed
        for i in range(len(self.map_array)):
            location = self.map_array[i]
            location_name = self.map_key[i]
            location.load_info(map_dictionary.get(location_name))

        # fill in the npc data
        for i in range(len(self.npc_array)): 
            npc = self.npc_array[i]
            npc.location(npc_dictionary.get(self.npc_ids[i]))
        
        return
    
    def save_map(self):
        # Converts the contents of the inventory into JSON format and saves to inventory.json

        # Create dictionaries to store inventory that will be converted to JSON
        location_dict = {}
        npc_dict = {}

        # Add locations to dictionary
        for item in self.map_array:
            info = {
                "name": item.name,
                "song" : item.song, 
                "is_start": item.is_start,
                "is_current_location": item.is_current_location,
                "north": item.north,
                "east": item.east,
                "south": item.south,
                "west": item.west,
                "times_visited": item.times_visited,
                "was_forgotten": item.was_forgotten,
                "long_description": item.long_description,
                "short_description": item.short_description,
                "forgotten_description": item.forgotten_description, 
                "ascii_art": item.ascii_art, 
                "features": item.features, 
                "npcs": item.npcs,
                "enemies": item.enemies, 
                "items": item.items
                }

            location_dict[item.name] = info

        # Add npcs to dictionary
        for item in self.npc_array:
            info = {
                "name": item.name,
                "aliases": item.aliases,
                "description": item.description,
                "location": item.location,
                "is_impostor": item.is_impostor,
                "dialogue": item.dialogue
                }

            npc_dict[item.name] = info

        loc_json = json.dumps(location_dict, indent=4)
        npc_json = json.dumps(npc_dict, indent=4)

        with open("fugue_locations.json", "w") as outfile:
            outfile.write(loc_json)

        with open("npc.json", "w") as outfile: 
            outfile.write(npc_json)


def main():
    my_map = Fugue_Map()
    my_map.prep_data()
    my_map.print_info()
    return


if __name__ == "__main__":
    main()
