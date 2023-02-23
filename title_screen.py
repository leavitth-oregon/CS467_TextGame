import ascii_art
import textwrap
import os
import fugue_map


def title_screen():
    print("#############################")
    print("#          FUGUE            #")
    print("#############################")
    print(ascii_art.castle.center(30))
    print("        1 NEW GAME           ")
    print("        2 CONTINUE           ")
    print("        3 SETTINGS           ")
    print("        4 CREDITS            \n")

    choice = input("What would you like to do?: \n")

    if choice == "1" or choice == "new game".lower():
        os.system('cls')
        new_room = fugue_map.campfire
        new_room.in_current_room = True
        print("###############################################################################################")
        print("\n".join(textwrap.wrap(new_room.long_description, width=100, replace_whitespace=False)))
        print("###############################################################################################")
        print(new_room.ascii_art.center(30) + "\n")
        print("###############################################################################################")

        return
