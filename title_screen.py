import ascii_art
import textwrap
import os
import fugue_map
import sys
import inventory
import character
import player


def title_screen():

    print("#############################")
    print("#          FUGUE            #")
    print("#############################")
    print(ascii_art.castle.center(30))
    print("        1 NEW GAME           ")
    print("        2 CONTINUE           ")
    print("        3 CREDITS            ")
    print("        4 EXIT             \n")

    choice = input("What would you like to do?: \n")

    # Choices:

    if choice == "1" or choice == "new game".lower():
        my_map = fugue_map.Fugue_Map()
        my_map.prep_data()
        my_inventory = inventory.Inventory()
        my_player = player.Player(inventory, 20, 10, 10, 10, 30, None, None, None, 50, "desert camp")
        os.system('cls')

        current_room = my_map.desert_camp
        current_room.times_visited += 1
        os.system('cls')
        print("###############################################################################################")
        print("\n".join(textwrap.wrap(current_room.long_description, width=100, replace_whitespace=False)))
        print("###############################################################################################")
        print(current_room.ascii_art.center(30) + "\n")
        print("###############################################################################################")

        return


#
    elif choice == "2" or choice.lower == "continue":
        my_map = fugue_map.Fugue_Map()
        my_map.prep_data()
        my_inventory = inventory.Inventory()
        my_inventory.LoadInventory("inventory.json")

        current_room = my_map.current
        # current_room.times_visited += 1
        os.system('cls')
        print("###############################################################################################")
        print("\n".join(textwrap.wrap(current_room.long_description, width=100, replace_whitespace=False)))
        print("###############################################################################################")
        print(current_room.ascii_art.center(30) + "\n")
        print("###############################################################################################")

        return


#
    elif choice == "3" or choice.lower() == "credits":
        os.system('cls')
        print("###############################################################################################")
        print("                                        FUGUE                                                 ")
        print("                                         BY                                                   \n")
        print("                                    Hayley Leavitt                                            ")
        print("                                     John Koenig                                              ")
        print("                                     Luke Babcock                                             \n")
        print("###############################################################################################\n")
        input("Press any key to go back")
        title_screen()


#
    elif choice == "4" or choice.lower() == "exit":
        sys.exit("Thank you for playing!")


#
    else:
        print("Invalid selection. Try again: ")

