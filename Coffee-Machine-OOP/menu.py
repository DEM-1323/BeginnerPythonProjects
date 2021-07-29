from art import menu_header


class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def print_menu(self):
        """Returns all the names of the available menu items"""
        print(menu_header)
        options = '----------------------'
        menu_item = 1
        for item in self.menu:
            options += f'\n{str(menu_item)}. {item.name.upper()} ${item.cost}'
            menu_item += 1
        options += '\n----------------------'
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item
        if it exists, otherwise returns None"""
        for item in self.menu:
            menu_index = str(self.menu[order_name - 1].name)
            if item.name == menu_index:
                return item
        print("Sorry that item is not available.")
