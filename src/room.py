# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        # 1) Adding these as attributes in the constructor is optional;
        # in python you can arbitrarily set attributes on instances
        # 2) the `: Room` syntax is a typehint. It just serves as a reminder
        # for other developers that self.n_to is storing a Room object (as opposed to a str)
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
        self.items = items

    def __str__(self):
        if len(self.items) > 0:
            for item in self.items:
                return f"This room contains {item.name} {item.description}"
        else:
            return f"This room has no items"

    def give(self, item):
        self.items.append(item)

    def take(self, item):
        self.items.remove(item)