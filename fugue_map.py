# libraries
import json

# global variables
game_num = 0
game_files = ['locations.json']
current_location = None

def get_location_file_info(locfile) -> dict:
    """
    :param locfile: the json file where the location data is stored
    :return parsed_locations: a directory containing the parsed data inside the locations json file

    Uses json.loads() to read a json file and convert it into a directory in python format. This allows
    the data to be stored externally in a JSON file.
    """
    # import location data from location json file
    with open(locfile) as in_file:
        unparsed_locations = in_file.read()

        # parse the json data into a directory in Python format
        parsed_locations = json.loads(unparsed_locations)

    return parsed_locations

def create_location_file(location_data, game_number: int) -> None:
    """
    :arg location_data: a directory that contains the location data we want to write to a file
    :arg game_number: the number of the game we are creating a file for
    :return None:

    Uses open() to create a new location json file with the current data

    Source:
    https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    """
    # create a new game file
    file_name = "locations" + str(game_number) + ".json"
    new_file = open(file_name, "x")

    if new_file:
        # parse the dictionary into a json object
        location_json = json.dumps(location_data, indent = 2)

        # dump the data in json format into the json file
        with open(file_name, "w") as outfile:
            outfile.write(location_json)

    return 


class Fugue_Location:
    def __init__(self, name: str) -> None:
        """
        :param name: the string name of the location
        :returns None:

        Sets up all the variables of the location
        """
        self.game_number = 0

        self.name = name
        self.is_start = False

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.times_visited = 0
        self.was_forgotten = False

        self.long_description = ""
        self.short_description = ""
        self.forgotten_description = ""

        self.features = {}
        self.npcs = {}
        self.items = {}

        self.location_array = (self.game_number, self.name, self.is_start, self.north, self.east, self.south, self.west, self.times_visited, self.was_forgotten, 
                               self.long_description, self.short_description, self.forgotten_description, self.features, self.npcs, self.items)

        return 

    def load_info(self, location_info: dict) -> None:
        """
        :param location_info: a dictionary that contains the json data to be loaded into the location variables
        """
        self.game_number = location_info.get("game_number")
        self.is_start = location_info.get("is_start")

        self.north    = location_info.get("north")
        self.east     = location_info.get("east")
        self.south    = location_info.get("south")
        self.west     = location_info.get("west")

        self.long_description  = location_info.get("long_description")
        self.short_description = location_info.get("short_description")
        self.forgotten_description = location_info.get("forgotten_description")

        self.features = location_info.get("features")
        self.npcs     = location_info.get("npcs")
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

        # create location tracking data
        self.start   = self.desert_camp
        self.current = self.start

        self.map_key = {"desert_camp" :       self.desert_camp,
                             "desert_wilderness" : self.desert_wilderness, 
                             "path_1" :            self.path_1, 
                             "path_2":             self.path_2, 
                             "path_3":             self.path_3, 
                             "city_gates" :        self.city_gates,
                             "city_road_1" :       self.city_road_1, 
                             "city_road_2" :       self.city_road_2, 
                             "city_road_3" :       self.city_road_3, 
                             "palace_walls" :      self.palace_walls, 
                             "marketplace" :       self.marketplace, 
                             "secret_passage" :    self.secret_passage, 
                             "gardens" :           self.gardens, 
                             "well" :              self.well, 
                             "tower" :             self.tower, 
                             "bedroom" :           self.bedroom, 
                             "great_hall" :        self.great_hall, 
                             "throne_room" :       self.throne_room, 
                             "dining_hall" :       self.dining_hall, 
                             None :                None
                            }

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

        return
    
    def prep_data(self, map_dictionary: dict) -> None:
        """
        :param map_dictionary: a dictionary that contains all of the json data that has not yet been prepared to be loaded into the location variables 
        """
        # get the data from the original location json file (template)
        location_data = get_location_file_info(game_files[0])

        # replace the strings for node pointers with location objects 
        for location in map_dictionary:
            north = location.get("north")
            east = location.get("east")
            south = location.get("south")
            west = location.get("west")

            direction_array = [north, south, east, west]

            # swap the string north/east/south/west for location nodes 
            for direction in direction_array:
                if direction: 
                    direction = self.map_key.get(direction)
        
        return
