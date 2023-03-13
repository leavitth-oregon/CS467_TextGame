from ascii_art import *
from fugue_map import *
from fugue_jukebox import *


def title_screen(fugue_map, jukebox):
    print("#############################")
    print("#          FUGUE            #")
    print("#############################")
    print(castle.center(30))
    print("        1 NEW GAME           ")
    print("        2 CONTINUE           ")
    print("        3 CREDITS           ")
    print("        4 EXIT            \n")

    choice = input("What would you like to do?: \n")
    
    # 1 - NEW GAME
    if choice == "1" or choice == "new game".lower():
        user_continue = input("WARNING: Choosing this option will overwrite any previous saves you have. Do you wish to continue? \n1) YES \n2) NO\n")

        if (user_continue == "1" or user_continue.lower() == "yes"):
            jukebox.set_os()
            new_room = fugue_map.desert_camp
            new_room.is_current_location = True

            print("###############################################################################################")
            print(new_room.get_description())
            print("###############################################################################################")
            print(new_room.ascii_art)
            print("###############################################################################################")

            new_room.times_visited += 1
            return fugue_map.desert_camp

        else: 
            title_screen(fugue_map, jukebox)
            return
    
    
    # 2 - LOAD GAME 
    elif choice == "2" or choice.lower == "continue":
        #  Load Game
        pass


    # 3 - CREDITS
    elif choice == "3" or choice.lower() == "credits":
        print("###############################################################################################")
        print("                                        FUGUE                                                 ")
        print("                                         BY                                                   \n")
        print("                                    Hayley Leavitt                                            ")
        print("                                     John Koenig                                              ")
        print("                                     Luke Babcock                                             \n")
        print("###############################################################################################\n")
        input("Press any key to go back")
        title_screen(fugue_map, jukebox)
        return


#
    elif choice == "4" or choice.lower() == "exit":
        print("Thank you for playing!")
        exit(1)


#
    else:
        print("Invalid selection. Try again: ")
