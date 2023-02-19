import rooms
import inventory
import inventory_item
import os
import textwrap

current_room = rooms.campfire
my_inventory = inventory.Inventory()
room_items = current_room.room_items


def enter_room(new_room):

    """
    When the player changes rooms, the screen clears and displays the description(long or short
    depending if they have been to the room or not) ascii art, changes been_to room attribute to
    True and then prompts the player on what to do next.
    """

    os.system('cls')
    if not new_room.been_to:
        print("###############################################################################################")
        print("\n".join(textwrap.wrap(new_room.description, width=100, replace_whitespace=False)))
        print("###############################################################################################")
        print(new_room.ascii_art.center(30) + "\n")
        print("###############################################################################################")
        new_room.been_to = True
        new_room.in_current_room = True
        player_prompt()

    else:
        # Print short description
        print(new_room.short_desc)
        print(new_room.ascii_art + "\n")
        player_prompt()

    print("You can't go that way\n")


def take(noun):

    """
    I made a game_items list in John's inventory_item program. The list can then be checked for nouns
    created by us. If it's a noun, check if it can be equipped, check if it's in the current room.
    If it can be equipped, we can put it in our inventory. Mark item as equipped and remove item
    from the room items list. Print messages saying we got the backpack, we picked it up,
    can't take it, need to get the backpack first, or that there is no such item in the current room.
    """

    for i in range(len(inventory_item.game_items)):
        if inventory_item.game_items[i].name == noun:
            if inventory_item.game_items[i].equipable:
                if inventory_item.game_items[i] in current_room.room_items:

                    # Getting the backpack
                    if inventory_item.game_items[i] == inventory_item.backpack:
                        my_inventory.AddItem(inventory_item.game_items[i])
                        inventory_item.game_items[i].equipped = True
                        current_room.room_items.remove(inventory_item.game_items[i])
                        print("You now have your backpack! You can carry lots of things in this!\n")
                        return

                    # Need the backpack first to add more items
                    elif inventory_item.backpack.equipped:
                        my_inventory.AddItem(inventory_item.game_items[i])
                        inventory_item.game_items[i].equipped = True
                        current_room.room_items.remove(inventory_item.game_items[i])
                        print("You now have", noun + "\n")
                        return

                    else:
                        print("You have no where to put", noun + "\n")
                        return

            else:
                print("You can't take", noun + "\n")
                return

    print("There is no", noun + "\n")


def drop(noun):

    """
    Basically the same approach as take but with removing items from my_inventory and adding
    items to the room inventory. Prints message saying we dropped it. Must have item to drop it.
    """

    for i in range(len(inventory_item.game_items)):
        if inventory_item.game_items[i].name == noun:
            inventory_item.game_items[i].equipped = False
            my_inventory.RemoveItem(inventory_item.game_items[i])
            current_room.room_items.append(inventory_item.game_items[i])
            print("You dropped", noun + "\n")
            return
    print("You don't have", noun + "\n")


def look(noun):

    """
    Checks to see if the noun is in our list of nouns, then to see if the noun is in the current
    room. (If the noun is the tree in the campfire room, after the user takes the backpack off the
    tree it will print a different description that doesn't mention a backpack hanging on the tree.)
    Then prints the description of the noun.
    """

    for i in range(len(inventory_item.game_items)):
        if inventory_item.game_items[i].name == noun:
            if inventory_item.game_items[i] in current_room.room_items:
                if inventory_item.game_items[i] == inventory_item.tree and current_room == rooms.campfire:
                    if inventory_item.backpack.equipped:
                        print(rooms.campfire.short_desc)
                        return
                    else:
                        print("You see your backpack on the tree's branch. It is as if someone had placed"
                              " it there with care.\n")
                        return
                print(inventory_item.game_items[i].description)
                return

            # If the user wants to "look in backpack", display inventory
            elif inventory_item.game_items[i] == inventory_item.backpack:
                inventory.Inventory.DisplayInventory(my_inventory)
                return

    print("There is no", noun + "\n")


# ###############################################################################################
# Verbs the user can use to play. The keys are the functions above. The values are synonyms the
# user could use.

commands = {drop: ["drop", "leave"],
            take: ["grab", "pick up", "pickup", "pick", "take"],
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
    noun = None
    verb = None

    command_list = user_input.split(" ")

    if "inventory" in command_list:
        inventory.Inventory.DisplayInventory(my_inventory)
        return

    if len(command_list) == 1 and command_list[0] == "look":
        print(current_room.short_desc)
        return

    for word in command_list:
        if word in current_room.room_items:
            noun = word

        elif my_inventory.GetItem(word) is not None:
            noun = word

        else:
            noun = word

    for word in command_list:
        if verb_return(word) is not None:
            verb = verb_return(word)
        else:
            print("I don't know how to do that.\n")
            return

        return verb(noun)


print(current_room.description)
print(current_room.ascii_art + "\n")


def player_prompt():
    while True:
        user_input = input("What do you want to do? ")
        parse(user_input)
