

def translate(phrase):
    translation = ''
    vowels = ['a','e','i','o','u']
    for letter in phrase:
        if letter in vowels:
            translation += 'g'
        else:
            translation += letter
   

    print(translation)

translate('aaaaaa')