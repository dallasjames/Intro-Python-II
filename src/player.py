# Write a class to hold player information, e.g. what room they are in
# currently.
import re


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name} is in the {self.current_room}"

    def do(self, opt):
        if re.compile("[nesw]|north|south|east|west").fullmatch(opt):
            self.move(opt)

    def move(self, opt):
        try:
            self.current_room = self.current_room.move(opt[0])
            print(f"{self.name} is now in the {self.current_room.name}")

        except:
            print("You can't go that way")
