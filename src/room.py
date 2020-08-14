from typing import List
from item import Item


class Room:
    # room object
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items: List[Item] = []

    # for items put in room
    def get_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    # for items taken out of room
    def remove_item(self, item: Item):
        self.items.remove(item)
