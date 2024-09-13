from menu.menu_option_interface import MenuOptionInterface
from utilities import stock_materials

class ReportMaterials(MenuOptionInterface):
    def __init__(self):
        self._shortcut = "B"
        self._description = "Get materials report"

    @property
    def shortcut(self):
        return self._shortcut

    @property
    def description(self):
        return self._description

    def perform_action(self):
        print_report()
        return True

def print_report():
    stock_materials.print_materials_report()
