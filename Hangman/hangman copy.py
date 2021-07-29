import string

secret_word = 'hello'.lower()
word_letters = set(secret_word)




def main():
    user_input()

def user_input():
    user_input = ''
    valid_input = True
    alphabet = list(string.ascii_lowercase)
    used_letters = []
    available_char = ' '.join(alphabet) 
    while len(word_letters) > 0:
        if len(used_letters) == 0:
            break
        else: 
            #Letters Used
            print('You have used these letters: ', ' '.join(used_letters))

            #Visualization of word
            word_list = [letter if letter in used_letters else '-' for letter in secret_word]
            print('Current Word: ', ' '.join(word_list))
            
    
        while valid_input:
            user_input = str(input(f'Choose a letter from "{available_char}": ').lower())
            
            if user_input in alphabet:
                break
            elif user_input in used_letters:
                print('You already used that Letter')
                continue
            else:
                print('Invalid Input')
                continue

        #game_logic(user_input)

#def progress(used_letters):
   



#user_input()
main()