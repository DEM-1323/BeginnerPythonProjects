import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# initialize coffee machine
coffee_machine = CoffeeMaker()
menu = Menu()
money_bank = MoneyMachine()
exit_machine = False


def main():
    while not exit_machine:
        cls()
        boot_screen()
        service()
        exit_console()


def boot_screen():
    '''Boot screen with custom logos a resource list and menu items'''
    coffee_machine.boot_screen()
    print(menu.print_menu())


def service():
    # Ask User what they'd like
    while True:
        try:
            user_input = int(input('\nWhat would you like?: '))
            order = menu.find_drink(user_input)
            break
        except IndexError:
            print('\nInvalid input. Try again')
            continue

    if coffee_machine.is_resource_sufficient(order) is True:
        money_bank.make_payment(order.cost)
        coffee_machine.make_coffee(order)


def exit_console():
    global exit_machine
    while True:
        user_input = input('\nExit machine? (Y/N): ').upper()
        if user_input == 'Y':
            exit_machine = True
            break
        elif user_input == 'N':
            break
        else:
            print('\nInvalid Input')
            continue


# Clear Screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
