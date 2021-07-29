import os
from art import logo, menu_header
from machineData import MENU, resources


# TODO: 1. Print logo and report of coffee machine resources and menu

# Global Variables
machine_water = resources['water']
machine_milk = resources['milk']
machine_coffee = resources['coffee']
money = 0.0
balance = 0.0
exit_machine = False
payment_processed = False
menu = f'''----------------------
/ 1. Espresso ${MENU['espresso']['cost']}   /
/ 2. Latte ${MENU['latte']['cost']}      /
/ 3. Cappuccino ${MENU['cappuccino']['cost']} /
----------------------'''


def main():

    while not exit_machine:
        cls()
        boot_screen()
        service()
        exit_console()


# Coffee Machine Startup
def boot_screen():
    machine_report = (f'-------------------\n'
                      f' Water: {machine_water} \n'
                      f' Milk: {machine_milk}   \n'
                      f' Coffee: {machine_coffee} \n'
                      f' Money: ${money} \n'
                      f'-------------------')
    print(logo)
    print(machine_report)
    print(menu_header)
    print(menu)


# TODO: 2. Create user input and check to see if there are enough resources


# Main Program Loop
def service():
    # Ask User what they'd like
    while True:
        user_input = str(input('What would you like? (1/2/3): '))

        if user_input == '1' or '2' or '3':
            break
        else:
            print('\nInvalid input. Try again')
            continue
    # Check if there's enough resources and remove resources to create drink
    enough_resources(user_input)
    process_coins(user_input)


def enough_resources(user_selection):
    if input == '1':
        if machine_water < MENU['espresso']['ingredients']['water']:
            return 'Sorry there is not enough water.'
        elif machine_coffee < MENU['espresso']['ingredients']['coffee']:
            return 'Sorry there is not enough coffee.'
    elif input == '2':
        if machine_water < MENU['latte']['ingredients']['water']:
            return 'Sorry there is not enough water.'
        elif machine_milk < MENU['latte']['ingredients']['milk']:
            return 'Sorry there is not enough milk.'
        elif machine_coffee < MENU['latte']['ingredients']['coffee']:
            return 'Sorry there is not enough coffee.'
    elif input == '3':
        if machine_water >= MENU['cappuccino']['ingredients']['water']:
            return 'Sorry there is not enough water.'
        elif machine_milk >= MENU['cappuccino']['ingredients']['milk']:
            return 'Sorry there is not enough milk.'
        elif machine_coffee >= MENU['cappuccino']['ingredients']['coffee']:
            return 'Sorry there is not enough coffee.'


# Coin processor
def process_coins(user_input):
    print('We accept Quarters, Dimes, Nickles, and Pennies')
    runtime = True
    coin = coin_select()
    tally_payment(coin)
    while runtime:
        add_more = input('Do you want to use other coins too? (Y/N): ').upper()

        if add_more == 'N':
            runtime = False
        elif add_more == 'Y':
            coin = coin_select()
            tally_payment(coin)
            continue
        else:
            print('\nInvalid input. Try again')
            continue

    successful_transaction(user_input)


def coin_select():
    while True:
        coin_selection = input('\nHow will you pay? (Q/D/N/P): ').upper()

        if coin_selection == 'Q' or 'D' or 'N' or 'P':
            break
        else:
            print('\nInvalid input. Try again')
            continue
    return coin_selection


def tally_payment(coin_selection):
    global balance
    quarters = .25
    dimes = .10
    nickles = .05
    pennies = .01
    if coin_selection == 'Q':
        coin_count = int(input("\nHow many Quarters? : "))
        balance += (quarters * coin_count)
    elif coin_selection == 'D':
        coin_count = int(input("\nHow many Dimes : "))
        balance += (dimes * coin_count)
    elif coin_selection == 'N':
        coin_count = int(input("\nHow many Nickles? : "))
        balance += (nickles * coin_count)
    elif coin_selection == 'P':
        coin_count = int(input("\nHow many Pennies? : "))
        balance += (pennies * coin_count)


# TODO: 3. Create transaction system


# Check if the user inserted enough money
def successful_transaction(user_input):
    global money
    global balance
    global payment_processed
    if user_input == '1':
        if balance < MENU['espresso']['cost']:
            return 'Sorry that\'s not enough money. Money refunded.'
        elif balance > MENU['espresso']['cost']:
            change = float(balance - MENU['espresso']['cost'])
            money += balance
            print(f'\nHere is ${change} back in change.')
        else:
            money += balance
    elif user_input == '2':
        if balance < MENU['latte']['cost']:
            return 'Sorry that\'s not enough money. Money refunded.'
        elif balance > MENU['latte']['cost']:
            change = float(balance - MENU['latte']['cost'])
            money += balance
            print(f'\nHere is ${change} back in change.')
        else:
            money += balance
    elif user_input == '3':
        if balance < MENU['cappuccino']['cost']:
            return 'Sorry that\'s not enough money. Money refunded.'
        elif balance > MENU['cappuccino']['cost']:
            change = float(balance - MENU['cappuccino']['cost'])
            money += balance
            print(f'\nHere is ${change} back in change.')
        else:
            money += balance
    make_coffee(user_input)


# Make Coffee
def make_coffee(selection):
    global machine_water
    global machine_milk
    global machine_coffee

    if selection == '1':
        machine_water -= int(MENU['espresso']['ingredients']['water'])
        machine_coffee -= int(MENU['espresso']['ingredients']['coffee'])
        print('\nHere\'s your espresso. Enjoy!')
    elif selection == '2':
        machine_water -= int(MENU['latte']['ingredients']['water'])
        machine_milk -= int(MENU['latte']['ingredients']['milk'])
        machine_coffee -= int(MENU['latte']['ingredients']['coffee'])
        print('\nHere\'s your latte. Enjoy!')
    elif selection == '3':
        machine_water -= int(MENU['cappuccino']['ingredients']['water'])
        machine_milk -= int(MENU['cappuccino']['ingredients']['milk'])
        machine_coffee -= int(MENU['cappuccino']['ingredients']['coffee'])
        print('\nHere\'s your cappuccino. Enjoy!')


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
