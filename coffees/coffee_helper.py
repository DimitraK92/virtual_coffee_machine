from coffees.latte import Latte
from coffees.capuccino import Capuccino
from coffees.espresso import Espresso

def get_coffee_types():
    return [Espresso(), Latte(), Capuccino()]

def get_coffee_types_formatted():
    return "\n".join([f"{coffee.shortcut}. {coffee.name.title()}" for coffee in get_coffee_types()])

def get_coffees_shortcuts():
    return [coffee.shortcut for coffee in get_coffee_types()]

def get_coffee_by_shortcut(shortcut):
    return next((coffee for coffee in get_coffee_types() if coffee.shortcut == shortcut), None)

def get_coffee_name_by_shortcut(shortcut):
    return get_coffee_by_shortcut(shortcut).name

def get_coffee_price_by_shortcut(shortcut):
    return get_coffee_by_shortcut(shortcut).cost

def get_coffee_requirements_by_shortcut(shortcut):
    coffee = get_coffee_by_shortcut(shortcut)
    return coffee.water_needed, coffee.coffee_needed, coffee.milk_needed



