from abc import ABC, abstractmethod

class BaseCoffee(ABC):
    def __init__(self, water_needed: int, coffee_needed: int, milk_needed: int, cost: float):
        self.water_needed = water_needed
        self.coffee_needed = coffee_needed
        self.milk_needed = milk_needed
        self.cost = cost

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def shortcut(self) -> str:
        pass

