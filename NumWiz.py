import random

def main():
    run = True
    while run:
        print('\nWelcome to Number Wizard\n')
        mode_select()
        run_again(run)

def mode_select():
    valid = True
    while valid: 
        mode_select = str(input('Choose a mode:\n 1) You Guess Number Wizard\'s Number\n 2) Number Wizard Guesses your Number\n'))
    
        if mode_select == '1':
            guess_num_user(int(input('\nEnter the Start of the Range: ')), int(input('Enter the End of the Range: ')))
            valid = False
        elif mode_select == '2':
            guess_num_wiz(int(input('\nEnter the Start of the Range: ')), int(input('Enter the End of the Range: ')))
            valid = False
        else:
            print('\nInvalid Option')
            continue

def guess_num_user(range_start, range_end):
    print(f"\nI'm thinking of a number between {range_start} and {range_end}. Can you guess it?\n")
    rand_num = random(range_start, range_end)
    correct_guess = False

    while correct_guess == False:
        user_guess = int(input("Enter your guess: "))

        if user_guess != rand_num:
            if user_guess > rand_num:
                print(f'\n{user_guess} is higher than my number. Please Try Again\n')
            elif user_guess < rand_num:
                print(f'\n{user_guess} is lower than my number. Please Try Again\n')
        else:
            correct_guess = True

    if correct_guess == True:
        print('You Guessed Right!')


def guess_num_wiz(range_start, range_end):
    low = range_start
    high = range_end 
    correct_guess = False
    
    while correct_guess == False:
        wiz_guess = int((high + low)  / 2)
        user_answer = input(f'\nIs {wiz_guess} Your Number? (Y/N): ').upper()

        if user_answer == 'N':
            user_prompt = input(f'\nIs {wiz_guess} > or < Than Your Number? (>/<): ')
            if user_prompt == '>':
                high = wiz_guess - 1
            elif user_prompt == '<':
                low = wiz_guess + 1
        elif user_answer == 'Y':
            correct_guess = True
    
    print('\nNumber Wizard Guessed Correctly\n')

def run_again(run):
    while run:
        user_prompt = input('\nPlay Again (Y/N): ').upper()
        
        if user_prompt == 'N':    
            run = False
        elif user_prompt == 'Y':
            break
        else: 
            print('\nInvalid Input')
    return run

if __name__ == '__main__':
    main()