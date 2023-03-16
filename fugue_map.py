"""
Fugue Map 
Hayley Leavitt 2023
Version 5.0
"""

# bed ascii art from https://asciiart.website/index.php?art=objects/furniture/beds 
# armor ascii art from https://www.asciiart.eu/people/occupations/knights 
# cake ascii art from https://www.asciiart.eu/food-and-drinks/other 

# libraries
import json
import textwrap
from fugue_jukebox import Jukebox

# global variables
location_file = "fugue_locations.json"
npc_file = "npc.json"
enemy_file = "enemies.json"
item_file = "items.json"
game_files = [location_file, npc_file, enemy_file, item_file]

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
        out_file.write(json_object)


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
        self.name = npc_info.get("name")
        self.description = npc_info.get("description")
        self.location = npc_info.get("location") 
        self.is_impostor = npc_info.get("is_impostor")
        self.dialogue = npc_info.get("dialogue")
        self.aliases = npc_info.get("aliases")

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

        self.times_visited += 1

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

    def look_at(self, keyword) -> str: 
        if keyword in self.features:
            return self.features.get(keyword)
        else: 
            return "You can't search for that."

    def remove_item(self, thing) -> None: 
        if thing in self.items:
            self.items.drop(thing)

    def add_item(self, thing) -> None: 
        if thing not in self.items:
            self.items.append(thing)


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
        self.desert_camp.east  = None
        self.desert_camp.south = self.desert_wilderness
        self.desert_camp.west  = None

        self.desert_wilderness.north = self.desert_camp
        self.desert_wilderness.east  = None
        self.desert_wilderness.south = None
        self.desert_wilderness.west  = None

        self.path_1.north = self.path_2
        self.path_1.east = None
        self.path_1.south = self.desert_camp
        self.path_1.west = None
        
        self.path_2.north = self.path_3
        self.path_2.east = None
        self.path_2.south = self.path_1
        self.path_2.west = None

        self.path_3.north = self.city_gates
        self.path_3.east = None
        self.path_3.south = self.path_2
        self.path_3.west = None

        self.city_gates.north = self.city_road_2
        self.city_gates.east = None
        self.city_gates.south = self.path_3
        self.city_gates.west = None

        self.city_road_1.north = self.secret_passage
        self.city_road_1.east = self.city_road_2
        self.city_road_1.south = None
        self.city_road_1.west = None

        self.city_road_2.north = self.palace_walls
        self.city_road_2.east  = self.city_road_3
        self.city_road_2.south = self.city_gates
        self.city_road_2.west  = self.city_road_1

        self.city_road_3.north = self.marketplace
        self.city_road_3.east = None
        self.city_road_3.south = None
        self.city_road_3.west  = self.city_road_2

        self.palace_walls.north = None
        self.palace_walls.east = self.marketplace
        self.palace_walls.south = self.city_road_2
        self.palace_walls.west  = None

        self.marketplace.north = None
        self.marketplace.east = None
        self.marketplace.south = self.city_road_3
        self.marketplace.west  = self.palace_walls

        self.secret_passage.north = self.gardens
        self.secret_passage.east = None 
        self.secret_passage.south = self.city_road_1
        self.secret_passage.west = None

        self.gardens.north = None
        self.gardens.east  = self.tower
        self.gardens.south = self.secret_passage
        self.gardens.west  = self.well

        self.well.north = None
        self.well.east = self.gardens
        self.well.south = None
        self.well.west = None
        
        self.tower.north = self.great_hall
        self.tower.east  = self.bedroom
        self.tower.south = None
        self.tower.west = self.gardens

        self.bedroom.north = None
        self.bedroom.east = None
        self.bedroom.south = None
        self.bedroom.west = self.tower

        self.great_hall.north = self.throne_room
        self.great_hall.east  = self.dining_hall
        self.great_hall.south = self.tower
        self.great_hall.west = None

        self.throne_room.north = None
        self.throne_room.east = None
        self.throne_room.south = self.great_hall
        self.throne_room.west = None

        self.dining_hall.north = None
        self.dining_hall.east = None
        self.dining_hall.south = None
        self.dining_hall.west = self.great_hall

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
        self.npc_ids = ["Impostor", "City_Gate_Guard", "City_Guide", "Little_Boy", "Wizard", "Merchant", "Person_in_the_Mirror", "Soldier_Ghost"]
        self.npc_aliases = ["impostor", "guide", "boss", "proteus", "stranger", "shrouded stranger", 
                            "city guard", "city gate guard", "guard", "jace",
                            "city guide", "town guide", "tour guide", "artie",
                            "little boy", "boy", "child", "kid", "luca",
                            "witch", "wizard", "magician", "alex", "red robed figure", "magic guard",
                            "old woman", "store owner", "shopkeep", "shopkeeper", "marianna", "merchant", "old lady", 
                            "mirror self", "mirror man", "elisab", "man in mirror", "man in the mirror", "person in the mirror", "person in mirror", "person", 
                            "cecilia", "ghost", "soldier", "ghost solider", "soldier ghost"]
        self.npc_array = [self.impostor, self.city_gate_guard, self.city_guide, self.little_boy, self.wizard, self.merchant, self.person_in_mirror, self.soldier_ghost]

        self.jukebox = Jukebox()

        return
    
    def prep_data(self, locationfile = game_files[0], npcfile = game_files[1]) -> None:
        """
        :param map_dictionary: a dictionary that contains all of the json data that has not yet been prepared to be loaded into the location variables 
        """
        # get the data from the original location json file (template)
        map_dictionary = get_file_info(locationfile)
        npc_dictionary = get_file_info(npcfile)

        # fill in the location data, correcting strings to objects as needed
        for i in range(len(self.map_array)):
            location = self.map_array[i]
            location_name = self.map_key[i]
            location.load_info(map_dictionary.get(location_name))

        # fill in the npc data
        for i in range(len(self.npc_array)): 
            npc = self.npc_array[i]
            npc_name = self.npc_ids[i]
            npc.load_info(npc_dictionary.get(npc_name))
            
    def save_map(self, locfile, npcfile):
        """
        save_map() Converts the contents of the Map, Locations, and NPC objects and saves them to the specified file
        """
        
        # Create dictionaries to store inventory that will be converted to JSON
        location_dict = {}
        npc_dict = {}

        # Add locations to dictionary
        for loc in self.map_array:
            info = {
                "name": loc.name,
                "song" : loc.song, 
                "is_start": loc.is_start,
                "is_current_location": loc.is_current_location,
                "north": loc.north,
                "east": loc.east,
                "south": loc.south,
                "west": loc.west,
                "times_visited": loc.times_visited,
                "was_forgotten": loc.was_forgotten,
                "long_description": loc.long_description,
                "short_description": loc.short_description,
                "forgotten_description": loc.forgotten_description, 
                "ascii_art": loc.ascii_art, 
                "features": loc.features, 
                "npcs": loc.npcs,
                "enemies": loc.enemies, 
                "items": loc.items
                }

            location_dict[loc.name] = info

        # Add npcs to dictionary
        for character in self.npc_array:
            info = {
                "name": character.name,
                "aliases": character.aliases,
                "description": character.description,
                "location": character.location,
                "is_impostor": character.is_impostor,
                "dialogue": character.dialogue
                }

            npc_dict[character.name] = info

        loc_json = json.dumps(location_dict, indent=4)
        npc_json = json.dumps(npc_dict, indent=4)

        with open(locfile, "w") as outfile:
            outfile.write(loc_json)

        with open(npcfile, "w") as outfile: 
            outfile.write(npc_json)

    def display_location(self) -> None:
        """
        Prints out the location display info
        """
        if self.current.name == "city road 2" and self.current.times_visited <2: 
            print("".join(textwrap.wrap("Your companion turns to you and speaks, \"You continue on, I must run ahead. If you have any questions, ask the city guide. I'll meet you in the Great Hall of the Palace!\", then he runs ahead, out of your sight. \n")))

        print(self.current.ascii_art.center(30) + "\n")
        print("".join(textwrap.wrap(self.current.get_description() + "\n\n", width=100, replace_whitespace=False)))
  
    def begin_map(self) -> str: 
        """
        Prints out the starting locaton and its information
        """
        print(self.desert_camp.ascii_art + "\n")
        print(self.desert_camp.long_description + "\n\n")

    def navigate(self, nput): 
        """
        Receives user input and changes the location, then displays the new location information
        """
        if "north" in nput or "up" in nput and self.current.north: 
                self.current = self.current.north
                self.display_location()
        
        elif "south" in nput or "down" in nput and self.current.south: 
                self.current = self.current.south
                self.display_location()

        elif "east" in nput or "right" in nput and self.current.east: 
                self.current = self.current.east
                self.display_location()

        elif "west" in nput or "left" in nput and self.current.west: 
                self.current = self.current.west
                self.display_location()

        else: 
            print("You can't go that direction")

        return

    def look(self, nput):
        """
        Displays the description of the feature or npc that the user wants to look at 
        """
        nput = nput.split(" ")
        if len(nput) < 2: 
            print("".join(textwrap.wrap(self.current.get_description() + "\n\n", width=100, replace_whitespace=False)))

        else: 
            for word in nput: 
                # check if the word is an NPC
                if word in self.impostor.aliases and "Imposter" in self.current.npcs:
                    print("".join(textwrap.wrap(self.impostor.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.city_gate_guard.aliases and "City Gate Guard" in self.current.npcs:
                    print("".join(textwrap.wrap(self.city_gate_guard.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.city_guide.aliases and "City Guide" in self.current.npcs:
                    print("".join(textwrap.wrap(self.city_guide.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.little_boy.aliases and "Little Boy" in self.current.npcs:
                    print("".join(textwrap.wrap(self.little_boy.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.wizard.aliases and "Wizard" in self.current.npcs:
                    print("".join(textwrap.wrap(self.wizard.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.merchant.aliases and "Merchant" in self.current.npcs:
                    print("".join(textwrap.wrap(self.merchant.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.person_in_mirror.aliases and "Person in the Mirror" in self.current.npcs:
                    print("".join(textwrap.wrap(self.person_in_mirror.description) + "\n\n", width=100, replace_whitespace=False))
                    break

                elif word in self.soldier_ghost.aliases and "Soldier Ghost" in self.current.npcs:
                    print("".join(textwrap.wrap(self.soldier_ghost.description) + "\n\n", width=100, replace_whitespace=False))
                    break
                    
                # check if the word is a feature
                elif word in self.current.features: 
                    print("".join(textwrap.wrap(self.current.look_at(word) + "\n\n", width=100, replace_whitespace=False)))
                    break 

            return

        print ("You can't do that\n")

    def help(self):
        """
        Displays the command word info to the user
        """
        print("".join(textwrap.wrap("The keywords are as follows: go, head, up, down, left, right, north, south, east, west, exit, quit, look, examine", width=100, replace_whitespace=False)))

    def talk(self, sentence):
        sentence = sentence.lower()
        sentence = sentence.split(" ")

        npc = None

        # figure out what npc the user wants to talk to and if that npc is in this location
        for word in sentence: 
            if word in self.npc_aliases:
                
                # figure out which npc is being referred to
                if word in self.impostor.aliases:
                    npc = self.impostor
                    break

                elif word in self.city_gate_guard.aliases:
                    npc = self.city_gate_guard
                    break

                elif word in self.city_guide.aliases:
                    npc = self.city_guide
                    break

                elif word in self.little_boy.aliases:
                    npc = self.little_boy
                    break

                elif word in self.wizard.aliases:
                    npc = self.wizard
                    break

                elif word in self.merchant.aliases:
                    npc = self.merchant
                    break

                elif word in self.person_in_mirror.aliases:
                    npc = self.person_in_mirror
                    break

                elif word in self.soldier_ghost.aliases:
                    npc = self.soldier_ghost
                    break

        # If none of the words in the sentence referred to an npc 
        if npc is None: 
            print("I don't know who you're referring to\n")
            return

        # If that npc is not here
        if npc and npc.name not in self.current.npcs: 
            print("They are not here right now\n")
            return
        
        # If we know the npc and that npc is here, what is the user asking about?
        for word in sentence: 
            if word in npc.dialogue:
                print(npc.talk_to(word) + "\n")
                return

        # If none of the user's input is in the npc's dialogue tree, print their other dialogue option
        print(npc.dialogue.get("other") + "\n")
        return


    def talk_to_npc(self, npc, noun): 
        """
        Allows the user to interact with the npc dialogue
        """
        if npc in self.impostor.aliases and "Impostor" in self.current.npcs:
            print(self.impostor.talk_to(noun))

        elif npc in self.city_gate_guard.aliases and "City Gate Guard" in self.current.npcs:
            print(self.city_gate_guard.talk_to(noun))

        elif npc in self.city_guide.aliases and "City Guide" in self.current.npcs:
            print(self.city_guide.talk_to(noun))

        elif npc in self.little_boy.aliases and "Little Boy" in self.current.npcs:
            print(self.little_boy.talk_to(noun))

        elif npc in self.wizard.aliases and "Wizard" in self.current.npcs:
            print(self.wizard.talk_to(noun))

        elif npc in self.merchant.aliases and "Merchant" in self.current.npcs:
            print(self.merchant.talk_to(noun))

        elif npc in self.person_in_mirror.aliases and "Person in the Mirror" in self.current.npcs:
            print(self.person_in_mirror.talk_to(noun))

        elif npc in self.soldier_ghost.aliases and "Soldier Ghost" in self.current.npcs:
            print(self.soldier_ghost.talk_to(noun))

        else:
            print("You cannot do that\n")



def main():
    my_map = Fugue_Map()
    my_map.prep_data()

    while(1):
        print("Welcome to the Map of Fugue! What would you like to do today?")
        print("1.) Explore the map")
        print("2.) Talk to an npc")
        print("3.) Save the Map and NPCS to a new file")
        print("4.) Exit")
        print("Please enter a number\n")

        nput = input()

        if nput == "4": 
            print("Thank you for exploring Fugue!")
            break;
        
        elif nput == "1": 
            print("The navigation keywords are \"go\" and \"head\"")
            print("The interaction keywords are \"look\", \"examine\", \"check\", \"inspect\", \"investigate\", and \"search\"")
            print("".join(textwrap.wrap("Direction keywords are \"north\", \"east\", \"south\", \"west\", \"up\", \"down\", \"left\", and \"right\"", width=100, replace_whitespace=False)))
            
            print("So, you can type \"go north\" or \"Head Left\" and it will navigate")
            print("At any time, type \"exit\" or \"quit\" to stop exploring the map and return to the menu.")
            print("Lastly, if you need to see a list of keywords, just type \"help\"")
            print() 
            print("====================================================================================================")

            my_map.begin_map()

            while(1): 
                print("What would you like to do?")
                user_input = input()
                user_input = user_input.lower()

                if "exit" in user_input or "quit" in user_input: 
                    print("Exiting Map...")
                    break

                elif "go" in user_input or "head" in user_input:
                    my_map.navigate(user_input)

                elif "look" in user_input: 
                    my_map.look(user_input)

                elif "talk" in user_input or "ask" in user_input:
                    my_map.talk(user_input)

                else: 
                    print("I don't understand, please try again.\n")

                

        else: 
            print("Number input here only, please.")

            




if __name__ == "__main__":
    main()
