import signal, os
from utilities import validator
from menu import menu_helper

EXIT_OPTION = "C"
CLEAR_SCREEN_COMMAND = 'cls' if os.name == 'nt' else 'clear'

def handle_interrupt_signal(signum, frame):
    clear_console()
    exit(1)

signal.signal(signal.SIGINT, handle_interrupt_signal)

def clear_console():
    os.system(CLEAR_SCREEN_COMMAND)

def run_main_menu_loop():
    shut_down = False
    while not shut_down:
        display_main_menu()
        try:
            user_choice = get_user_choice()
            if not  menu_helper.handle_user_selection(user_choice): break
            shut_down = user_choice == EXIT_OPTION
            if not shut_down: prompt_return_to_main_menu()
        except Exception as e:
            print(e)
            shut_down = True

def display_main_menu():
    clear_console()
    menu_content = (f"\nWelcome to our Virtual Coffee Machine! How can we help you?"
                    f"\n{menu_helper.get_main_menu_formatted()}")
    print(menu_content)

def get_user_choice():
    return validator.validate_user_input(input("What do you want to do? "), menu_helper.get_main_menu_shortcuts())

def prompt_return_to_main_menu():
    input("Press enter to go back to the main menu...")
    clear_console()

run_main_menu_loop()
