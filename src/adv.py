from item import Item
from player import Player
from room import Room

# Marking rooms
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

# making map of rooms
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# putting objects in rooms
room['outside'].items.append(Item("Knife", "Sharp thing"))
room['outside'].items.append(Item("Potion", "Green and bubbly liquid in a glass vial"))

# gets name and creates player
name = input("Your name: ")
player = Player(name, room['outside'])

while True:
    current_room = player.current_room
    # prints current room name
    print(name, player.current_room.name)
    # prints current room description
    print(player.current_room.description)
    # prints rooms items if there are any
    if current_room.items:
        print("The room contains the following items:")
        for item in current_room.items:
            print(item)
    else:
        print("This room has no items")
    # gets input for commands user can give
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w') or get or take an item: ")
    if user_input == "q":
        print("Goodbye")
        break
    split_input = user_input.split()
    print(split_input)
    if len(split_input) == 1:
        direction = f"{user_input}_to"
        # moves player
        if hasattr(current_room, direction):
            player.current_room = getattr(current_room, direction)
        # shows player inventory
        elif user_input == "i":
            player.stuff()
        # error handling
        else:
            print("You can't go that way")
            continue
    elif len(split_input) == 2:
        item_name = split_input[1]
        # for getting or dropping stuff
        if split_input[0].lower() == "get" or "g":
            item = current_room.get_item(item_name)
            if item:
                item.on_take()
                current_room.remove_item(item)
                player.inventory.append(item)
            else:
                print(f"There is no {item_name} in this room")
        elif split_input[0].lower() == "drop" or "d":
            item = player.inventory[split_input[1]]
            if item:
                item.on_drop
                current_room.items.append(item.name, item.description)
                player.items.remove(item)
            else:
                print(f"You don't have a {split_input[1]}")
        # final error handling
        else:
            print(f"{user_input} is not an option.")
            continue
