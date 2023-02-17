"""
Fugue Map 
Hayley Leavitt 2023
Version 1.0


"""

# libraries
import json

# global variables
game_num = 0
game_files = ['fugue_locations.json']
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

    def been_to(self) -> bool: 
        if self.times_visited > 0:
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

        # link all of the locations in the map 
        self.desert_camp.north = self.path_1
        self.desert_camp.east = self.desert_wilderness
        self.desert_camp.south = self.desert_wilderness
        self.desert_camp.west = self.desert_wilderness

        self.desert_wilderness.north = self.desert_camp
        self.desert_wilderness.east = self.desert_camp
        self.desert_wilderness.west = self.desert_camp

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
        self.city_road_2.east = self.city_road_3
        self.city_road_2.south = self.city_gates
        self.city_road_2.west = self.city_road_1

        self.city_road_3.north = self.marketplace
        self.city_road_3.west = self.city_road_2

        self.palace_walls.south = self.city_road_2
        self.palace_walls.west = self.marketplace

        self.marketplace.south = self.city_road_3
        self.marketplace.west = self.palace_walls

        self.secret_passage.north = self.gardens
        self.secret_passage.south = self.city_road_1

        self.gardens.east = self.tower
        self.gardens.south = self.secret_passage
        self.gardens.west = self.well

        self.well.east = self.gardens
        
        self.tower.west = self.gardens
        self.tower.north = self.great_hall
        self.tower.east = self.bedroom

        self.great_hall.north = self.throne_room
        self.great_hall.east = self.dining_hall
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

        return
    
    def prep_data(self) -> None:
        """
        :param map_dictionary: a dictionary that contains all of the json data that has not yet been prepared to be loaded into the location variables 
        """
        # get the data from the original location json file (template)
        map_dictionary = get_location_file_info(game_files[0])

        # replace the strings for node pointers with location objects 
        for i in range(len(self.map_array)):
            location = self.map_array[i]
            location_name = self.map_key[i]
            location.load_info(map_dictionary.get(location_name))
        
        return

    def print_info(self) -> None: 
        for location in self.map_array: 
            print(location.name)
            print()

            if location.north: 
                print("North: " + location.north.name)

            if location.east:
                print("East: " + location.east.name)

            if location.south: 
                print("South: " + location.south.name)

            if location.west: 
                print("West: " + location.west.name)

            print("Location Features: ")
            print(location.features)
            
            print("Location Items: ")
            print(location.items)

            print("Location NPCs: ")
            print(location.npcs)

            print()
        
        return


def main():
    my_map = Fugue_Map()
    my_map.prep_data()
    my_map.print_info()
    return


if __name__ == "__main__":
    main()
