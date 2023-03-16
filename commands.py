import inventory
import inventory_item
import fugue_map
import os
import sys
import textwrap
# import main
my_map = fugue_map.Fugue_Map()
my_map.prep_data()

world_inventory = inventory.Inventory()
world_inventory.LoadAllInventory()

my_inventory = inventory.Inventory()


def enter_room(new_room):
    """
    When the player changes rooms, the screen clears and displays the description(long or short
    depending if they have been to the room or not) ascii art, changes been_to room attribute to
    True and then prompts the player on what to do next.
    """
    for room in my_map.map_array:
        if room.is_current_location:
            current_room = room
            current_room.times_visited += 1

            if new_room == "north" or new_room == "up":
                if current_room.north is not None:
                    current_room.is_current_location = False
                    current_room = current_room.north
                    current_room.times_visited += 1
                    current_room.is_current_location = True

                else:
                    print("You can't go that way\n")
                    return

            elif new_room == "south" or new_room == "down":
                if current_room.south is not None:
                    current_room.is_current_location = False
                    current_room = current_room.south
                    current_room.times_visited += 1
                    current_room.is_current_location = True

                else:
                    print("You can't go that way\n")
                    return

            elif new_room == "east" or new_room == "right":
                if current_room.east is not None:
                    current_room.is_current_location = False
                    current_room = current_room.east
                    current_room.times_visited += 1
                    current_room.is_current_location = True

                else:
                    print("You can't go that way\n")
                    return

            elif new_room == "west" or new_room == "left":
                if current_room.west is not None:
                    current_room.is_current_location = False
                    current_room = current_room.west
                    current_room.times_visited += 1
                    current_room.is_current_location = True

                else:
                    print("You can't go that way\n")
                    return
            else:
                print("You can't go that way\n")
                return

            if current_room.times_visited == 1:
                os.system('cls')
                print("###############################################################################################\n")
                # print(current_room.long_description)
                print("\n".join(textwrap.wrap(current_room.long_description, width=100, replace_whitespace=False)))
                print("###############################################################################################")
                print(current_room.ascii_art.center(30) + "\n")
                print("###############################################################################################")
                player_prompt()
            else:
                os.system('cls')
                print("###############################################################################################\n")
                # print(current_room.short_description)
                # print("\n".join(textwrap.wrap(current_room.get_description(), width=100, replace_whitespace=False)))
                print("\n".join(textwrap.wrap(current_room.short_description, width=100, replace_whitespace=False)))
                print("###############################################################################################")
                print(current_room.ascii_art.center(30) + "\n")
                print("###############################################################################################")
                player_prompt()


def take(noun):
    """
    I made a game_items list in John's inventory_item program. The list can then be checked for nouns
    created by us. If it's a noun, check if it can be equipped, check if it's in the current room.
    If it can be equipped, we can put it in our inventory. Mark item as equipped and remove item
    from the room items list. Print messages saying we got the backpack, we picked it up,
    can't take it, need to get the backpack first, or that there is no such item in the current room.
    """

    if world_inventory.GetItem(noun) is not None:
        noun = world_inventory.GetItem(noun)
        my_inventory.AddItem(noun)
        print("You picked up", noun.name)


    else:
        print("There is no", noun)



def drop(noun):
    """
    Basically the same approach as take but with removing items from my_inventory and adding
    items to the room inventory. Prints message saying we dropped it. Must have item to drop it.
    """
    for room in my_map.map_array:
        if room.is_current_location:
            current_room = room

            my_inventory.RemoveItem(noun)
            print("You dropped the", noun.name)
            current_room.items.append(noun)




