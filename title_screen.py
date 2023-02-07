import rooms
import ascii_art
import commands


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
        current_room = rooms.campfire
        commands.enter_room(current_room)
    return
