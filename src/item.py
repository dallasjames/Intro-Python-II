class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.event = None

    def take(self):
        print(f"You picked up the {self.name}")

    def drop(self):
        print(f"You dropped the {self.name}")
