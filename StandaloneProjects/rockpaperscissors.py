import random

def main():
    play = True
    
    while play:
        outcome = move_declaration()
        who_wins(outcome)
        play = play_again(play)
        

def move_declaration(): #Declare User and Computer's Move
        options = ['r','p','s']
        valid = True
        while valid:
            user_input = str(input("\nPick Between: 'r' (Rock), 'p' (Paper), 's' (Scissors): ").lower())
            for option in options:
                if user_input == option:
                    valid = False
                else:
                    print('\nInvalid Input')
                    break

        pc_input = random.choice(['r','p','s'])
        outcome = game_logic(user_input, pc_input)
        return outcome

def game_logic(user_input, pc_input): #Rules and Logic for Rock Paper Scissors
    move_key = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    if user_input == pc_input:
        outcome = 1    
    elif (user_input == 'r' and pc_input == 's') or (user_input == 'p' and pc_input == 'r') or (user_input == 's' and pc_input == 'p') :
        print(f'\n{move_key[user_input]} beats {move_key[pc_input]}')
        outcome = 2
    elif ((pc_input == 'r') and (user_input == 's')) or ((pc_input == 'p') and (user_input == 'r')) or ((pc_input == 's') and (user_input == 'p')) :     
        print(f'\n{move_key[pc_input]} beats {move_key[user_input]}')
        outcome = 3
    return outcome

def who_wins(prompt): #Prints out who win each round
    if prompt == 1:
        print("\nIt's a Tie")
    elif prompt == 2:
        print('\nYou Win')
    elif prompt == 3:
        print('\nYou Lose')

def play_again(play):
    while play:
        user_prompt = input('\nPlay Again (Y/N): ').upper()
        
        if user_prompt == 'N':    
            play = False
        elif user_prompt == 'Y':
            break
        else: 
            print('\nInvalid Input')
    return play

if __name__ == '__main__':
    main()