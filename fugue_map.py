# libraries
import json

# global variables
game_num = 0
game_files = ['locations.json']
current_location = None


def get_location_file_info(locfile):
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
        
        # TO DO: apply the parsed data to the location objects in the map

    return parsed_locations


def create_location_file(location_data, game_number):
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

    return None


class Fugue_Location:
    def __init__(self, name):
        """
        :param name: the string name of the location
        :returns None:

        Sets up all the variables of the location
        """
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

        self.features = []
        self.npcs = []
        self.items = []

    def get_description(self):
        """
        :param self: the location
        :return location_description: the description of the location being visited, relative to when and how it
        is being visited
        """
        location_description = self.short_description

        if (self.times_visited <= 0) and (self.was_forgotten is False):
            location_description = self.long_description
        elif (self.times_visited <= 0) and (self.was_forgotten is True):
            location_description = self.short_description

        return location_description

    def get_direction(self, direction):
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

    def is_npc_here(self, npc):
        if npc in self.npcs:
            return True
        else:
            return False

    def is_item_here(self, item):
        if item in self.items:
            return True
        else:
            return False


class Fugue_Map:
    def prep_data(self):
        # get the data from the original location json file (template)
        location_data = get_location_file_info(game_files[0])

        # parse the location data out into the locations

    def __init__(self):
        # create all locations in the map
        self.desert_camp = Fugue_Location("desert camp")
        self.desert_wilderness = Fugue_Location("desert wilderness")
        self.path_1 = Fugue_Location("path 1")
        self.path_2 = Fugue_Location("path 2")
        self.path_3 = Fugue_Location("path 3")
        self.city_gates = Fugue_Location("city gates")
        self.city_road_1 = Fugue_Location("city road 1")
        self.city_road_2 = Fugue_Location("city road 2")
        self.city_road_3 = Fugue_Location("city road 3")
        self.palace_walls = Fugue_Location("palace walls")
        self.marketplace = Fugue_Location("marketplace")
        self.secret_passage = Fugue_Location("secret passage")
        self.gardens = Fugue_Location("gardens")
        self.well = Fugue_Location("well")
        self.tower = Fugue_Location("tower")
        self.bedroom = Fugue_Location("bedroom")
        self.great_hall = Fugue_Location("great hall")
        self.throne_room = Fugue_Location("throne room")
        self.dining_hall = Fugue_Location("dining hall")

        # create location tracking data
        self.start = self.desert_camp
        self.current = self.start
