# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def __str__(self):
        return self.name

    def __getter__(opt):
        return lambda self: self.connections[opt]

    def __setter__(opt):
        def setter(self, room):
            self.connections[opt] = room

        return setter

    def move(self, opt):
        return self.connections[opt]

    n_to = property(__getter__("n"), __setter__("n"), doc="North")
    s_to = property(__getter__("s"), __setter__("s"), doc="South")
    e_to = property(__getter__("e"), __setter__("e"), doc="East")
    w_to = property(__getter__("w"), __setter__("w"), doc="West")
