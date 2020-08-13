# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        # Store current_room as a Room object
        self.current_room: Room = current_room
        self.inventory = inventory

    def take(self, opt):
        try:
            item_name = opt.split(" ")[1]
            item = self.current_room.take(item_name)
            item.get()
            self.inventory.append(item)
        except ValueError:
            print(f"{item_name} wasn't found")

    def drop(self, opt):
        try:
            item_name = opt.split(" ")[1]
            item = self.current_room.drop(item_name)
            item.drop(item_name)
            self.inventory.remove(item_name)
        except ValueError:
            print(f"You don't have a {item_name}")
