from enum import Enum
from coffees import coffee_helper

WATER_STOCK_INITIAL = 300
MILK_STOCK_INITIAL = 200
COFFEE_STOCK_INITIAL = 100
MACHINE_MONEY_INITIAL = 0

water_stock = WATER_STOCK_INITIAL
milk_stock = MILK_STOCK_INITIAL
coffee_stock = COFFEE_STOCK_INITIAL
machine_money = MACHINE_MONEY_INITIAL

class Material(Enum):
    WATER = 1
    MILK = 2
    COFFEE = 3

def print_materials_report():
    print(f"{Material.WATER.name.title()}: {water_stock}ml")
    print(f"{Material.COFFEE.name.title()}: {coffee_stock}g")
    print(f"{Material.MILK.name.title()}: {milk_stock}ml")
    print(f"Money: ${machine_money}")


def check_stock_for_coffee(shortcut):
    print("Checking our stock...")
    coffee_requirements = coffee_helper.get_coffee_requirements_by_shortcut(shortcut)
    return is_stock_sufficient(*coffee_requirements)

def is_stock_sufficient(water_amount, coffee_amount, milk_amount):
    if water_stock < water_amount:
        print_not_enough(f"{Material.WATER.name.lower()}")
        return False
    if coffee_stock < coffee_amount:
        print_not_enough(f"{Material.COFFEE.name.lower()}")
        return False
    if milk_stock < milk_amount:
        print_not_enough(f"{Material.MILK.name.lower()}")
        return False
    return True

def print_not_enough(material):
    print(f"Sorry there is not enough {material} at the moment.")

def decrement_stock(shortcut):
    (water_amount, coffee_amount, milk_amount) = coffee_helper.get_coffee_requirements_by_shortcut(shortcut)
    global water_stock, coffee_stock, milk_stock
    water_stock -= water_amount
    coffee_stock -= coffee_amount
    milk_stock -= milk_amount
