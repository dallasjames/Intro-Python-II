from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    "sword": Item("Sword", "A nice sword that will fetch money at a pawn shop"),
    "coins": Item("Some Coins", "$2000 worth"),
    "dragon": Item("Dragon", "It's asleep don't worry")
}

room['outside'].give(item["sword"])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

name = input("What is your name: ")
player = Player(name, room["outside"])
while True:
    # * Prints the current room name
    current_room = player.current_room
    print(player)
    print(f"{player.name} is in the {player.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
    print(current_room.description)
    print(current_room.__str__())
    # * Waits for user input and decides what to do.
    print("To move in a direction enter ('n', 's', 'e' or 'w') ")
    print("You can also choose 't' or 'd' followed by the item to take or drop it")
    user_input = input("Choose 'i' to see the inventory or 'q' to quit: ")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if user_input == "q":
        print("Goodbye")
        break
    elif user_input == "n":
        if hasattr(current_room, "n_to"):
            # if current_room.n_to is not None:
            player.current_room = getattr(current_room, "n_to")
            player.current_room = current_room.n_to
        else:
            print("You can't go North")
    elif user_input == "s":
        if hasattr(current_room, "s_to"):
            # if current_room.n_to is not None:
            player.current_room = getattr(current_room, "s_to")
            player.current_room = current_room.s_to
        else:
            print("You can't go South")
    elif user_input == "e":
        if hasattr(current_room, "e_to"):
            # if current_room.n_to is not None:
            player.current_room = getattr(current_room, "e_to")
            player.current_room = current_room.e_to
        else:
            print("You can't go East")
    elif user_input == "w":
        if hasattr(current_room, "w_to"):
            # if current_room.n_to is not None:
            player.current_room = getattr(current_room, "w_to")
            player.current_room = current_room.w_to
        else:
            print(f"You can't go West")
    else:
        print("\nCurrent Room: " + player.current_room.name)
    # You can dynamically generate attributes like on the line below and then check/access them using hasattr
    # and getattr

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
