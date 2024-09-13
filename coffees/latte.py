from coffees.base_coffee import BaseCoffee

class Latte(BaseCoffee):
    def __init__(self):
        super().__init__(
            water_needed=200,
            coffee_needed=24,
            milk_needed=150,
            cost=2.5)

    @property
    def name(self):
        return "Latte"

    @property
    def shortcut(self):
        return "L"
