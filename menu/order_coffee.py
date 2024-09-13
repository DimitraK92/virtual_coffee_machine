from msilib.schema import SelfReg

from .menu_option_interface import MenuOptionInterface
from utilities import validator, payments, stock_materials
from coffees import coffee_helper


class OrderCoffee(MenuOptionInterface):
    def __init__(self):
        self._shortcut = "A"
        self._description = "Order coffee"

    @property
    def shortcut(self):
        return self._shortcut

    @property
    def description(self):
        return self._description

    def perform_action(self) -> bool:
        try:
            user_choice = get_user_choice()
            if process_order(user_choice): serve_coffee(user_choice)
            return True
        except Exception as e:
            print(e)
            return False

# region perform_action helpers
def get_user_choice():
    coffee_type_question = f"Which coffee do you want?\n{coffee_helper.get_coffee_types_formatted()}\n"
    valid_options = coffee_helper.get_coffees_shortcuts()
    return validator.validate_user_input(input(coffee_type_question), valid_options)

def process_order(choice) -> bool:
    if stock_materials.check_stock_for_coffee(choice) and payments.process_payment(choice):
        stock_materials.decrement_stock(choice)
        return True
    return False

def serve_coffee(choice):
    coffee_name = coffee_helper.get_coffee_name_by_shortcut(choice).lower()
    print(f"Here is your {coffee_name}. Enjoy!")
# endregion
