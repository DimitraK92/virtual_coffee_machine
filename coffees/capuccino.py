from coffees.base_coffee import BaseCoffee

class Capuccino(BaseCoffee):
    def __init__(self):
        super().__init__(
            water_needed=250,
            coffee_needed=24,
            milk_needed=100,
            cost=3)

    @property
    def name(self):
        return "Capuccino"

    @property
    def shortcut(self):
        return "C"