def look(noun):
    """
    Checks to see if the noun is in our list of nouns, then to see if the noun is in the current
    room. (If the noun is the tree in the campfire room, after the user takes the backpack off the
    tree it will print a different description that doesn't mention a backpack hanging on the tree.)
    Then prints the description of the noun.
    """
    for room in my_map.map_array:
        if room.is_current_location:
            current_room = room

            if noun == "satchel":
                print("You see a wooden sword, some cloth armor and an everburning lamp!")
                my_inventory.AddItem(world_inventory.GetItem('Wooden Sword'))
                my_inventory.AddItem(world_inventory.GetItem('Cloth Armor'))
                my_inventory.AddItem(world_inventory.GetItem('Everburning Lamp'))

            elif noun in current_room.features:
                print(current_room.look_at(noun))

            elif noun in current_room.npcs:
                if noun in my_map.impostor.aliases and "Imposter" in current_room.npcs:
                    print(my_map.impostor.description)

                elif noun in my_map.city_gate_guard.aliases and "City Gate Guard" in current_room.npcs:
                    print(my_map.city_gate_guard.description)

                elif noun in my_map.city_guide.aliases and "City Guide" in current_room.npcs:
                    print(my_map.city_guide.description)

                elif noun in my_map.little_boy.aliases and "Little Boy" in current_room.npcs:
                    print(my_map.little_boy.description)

                elif noun in my_map.wizard.aliases and "Wizard" in current_room.npcs:
                    print(my_map.wizard.description)

                elif noun in my_map.merchant.aliases and "Merchant" in current_room.npcs:
                    print(my_map.merchant.description)

                elif noun in my_map.person_in_mirror.aliases and "Person in the Mirror" in current_room.npcs:
                    print(my_map.person_in_mirror.description)

                elif noun in my_map.soldier_ghost.aliases and "Soldier Ghost" in current_room.npcs:
                    print(my_map.soldier_ghost.description)

            else:
                print("You cannot search for that\n")



# ###############################################################################################
# Verbs the user can use to play. The keys are the functions above. The values are synonyms the
# user could use.

commands = {drop: ["drop", "leave"],
            take: ["take", "pick up", "pickup", "pick", "grab"],
            look: ["look", "examine", "check"],
            enter_room: ["go", "head"]
            }


##################################################################################################


def verb_return(word):
    """Checks if a word is an acceptable synonym of our commands"""
    for verb, synonym in commands.items():
        if word == synonym:
            return verb
        if isinstance(synonym, list) and word in synonym:
            return verb


def parse(user_input):
    for room in my_map.map_array:
        if room.is_current_location:
            current_room = room
            noun = None
            verb = None
            user_input = user_input.lower()

            command_list = user_input.split(" ")
            
            # The user wants to save their game

            if command_list[0] == "save" or command_list[0] == "savegame":
                my_inventory.SaveInventory()
                fugue_map.save_file_info(my_map)
                sys.exit("Thank you for playing!")

            # The user wants to exit

            if command_list[0] == "exit" and len(command_list) == 1:
                quit_ans = input("Do you really want to quit? Y or N:  ")
                if quit_ans.lower() == "yes" or quit_ans.lower() == 'y':
                    sys.exit("Thank you for playing!")
                else:
                    return

            if command_list[0] == "exit" and command_list[1] == "game":
                quit_ans = input("Do you really want to quit? Y or N:  ")
                if quit_ans.lower() == "yes" or quit_ans.lower() == 'y':
                    sys.exit("Thank you for playing!")
                else:
                    return

            # The user wants to look at their inventory

            if "inventory" in command_list:
                inventory.Inventory.DisplayInventory(my_inventory)
                return

            # If the user only enters "look" then display the short description of the room

            if len(command_list) == 1 and command_list[0] == "look":
                os.system('cls')
                print("###############################################################################################")
                print(current_room.short_description)
                print("###############################################################################################")
                print(current_room.ascii_art.center(30) + "\n")
                print("###############################################################################################")
                return


            # Add words to the command list

            for word in command_list:
                if word in current_room.items:
                    noun = word

                elif word in current_room.npcs:
                    noun = word

                elif my_inventory.GetItem(word) is not None:
                    noun = my_inventory.GetItem(word)

                else:
                    noun = word

            for word in command_list:
                if verb_return(word) is not None:
                    verb = verb_return(word)
                else:
                    print("I don't know how to do that.\n")
                    return
                return verb(noun)


def player_prompt():
    while True:
        user_input = input("What do you want to do? ")
        parse(user_input)

