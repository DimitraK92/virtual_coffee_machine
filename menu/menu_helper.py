from menu.order_coffee import OrderCoffee
from menu.report_materials import ReportMaterials
from menu.turn_off import TurnOff

def get_menu_actions():
    return [OrderCoffee(), ReportMaterials(), TurnOff()]

def get_main_menu_formatted():
    return "\n".join([f"{action.shortcut}. {action.description}" for action in get_menu_actions()])

def get_main_menu_shortcuts():
    return [action.shortcut for action in get_menu_actions()]

def handle_user_selection(u_option):
    for action in get_menu_actions():
        if u_option == action.shortcut:
            return action.perform_action()







