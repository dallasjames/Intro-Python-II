class Item:
    # item object
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # showing the items
    def __str__(self):
        return f"{self.name}: {self.description}"

    # for taking items
    def on_take(self):
        print(f"You picked up the {self.name}")

    # for dropping items
    def on_drop(self):
        print(f"You dropped the {self.name}")
