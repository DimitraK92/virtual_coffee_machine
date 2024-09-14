from utilities import validator, stock_materials
from coffees import coffee_helper

def process_payment(shortcut):
    cost = coffee_helper.get_coffee_price_by_shortcut(shortcut)
    print(f"The cost is ${cost}. Please insert coins.")
    total = process_inserted_money(cost)
    if total >= cost:
        stock_materials.machine_money += cost
        return True
    return False

def process_inserted_money(cost):
    total = calculate_total_money()
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
    elif total > cost:
        change = calculate_change(total, cost)
        print(f"Here is ${change} in change.")
    return total

def calculate_total_money():
    quarters = validator.validate_user_input_payment(input("How many quarters? "))  # 25 cents
    dimes = validator.validate_user_input_payment(input("How many dimes? "))  # 10 cents
    nickles = validator.validate_user_input_payment(input("How many nickles? "))  # 5 cents
    pennies = validator.validate_user_input_payment(input("How many pennies? "))  # 1 cent
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def calculate_change(total, cost):
    return round(total - cost, 2)
