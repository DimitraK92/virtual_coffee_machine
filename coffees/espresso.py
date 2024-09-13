from coffees.base_coffee import BaseCoffee

class Espresso(BaseCoffee):
    def __init__(self):
        super().__init__(
            water_needed=50,
            coffee_needed=18,
            milk_needed=0,
            cost=1.5)

    @property
    def name(self):
        return "Espresso"

    @property
    def shortcut(self):
        return "E"
