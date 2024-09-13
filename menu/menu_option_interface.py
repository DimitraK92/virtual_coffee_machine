from abc import ABC, abstractmethod

class MenuOptionInterface(ABC):
    @property
    @abstractmethod
    def shortcut(self) -> str:
        """Returns the keyboard shortcut for this menu option"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Returns the description for this menu option"""
        pass

    @abstractmethod
    def perform_action(self) -> None:
        """Performs the action associated with this menu option"""
        pass
