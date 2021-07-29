import random

rand_num = random.randint(0, 100)
correct_guess = False
print("\nI'm Thinking of a number between 0 and 100. What is it?")
while correct_guess == False:
    user_guess = int(input('\nGuess my number: '))

    if user_guess != rand_num:
        if user_guess > rand_num:
            print(f'\n{user_guess} is Greater than My Number\nTry Again')
        elif user_guess < rand_num:
            print(f'\n{user_guess} is Less than My Number\nTry Again')
    elif user_guess == rand_num:
        correct_guess = True
if correct_guess == True:
    print('\nYou Guessed Right!')