# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        # Store current_room as a Room object
        self.current_room: Room = current_room
        self.inventory = []

    def stuff(self):
        print("Inventory")
        for i in self.inventory:
            print(i)
