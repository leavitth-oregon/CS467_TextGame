inventory = []


room_items = ["sword", "apple"]


def take(noun):
    if noun in room_items:
        inventory.append(noun)
        room_items.remove(noun)
        print("You now have", noun, "\n")
    else:
        print("You don't see", noun, "\n")


def drop(noun):
    if noun in inventory:
        room_items.append(noun)
        inventory.remove(noun)
        print("You dropped", noun, "\n")
    else:
        print("You don't have", noun, "\n")


def look(noun):
    if noun == "backpack":
        if len(inventory) == 1:
            print("You just have your backpack.\n")
        else:
            for item in inventory:
                if item != "backpack":
                    print(inventory)


# Command dictionary with keys and their synonyms
commands = {drop:    ["drop", "leave"],

            take:    ["grab", "pick up", "pickup", "pick", "take"],

            look:    ["look", "examine", "check"],

            # go:    ["go", "head"],

            # talk:  ["talk", "ask"],

            # drink: ["drink"],

            # convince ["convice", "persuade"],

            # scare ["scare", "intimidate"],
            }


def verb_return(word):
    for verb, synonym in commands.items():
        if word == synonym:
            return verb
        if isinstance(synonym, list) and word in synonym:
            return verb


def parse(user_input):

    noun = None

    # A list every word from the user
    command_list = user_input.split(" ")

    # Inventory Key Word
    if "inventory" in command_list:
        if not inventory:
            print("You have nothing to your name\n")
            return
        if len(inventory) == 1:
            print("Your backpack is empty\n")
            return
        else:
            print("Inventory: ")
            for item in inventory:
                if item != "backpack":
                    print("-" + item)
            return

    # Directional Key Words
    if "north" in command_list:
        if current_room.north is not None:
            current_room = current_room.north
        else:
            print("Can't go that way.\n")

    if "south" in command_list:
        if current_room.south is not None:
            current_room = current_room.south
        else:
            print("Can't go that way.\n")

    if "east" in command_list:
        if current_room.east is not None:
            current_room = current_room.east
        else:
            print("Can't go that way.\n")

    if "west" in command_list:
        if current_room.west is not None:
            current_room = current_room.west
        else:
            print("Can't go that way.\n")

    # Determine the noun from user_input
    for word in command_list:
        if word in room_items:
            noun = word
        elif word in inventory:
            noun = word
        else:
            noun = word

    # Determine the verb from user_input
    for word in command_list:
        if verb_return(word) is not None:
            verb = verb_return(word)
            # Return the action on the noun
            return verb(noun)
        else:
            print("I don't know how to do that.\n")
            return


# Prompt for the user
while True:
    user_input = input("What do you want to do? ")
    parse(user_input)
