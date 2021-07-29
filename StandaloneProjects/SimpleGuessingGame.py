
secret_word = 'hello'
user_input = ''
loss = False
guess_amount = 3

while (user_input != secret_word) and (loss != True):
    user_input = input('\nGuess the Secret Word!: ')
    guess_amount -= 1

    if (guess_amount == 0) and (user_input is not secret_word):
        loss = True
    elif (user_input != secret_word):
        if guess_amount > 1:
            print('\nTry Again ' + str(guess_amount) + ' Guesses Left')
        else:
            print('\nTry Again ' + str(guess_amount) + ' Guess Left')

if loss == True:
    print('\nGame Over')
else:
    print('\nCongrats! You Guessed Right!\n')
