from menu.menu_option_interface import MenuOptionInterface
import time

class TurnOff(MenuOptionInterface):
    def __init__(self):
        self._shortcut = "C"
        self._description = "Turn off coffee machine"

    @property
    def shortcut(self):
        return self._shortcut

    @property
    def description(self):
        return self._description

    def perform_action(self):
        print("Shutting down...")
        countdown_timer(5)
        return True

def countdown_timer(countdown_time):
    while countdown_time:
        mints, secs = divmod(countdown_time, 60)
        timer = '{:02d}:{:02d}'.format(mints, secs)
        if countdown_time == 1:
            print("Good bye!")
        else:
            print(timer, end="\r")
        time.sleep(1)
        countdown_time -= 1


