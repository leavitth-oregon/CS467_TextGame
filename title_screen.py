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

# Choices:
    
 
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
    
    
#
    elif choice == "2" or choice.lower == "continue":
        #  Load Game
        pass


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

