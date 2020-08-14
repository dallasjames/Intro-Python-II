from room import Room


class Player:
    # player object
    def __init__(self, name, current_room):
        self.name = name
        self.current_room: Room = current_room
        self.inventory = []

    # shows inventory
    def stuff(self):
        print("Inventory")
        for i in self.inventory:
            print(i)
